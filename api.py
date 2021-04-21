import flask
# from flask_mail import Mail, Message
from flask import Flask, render_template, request, redirect, url_for
import db_connector
import psycopg2
# mail= Mail(app)

app = Flask('wedding_app', static_url_path='')

@app.route('/submitted', methods=['GET', 'POST'])
def post():
    
    # Define parameters
    attendance = request.form['Attendance']
    name = request.form['Name']
    email = request.form['Email']
    affiliation = request.form['Affiliation']
    anythingelse = request.form['AnythingElse']
    
    try:
        pass
        # Write to DB
        db_connector.write_to_mysql(name, attendance, email, affiliation ,anythingelse)
    except Exception:
        return render_template('error.html')
    
    return render_template('submitted.html')

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/connect')
def connect():
    import configparser
    config = configparser.ConfigParser()
    config.read('config.ini')
    try:
        #host='172.17.0.1' is the defult IP for the docker container that it is being created during the deployment of the App Engine
        conn =  psycopg2.connect(user = "postgres",
                            password = config['credentials']['password'],
                            host = config['credentials']['host'],
                            # host='localhost',
                            port = "5432",
                            database = "postgres")
        return "Connection was established!"
    except:
        return "I am unable to connect to the database"


if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)
   