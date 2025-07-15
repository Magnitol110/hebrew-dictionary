
from flask import Flask, render_template
import sqlite3, os

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect(os.path.join('data', 'dictionary.db'))
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    words = conn.execute("SELECT * FROM words ORDER BY category").fetchall()
    conn.close()
    return render_template('index.html', words=words)

if __name__ == '__main__':
    app.run(debug=True)
