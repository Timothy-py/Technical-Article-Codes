import psycopg2

# Establish a database connection
connection = psycopg2.connect(database="mydb", user="myuser", password="mypassword", host="localhost")

# Create a cursor to execute SQL queries
cursor = connection.cursor()

try:
    # Begin the transaction
    connection.begin()

    # Perform database operations within the transaction
    cursor.execute("INSERT INTO orders (product_id, quantity) VALUES (1, 10)")
    cursor.execute("UPDATE inventory SET quantity = quantity - 10 WHERE product_id = 1")

    # Commit the transaction if all operations succeed
    connection.commit()
except Exception as e:
    # Rollback the transaction if an error occurs
    connection.rollback()
    print("Transaction rolled back due to an error:", str(e))
finally:
    # Close the cursor and database connection
    cursor.close()
    connection.close()
