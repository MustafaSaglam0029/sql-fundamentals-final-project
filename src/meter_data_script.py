import json
from src.utils.database_connection import conn


INSERT_SQL = """
INSERT INTO meter (business_partner_id,connection_ean_code,grid_company_code,oda_code,meter_number,
                   smart_collectable,brand,sjv1,sjv2,installation,division,move_out_date,
                   row_create_datetime,move_in_date)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
"""

SELECT_SQL = """
SELECT * FROM meter WHERE business_partner_id = '0100000022';
"""


def load_meter_data(json_file, db_config):

    try:
        con = conn(db_config)
        cur = con.cursor()



        with open(json_file, 'r') as file:
            data = json.load(file)


        for record in data:
            cur.execute(INSERT_SQL, (
                record['business_partner_id'], record['connection_ean_code'], record['grid_company_code'],
                record['oda_code'],record['meter_number'], record['smart_collectable'], record['brand'],
                record['sjv1'], record['sjv2'], record['installation'], record['division'],
                record['move_out_date'], record['row_create_datetime'], record['move_in_date']
                ))

        con.commit()
        print("JSON data uploaded successfully.")



    except Exception as e:
        print(f"Error: {e}")

    finally:
        if cur:
            cur.close()

        if con:
            con.close()

def export_meter_data(output_json_file, db_config):

    try:
        con = conn(db_config)
        cur = con.cursor()

        cur.execute(SELECT_SQL)
        rows = cur.fetchall()

        column_names = [desc[0] for desc in cur.description]
        data = [dict(zip(column_names, row)) for row in rows]

        with open(output_json_file, 'w') as output_file:
            json.dump(data, output_file, indent=4, default=str)

        print(f"Data is registered to {output_file}.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if cur:
            cur.close()

        if con:
            con.close()




