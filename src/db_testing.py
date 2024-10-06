import libsql_experimental as libsql
import os

url = os.getenv("TURSO_DATABASE_URL")
auth_token = os.getenv("TURSO_AUTH_TOKEN")

conn = libsql.connect("hello.db", sync_url=url, auth_token=auth_token)
conn.sync()

# conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER);")
# conn.execute("INSERT INTO users(id) VALUES (10);")
# amount = '24.3'
# category = 'Food'
# date = '2024-10-11'

def add_expense(amount, category, date):
    conn.execute("insert into Expenses(amount, category, date) values ('"+amount+"', '"+category+"', '"+date+"')")
    conn.commit()
    conn.sync()

def get_expenses(date):
    conn.sync()
    return conn.execute("select * from Expenses where date = '"+date+"'").fetchall()

# print(conn.execute("select * from Expenses").fetchall())
# conn.execute("insert into Expenses(amount, category, date) values ('"+amount+"', '"+category+"', '"+date+"')")
print(add_expense('11.32', 'School', '2024-08-26'))
print("get 1: ")
print(get_expenses('2023-07-15'))

conn.sync()

print("get 2: ")

print(conn.execute("select * from Expenses").fetchall())
