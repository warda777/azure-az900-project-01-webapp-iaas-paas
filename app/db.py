import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"SERVER={os.getenv('DB_SERVER')};"
        f"DATABASE={os.getenv('DB_NAME')};"
        f"UID={os.getenv('DB_USER')};"
        f"PWD={os.getenv('DB_PASSWORD')};"
    )
    return conn


def get_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name FROM users")
    rows = cursor.fetchall()

    users = []
    for row in rows:
        users.append({
            "id": row[0],
            "name": row[1]
        })

    conn.close()
    return users