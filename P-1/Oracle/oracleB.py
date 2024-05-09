import cx_Oracle
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

def create_db_url(username, password, host, port, sid):
    """
    Create a database URL for SQLAlchemy.
    """
    oracle_url = URL.create(
        "oracle+cx_oracle",
        username=username,
        password=password,
        host=host,
        port=port,
        database=sid
    )
    return oracle_url

def get_engine(db_url):
    """
    Create an SQLAlchemy engine.
    """
    return create_engine(db_url)

def query_data(engine, query):
    """
    Execute a query and return a DataFrame.
    """
    with engine.connect() as connection:
        return pd.read_sql(query, connection)

def main():
    # Database credentials and info
    username = 'your_username'
    password = 'your_password'
    host = 'your_host'
    port = '1521'  # Default Oracle port
    sid = 'your_sid'

    # SQL Query
    query = "SELECT * FROM your_table"

    # Create a database URL and engine
    db_url = create_db_url(username, password, host, port, sid)
    engine = get_engine(db_url)

    # Fetch data
    df = query_data(engine, query)
    print(df)

if __name__ == "__main__":
    main()
