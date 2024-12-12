import json
import psycopg2
from src.utils.database_connection import DB_CONFIG


INSERT_SQL = """
INSERT INTO mandate (business_partner_id,mandate_status,collection_frequency,brand,
                     row_update_datetime,row_create_datetime,changed_by,mandate_id,
                     collection_type,metering_consent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (business_partner_id) DO NOTHING;
"""


SELECT_SQL = """
SELECT * FROM mandate WHERE row_create_datetime = '2019-07-02 10:00:00';
"""




def load_mandate_data(json_file, db_config):
    try:
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()

        with open(json_file, 'r') as file:
            data = json.load(file)

        for record in data:
            cur.execute(INSERT_SQL, (
                record['business_partner_id'], record['mandate_status'],
                record['collection_frequency'], record['brand'], record['row_update_datetime'],
                record['row_create_datetime'], record['changed_by'], record['mandate_id'],
                record['collection_type'], record['metering_consent']
            ))

        conn.commit()
        print("JSON data uploaded successfully.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def export_mandate_data(output_json_file, db_config):
    try:
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()

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
        if conn:
            conn.close()


if __name__ == "__main__":
    execute_load = False

    if execute_load:
        load_mandate_data(r"/data/mandate_data.json", DB_CONFIG)

    export_mandate_data("../data/output_mandate_data.json", DB_CONFIG)