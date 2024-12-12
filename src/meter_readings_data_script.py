import json
from psycopg2.extras import Json
from src.utils.database_connection import conn


INSERT_SQL = """
INSERT INTO meter_readings (account_id, brand, connection_ean_code, energy_type, meter_number,
                   reading_date, reading_electricity, reading_gas, rejection,
                   validation_status)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
"""

SELECT_SQL = """
SELECT * FROM meter_readings WHERE energy_type = 'GAS';
"""

def load_meter_readings_data(json_file, db_config):
    try:
        con = conn(db_config)
        cur = con.cursor()

        with open(json_file, 'r') as file:
            data = json.load(file)

        for record in data:

            reading_electricity = Json(record['reading_electricity']) if isinstance(record['reading_electricity'], dict) else record['reading_electricity']
            reading_gas = Json(record['reading_gas']) if isinstance(record['reading_gas'], dict) else record['reading_gas']
            rejection = Json(record['rejection']) if isinstance(record['rejection'], dict) else record['rejection']

            cur.execute(INSERT_SQL, (
                record['account_id'], record['brand'],
                record['connection_ean_code'], record['energy_type'], record['meter_number'],
                record['reading_date'], reading_electricity,
                reading_gas, rejection, record['validation_status']
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


def export_meter_readings_data(output_json_file, db_config):
    try:
        con = conn(db_config)
        cur = con.cursor()

        cur.execute(SELECT_SQL)
        rows = cur.fetchall()

        column_names = [desc[0] for desc in cur.description]
        data = [dict(zip(column_names, row)) for row in rows]

        with open(output_json_file, 'w') as output_file:
            json.dump(data, output_file, indent=4, default=str)

        print(f"Data is registered to {output_file} .")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if cur:
            cur.close()

        if con:
            con.close()







