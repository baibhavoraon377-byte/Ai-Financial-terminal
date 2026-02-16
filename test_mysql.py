import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

# Load environment variables
load_dotenv()

# Get connection details
db_config = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

print("🔌 Testing MySQL connection...")
print(f"Host: {db_config['host']}")
print(f"User: {db_config['user']}")
print(f"Database: {db_config['database']}")

try:
    connection = mysql.connector.connect(**db_config)
    
    if connection.is_connected():
        print("✅ SUCCESS! Connected to MySQL")
        connection.close()
        
except Error as e:
    print(f"❌ Error: {e}")