import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine

# Load environment variables from .env file
load_dotenv()

# Get database credentials from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT", 5432)  # Default port is 5432

# Construct the database URL
db_url = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create an SQLAlchemy engine
engine = create_engine(db_url)

# Function to load data from the telecom_db database
def load_data(query):
    try:
        # Load data into a pandas DataFrame
        df = pd.read_sql(query, engine)
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage: Replace 'your_table_name' with the actual table name
if __name__ == "__main__":
    query = "SELECT * FROM public.xdr_data"
    df = load_data(query)
    if df is not None:
        print(df.head())  # Display the first few rows of the DataFrame
    else:
        print("Failed to load data.")
