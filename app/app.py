import json
import mysql.connector
import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World!" + os.getenv('MYSQL_ROOT_USER')


@app.route('/initdb')
def db_init():
    mydb = mysql.connector.connect(
        host="db",
        user=os.getenv('MYSQL_ROOT_USER'),
        password=os.getenv('MYSQL_ROOT_PASSWORD'),
    )
    cursor = mydb.cursor()

    cursor.execute("DROP DATABASE IF EXISTS inventory")
    cursor.execute("CREATE DATABASE inventory")
    cursor.close()

    mydb = mysql.connector.connect(
        host="db",
        user=os.getenv('MYSQL_ROOT_USER'),
        password=os.getenv('MYSQL_ROOT_PASSWORD'),
        database="inventory"
    )
    cursor = mydb.cursor()

    cursor.execute("DROP TABLE IF EXISTS widgets")
    cursor.execute("CREATE TABLE widgets (name VARCHAR(255), description VARCHAR(255))")
    cursor.close()

    return 'init database'


@app.route('/widgets')
def get_widgets():
    mydb = mysql.connector.connect(
        host="db",
        user=os.getenv('MYSQL_ROOT_USER'),
        password=os.getenv('MYSQL_ROOT_PASSWORD'),
        database="inventory"
    )
    cursor = mydb.cursor()

    cursor.execute("SELECT * FROM widgets")
    row_headers=[x[0] for x in cursor.description]

    results = cursor.fetchall()
    json_data = []
    for result in results:
        json_data.append(dict(zip(row_headers, result)))

    cursor.close()
    return json.dumps(json_data)

