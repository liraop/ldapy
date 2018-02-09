from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from ldap3 import Server, Connection, ALL, NTLM
from models.ldap_objects import Domain
from utils import test_connection

import os

app = Flask(__name__)

registered_domains = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def do_login():

    return index()

@app.route('/domain', methods=['POST'])
def connection():
    domain = Domain(request.form['domain'], request.form ['user'], request.form['pass'], request.form['domainType'])
    server = Server(domain.url, get_info=ALL)

    if (domain.kind == 'AD'):
        con = Connection(server, domain.url+"\\"+domain.bind_user , domain.bind_pw, authentication=NTLM)
    elif (domain.kind == 'LDAP'):
        con = Connection(server, domain.bind_user, domain.bind_pw, auto_bind=True)

    if (request.form['submit'] == 'Test Connection'):
        if (test_connection(con)):
            flash('Connection Successful!')
        else:
            flash('Connection Failed!')
    elif (request.form['submit'] == 'Register Domain'):
        registered_domains.append(domain)
        flash('Domain registered!')

    return render_template('index.html', domain_list=registered_domains)


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0')
