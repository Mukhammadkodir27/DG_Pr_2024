from flask import Flask, render_template, request, redirect, session
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

conn = mysql.connector.connect(host="sql11.freesqldatabase.com",
                               user="sql11679514", password="9W2PbvePXk", database="sql11679514")


cursor = conn.cursor()


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/register')
def about():
    return render_template('register.html')


@app.route('/home')
def home():
    if 'user_id' in session:
        return render_template('home.html')
    else:
        return redirect('/register')


@app.route('/login_validation', methods=['POST'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')

    cursor.execute(
        """SELECT * FROM `login` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email, password))
    users = cursor.fetchall()
    if len(users) > 0:
        session['user_id'] = users[0][0]
        return redirect('/home')
    else:
        return redirect('/')


@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get('uname')
    email = request.form.get('uemail')
    password = request.form.get('upassword')

    cursor.execute("""INSERT INTO `login` (`user_id`, `name`, `email`, `password`) VALUES (NULL,'{}','{}','{}')""".format(
        name, email, password))
    conn.commit()

    cursor.execute(
        """SELECT * FROM `login` WHERE `email` LIKE '{}'""".format(email))
    myuser = cursor.fetchall()

    if myuser:
        session['user_id'] = myuser[0][0]
        return redirect('/home')
    else:
        return redirect('/')


@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/login')


if __name__ == "__main__":
    app.run(debug=True)
