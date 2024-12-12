import json
import psycopg2
from multiprocessing import Pool
from src.utils.database_connection import DB_CONFIG


INSERT_SQL = """
INSERT INTO meter (business_partner_id,connection_ean_code,grid_company_code,oda_code,meter_number,
                   smart_collectable,brand,sjv1,sjv2,installation,division,move_out_date,
                   row_create_datetime,move_in_date)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (meter_number) DO NOTHING;
"""

SELECT_SQL = """
SELECT * FROM meter WHERE business_partner_id = '0100000022';
"""

BATCH_SIZE = 1000

def process_batch(batch):

    try:
        with psycopg2.connect(**DB_CONFIG) as conn:
            cur = conn.cursor()
            cur.executemany(INSERT_SQL, batch)
            conn.commit()
    except Exception as e:
        print(f"Batch processing error: {e}")

def load_meter_data(json_file, db_config):

    try:
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()


        cur.execute("SELECT business_partner_id FROM mandate")
        mandate_bpi_set = set(row[0] for row in cur.fetchall())


        with open(json_file, 'r') as file:
            data = json.load(file)


        filtered_data = []
        for record in data:
            bpi = record['business_partner_id']
            if bpi in mandate_bpi_set:
                filtered_data.append((
                    bpi, record['connection_ean_code'], record['grid_company_code'], record['oda_code'],
                    record['meter_number'], record['smart_collectable'], record['brand'],
                    record['sjv1'], record['sjv2'], record['installation'], record['division'],
                    record['move_out_date'], record['row_create_datetime'], record['move_in_date']
                ))
            else:
                print(f"Skipping business_partner_id {bpi} as it does not exist in mandate table.")


        batches = [filtered_data[i:i + BATCH_SIZE] for i in range(0, len(filtered_data), BATCH_SIZE)]


        with Pool(processes=4) as pool:
            pool.map(process_batch, batches)

        print("JSON data uploaded successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def export_meter_data(output_json_file, db_config):

    try:
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()

        cur.execute(SELECT_SQL)
        rows = cur.fetchall()

        column_names = [desc[0] for desc in cur.description]
        data = [dict(zip(column_names, row)) for row in rows]

        with open(output_json_file, 'w') as output_file:
            json.dump(data, output_file, indent=4, default=str)

        print(f"Data is registered to {output_file.name}.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == "__main__":

    execute_load = False

    if execute_load:
        load_meter_data(r"/data/meter_data.json", DB_CONFIG)

    export_meter_data("../data/output_meter_data.json", DB_CONFIG)


