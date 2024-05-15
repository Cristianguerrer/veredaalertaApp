from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
import os
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/veredaalerta"
app.secret_key = 'your_secret_key'
mongo = PyMongo(app)
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = mongo.db.users.find_one({'email': email})
        if user and bcrypt.check_password_hash(user['password'], password):
            session['username'] = user['username']
            return redirect(url_for('index'))
        return 'Invalid email or password'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        mongo.db.users.insert_one({'username': username, 'email': email, 'password': hashed_password})
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/add_alert', methods=['POST'])
def add_alert():
    if 'username' not in session:
        return redirect(url_for('login'))
    message = request.form['message']
    level = request.form['level']
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alert = {"message": message, "level": level, "timestamp": timestamp}
    alert_id = mongo.db.alerts.insert_one(alert).inserted_id
    alert["_id"] = str(alert_id)
    return jsonify(alert)

@app.route('/get_alerts', methods=['GET'])
def get_alerts():
    alerts = []
    for alert in mongo.db.alerts.find():
        alert["_id"] = str(alert["_id"])
        alerts.append(alert)
    return jsonify(alerts)

@app.route('/delete_alert/<alert_id>', methods=['DELETE'])
def delete_alert(alert_id):
    mongo.db.alerts.delete_one({"_id": ObjectId(alert_id)})
    return jsonify({"success": True})

@app.route('/update_alert/<alert_id>', methods=['PUT'])
def update_alert(alert_id):
    message = request.form['message']
    level = request.form['level']
    mongo.db.alerts.update_one(
        {"_id": ObjectId(alert_id)},
        {"$set": {"message": message, "level": level}}
    )
    return jsonify({"success": True})

@app.route('/filter_alerts/<level>', methods=['GET'])
def filter_alerts(level):
    alerts = []
    for alert in mongo.db.alerts.find({"level": level}):
        alert["_id"] = str(alert["_id"])
        alerts.append(alert)
    return jsonify(alerts)

if __name__ == "__main__":
    app.run(debug=True)
