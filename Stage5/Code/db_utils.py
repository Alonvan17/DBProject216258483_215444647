import psycopg2


def connect():
    return psycopg2.connect(
        dbname="mydatabase",
        user="vangelde",
        password="avgelder1379",
        host="localhost",
        port="5432"
    )
