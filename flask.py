from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
db_config = {
    'host': 'root@localhost',
    'user': 'root',
    'password': 'Harsha@123',
    'database': 'studentPortal',
}

@app.route('/')
def index():
    # Connect to MySQL
    connection = mysql.connector.connect(**db_config)

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Execute a simple query (replace this with your actual query)
    query = "SELECT * FROM students1"
    cursor.execute(query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    # Render the template with the retrieved data
    return render_template('index.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
