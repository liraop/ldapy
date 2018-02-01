from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from ldap3 import Server, Connection

import os

app = Flask(__name__)

registered_domains = []

@app.route('/')
def home():
    return render_template('login.html')


@app.route('/domain', methods=['POST'])
def connection():
    domain = request.form['domain']

    server = Server(domain, get_info='ALL')
    con = Connection(server, auto_bind=True)

    if (request.form['submit'] == 'Test Connection'):
        if (con.bind()):
            print("Connection successful")
        else:
            print("Connection failed")
    elif (request.form['submit'] == 'Register Domain'):
        registered_domains.append(con)
        print('added')

    return home()


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0')
