import libsql_experimental as libsql
import os
from flask import Flask, render_template, request # new

app = Flask(__name__) #new

url = os.getenv("TURSO_DATABASE_URL")
auth_token = os.getenv("TURSO_AUTH_TOKEN")

conn = libsql.connect("hello.db", sync_url=url, auth_token=auth_token)
conn.sync()

# conn.execute("CREATE TABLE IF NOT EXISTS Expenses (amount INTEGER, category TEXT, data TEXT);") #NEW CHANGES
# conn.commit() #NEW
# conn.sync #NEW

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

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == "POST":
        # Get data from the form
        amount = request.form["amount"]
        category = request.form["category"]
        date = request.form["date"]
        
        # Add the expense to the database
        add_expense(amount, category, date)

    # retrieve expenses based on date
    # date_query = request.args.get('date')
    # expenses = get_expenses(date_query) if date_query else []

    return render_template("main.html", expenses=expenses)

print(add_expense('11.32', 'School', '2024-08-26'))
print("get 1: ")
print(get_expenses('2023-07-15'))

conn.sync()

print("get 2: ")

print(conn.execute("select * from Expenses").fetchall())
