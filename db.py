import os
import psycopg2
from faker import Faker

def get_db():
    os.environ['PG_CONTAINER_NAME'] = "pg_test_instance"
    os.environ['PG_PORT'] = "5432"
    os.environ['PG_DB'] = "mydb"
    os.environ['PG_USER'] = "myuser"
    os.environ['PG_PASSWORD'] = "mysecretpassword"

    conn = psycopg2.connect(
        host="localhost",
        database=os.environ['PG_DB'],
        user=os.environ['PG_USER'],
        password=os.environ['PG_PASSWORD'],
        port=os.environ['PG_PORT']
    )

    return conn

def test_pg():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
    print(cursor.fetchall())
    conn.close()
    
def create_tables(drop_tables=False):
    conn = get_db()
    cursor = conn.cursor()
    if drop_tables:
        cursor.execute("DROP TABLE IF EXISTS users")
        cursor.execute("DROP TABLE IF EXISTS channels")
        cursor.execute("DROP TABLE IF EXISTS messages")
    #users table
    #id, name
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(255))")
    
    #channels table
    #id, name
    cursor.execute("CREATE TABLE IF NOT EXISTS channels (id SERIAL PRIMARY KEY, name VARCHAR(255))")
    
    #messages table
    #id, channel_id, sender_id, message, ctime
    cursor.execute("CREATE TABLE IF NOT EXISTS messages (id SERIAL PRIMARY KEY, channel_id INT, sender_id INT, message VARCHAR(255), ctime TIMESTAMP)")
    
    #membership table
    #id, user_id, channel_id
    cursor.execute("CREATE TABLE IF NOT EXISTS membership (id SERIAL PRIMARY KEY, user_id INT, channel_id INT)")
    conn.commit()
    conn.close()
    
def insert_data():
    conn = get_db()
    cursor = conn.cursor()
    fake = Faker()
    for i in range(10):
        name = fake.name()
        cursor.execute("INSERT INTO users (name) VALUES ('%s')" % name)
        
    #2 channels
    cursor.execute("INSERT INTO channels (name) VALUES ('channel1')")
    cursor.execute("INSERT INTO channels (name) VALUES ('channel2')")
    
    #user 1-5 in channel 1
    cursor.execute("INSERT INTO membership (user_id, channel_id) VALUES (1, 1)")
    cursor.execute("INSERT INTO membership (user_id, channel_id) VALUES (2, 1)")
    cursor.execute("INSERT INTO membership (user_id, channel_id) VALUES (3, 1)")
    cursor.execute("INSERT INTO membership (user_id, channel_id) VALUES (4, 1)")
    cursor.execute("INSERT INTO membership (user_id, channel_id) VALUES (5, 1)")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables(drop_tables=True)
    test_pg()
    insert_data()
    
    