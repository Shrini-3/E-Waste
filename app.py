from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)

# For testing purposes, a dummy user dictionary
users = {
    'user@example.com': 'password123',
    # Add more users as needed
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    # Check if the provided credentials are valid
    if email in users and users[email] == password:
        # Redirect to the dashboard on successful login
        return redirect(url_for('dashboard'))
    else:
        # Handle invalid credentials (you may want to show an error message)
        return render_template('index.html', error='Invalid credentials. Please try again.')

@app.route('/dashboard')
def dashboard():
    # Add logic for the dashboard here
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
