from flask import Flask , render_template , session , request , jsonify , redirect , url_for , flash
from pymongo import MongoClient
import os
import json
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
import pickle as pkl

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
bcrypt = Bcrypt(app)

client = MongoClient(os.environ['MONGODB_URI'])
db = client.database
users = db.users

with open('decision_tree_model.pkl' , 'rb') as file:
    model = pkl.load(file)
with open('scaler.pkl' , 'rb') as file:
    scaler = pkl.load(file)
with open('mapping.json' , 'r') as file:
    mapp = json.load(file)

def get_user(name , mail):
    docs = users.find({'name' : name , 'mail' : mail})
    return list(docs)[0]
def user_already_exists(name , mail):
    docs = users.find({'name' : name , 'mail' : mail})
    return len(list(docs)) > 0

def encode(mapp , instance):
    for key, value in instance.items():
        if key in mapp and isinstance(mapp[key], dict):
            instance[key] = mapp[key].get(value, value)

@app.route('/')
def home():
    return render_template('home.html' , username = session.get('username' , '') , logged_in = session.get('logged_in' , False))

@app.route('/login' , methods = ['GET' , 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        mail = request.form['mail']
        password = request.form['password']
        if not user_already_exists(name, mail):
            flash("User does not exist, please sign up.")
            return redirect(url_for('signup')) 
        
        user = get_user(name, mail)
        if user and bcrypt.check_password_hash(user['password'], password):
            session['logged_in'] = True
            session['username'] = name
            return redirect(url_for('home'))
        else:
            flash('Invalid password')
    return render_template('login.html')

@app.route('/signup' , methods = ['GET' , 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        mail = request.form['mail']

        if user_already_exists(name , mail):
            flash("User already exists, please login.")
            return redirect(url_for('login'))
        password = request.form['password']

        user = {
            'name' : name,
            'mail' : mail,
            'password' : bcrypt.generate_password_hash(password)
        }
        users.insert_one(user)
        session['logged_in'] = True
        session['username'] = name
        return redirect(url_for('dashboard'))
    
    if not session.get('logged_in'):    
        return render_template('signup.html')

@app.route('/dashboard' , methods = ['GET' , 'POST'])
def dashboard():
    if session.get('logged_in'):
        if request.method == 'POST':
            instance = request.form.to_dict()
            instance.pop('trans_date_trans_time')
            instance.pop('dob')
            encode(mapp , instance)
            instance = list(instance.values())
            instance = [list(map(int , instance))]

            instance = scaler.transform(instance)
            prediction = model.predict(instance)
            if prediction[0]:
                flash('fraud')
            else:
                flash('no fraud')
        return render_template('dashboard.html')
    else:
        return jsonify({'Alert' : 'Cannot access page without authorization'}) , 200

@app.route('/logout')
def logout():
    session.pop('username')
    session.pop('logged_in')

    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug = True , port='8000')