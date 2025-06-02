import psycopg2

from coin_api_streaming.constants import (
    POSTGRES_HOST
    , POSTGRES_DB
    , POSTGRES_PORT
    , POSTGRES_PASSWORD
    , POSTGRES_USER
)


conn = psycopg2.connect(
    host=POSTGRES_HOST,
    port=POSTGRES_PORT,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    dbname=POSTGRES_DB,
)
cur = conn.cursor()
cur.execute("SELECT current_database(), inet_server_addr();")
print("Connected to DB:", cur.fetchone())
cur.close()
conn.close()
