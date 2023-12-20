from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# MySQL configurations
db = pymysql.connect(
    host='localhost',
    user='new_user',
    password='admin',
    database='journal_app',
    cursorclass=pymysql.cursors.DictCursor
)

# Create a cursor object
cursor = db.cursor()

@app.route('/')
def index():
    # Example: Fetch entries from the database
    cursor.execute("SELECT * FROM entries")
    entries = cursor.fetchall()
    return render_template('index.html', entries=entries)

# Example route for adding new entries
@app.route('/add_entry', methods=['POST'])
def add_entry():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        # Example: Insert new entry into the database
        sql = "INSERT INTO entries (title, content) VALUES (%s, %s)"
        cursor.execute(sql, (title, content))
        db.commit()

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
