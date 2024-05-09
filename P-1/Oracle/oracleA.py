import cx_Oracle
import pandas as pd

def create_connection(user, password, dsn):
  """
  Creates a connection to the Oracle database.
  """
  try:
    connection = cx_Oracle.connect(
        user=user,
        password=password,
        dsn=dsn
    )
    return connection
  except cx_Oracle.Error as error:
    print("Error connecting to Oracle:", error)
    return None

def execute_query(connection, query):
  """
  Executes the given SQL query and returns the result.
  """
  cursor = connection.cursor()
  try:
    cursor.execute(query)
    result = cursor.fetchall()
    return result
  except cx_Oracle.Error as error:
    print("Error executing query:", error)
    return None
  finally:
    cursor.close()

def convert_to_dataframe(result):
  """
  Converts the query result to a pandas DataFrame.
  """
  columns = [column[0] for column in cursor.description]
  df = pd.DataFrame(result, columns=columns)
  return df

def main():
  """
  Main function to connect, execute, and retrieve data.
  """
  # Replace with your actual credentials and DSN
  user = "your_username"
  password = "your_password"
  dsn = "your_database_dsn" 

  # Replace with your actual SQL query
  query = "SELECT * FROM your_table"

  connection = create_connection(user, password, dsn)
  if connection:
    result = execute_query(connection, query)
    if result:
      df = convert_to_dataframe(result)
      print(df)
    connection.close()

if __name__ == "__main__":
  main()
