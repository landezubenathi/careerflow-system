# db_connection.py
import pyodbc

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=SERVER_NAME;"
    "DATABASE=DATABASE_NAME;"
    "UID=Career26Flow;"
    "PWD=strongPasword"
)