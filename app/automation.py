import sqlite3
from flask import Flask, render_template, request, session, redirect


app = Flask(__name__)
app.secret_key = 'kQ6i2392anhJ'


@app.route('/')
def home():
    if 'username' in session:
        return render_template('index.html')
    else:
        return redirect('/login')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        with sqlite3.connect('UsersStudent.db') as conn:
            cursor = conn.cursor()
            
            # Check if username and password match in the database
            cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
            user = cursor.fetchone()
            
            if user:
                session['username'] = username
                return redirect('/')
            else:
                error = 'Invalid username or password'
                return render_template('login.html', error=error)
        
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')


@app.route('/submit', methods=['POST'])
def submit():
    if 'username' in session:
        name = request.form['name']
        age = request.form['age']
        
        # Perform automation tasks here
        
        return render_template('result.html', name=name, age=age)
    else:
        return redirect('/login')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        with sqlite3.connect('UsersStudent.db') as conn:
            cursor = conn.cursor()
            
            # Check if the username already exists
            cursor.execute('SELECT * FROM users WHERE username=?', (username,))
            existing_user = cursor.fetchone()
            
            if existing_user:
                error = 'Username already exists'
                return render_template('register.html', error=error)
            
            # Insert the new user into the database
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            
            session['username'] = username
            return redirect('/')
        
    return render_template('register.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)