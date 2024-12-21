import psycopg2

db_config = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "1234",
    "host": "127.0.0.1",
    "port": "5432"
}

def conn(db_config):
        connection = psycopg2.connect(**db_config)
        return connection

con = conn(db_config)
con.close()











