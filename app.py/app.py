from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    tribe = db.Column(db.String(50), nullable=False)
    sub_county = db.Column(db.String(50), nullable=False)
    jaundice = db.Column(db.String(3), nullable=False)
    used_app = db.Column(db.String(3), nullable=False)
    asd_result = db.Column(db.String(3), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Retrieve user input
        username = request.form['username']
        gender = request.form['gender']
        age = int(request.form['age'])
        tribe = request.form['tribe']
        sub_county = request.form['sub_county']
        jaundice = request.form['jaundice']
        used_app = request.form['used_app']

        # Mock the ASD prediction result (replace with your actual prediction logic)
        asd_result = 'Yes' if age > 10 else 'No'

        # Save user data to the database
        new_user = User(
            username=username,
            gender=gender,
            age=age,
            tribe=tribe,
            sub_county=sub_county,
            jaundice=jaundice,
            used_app=used_app,
            asd_result=asd_result
        )
        db.session.add(new_user)
        db.session.commit()

        return render_template('result.html', result=asd_result)

    except Exception as e:
        flash('An error occurred. Please try again.', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
