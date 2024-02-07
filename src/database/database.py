import psycopg2

def connect_to_database():
    db_host = "localhost"
    db_port = "5432"
    db_name = "postgres"
    db_user = "postgres"
    db_password = "postgres"

    conn = psycopg2.connect(host=db_host, port=db_port, dbname=db_name, user=db_user, password=db_password)
    return conn

def close_connection(conn):
    conn.close()
