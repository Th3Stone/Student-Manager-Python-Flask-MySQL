from flask import Flask, render_template, request, redirect, url_for 
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor()

# Route (HOME)

@app.route('/')
def index():
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    return render_template('index.html', students = students)

#Adding Students
@app.route('/add', methods = ['POST'])
def add_student():
    name = request.form['name']
    age = request.form['age']
    grade = request.form['grade']
    cursor.execute('INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)', (name, age, grade))
    db.commit() #saving the changes

    return redirect(url_for('index'))

# Delete Student 

@app.route('/delete/<int:id>')
def delete_student(id):
    cursor.execute('DELETE FROM students WHERE id= %s', (id,))
    db.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


