from email import message
from flask import Flask, request, jsonify, render_template,session
import numpy as np
import pandas as pd
from csv import writer
import math
from collections import defaultdict
import csv
from pickle import load
                                                      # Model Class
import pickle
import csv
from os.path import dirname, realpath
import sqlite3  
import re
#model = pickle.load(open('./svc.pkl', 'rb'))
#scaler = pickle.load(open('./scaler.pkl', 'rb'))
app = Flask(__name__)
app.static_folder = 'static'  
app.secret_key = '12345'  

  
con = sqlite3.connect("vw1.db")  
print("Database opened successfully in login")  
     
  
con.execute("create table if not exists account ( fname TEXT NOT NULL, lname TEXT NOT NULL, email TEXT  NOT NULL, password TEXT NOT NULL)")  
  
print("Table account created successfully")  
con.execute("create table if not exists contact ( fname TEXT NOT NULL, lname TEXT NOT NULL, email TEXT  NOT NULL, mobile TEXT NOT NULL,msg text not null )")  
  
print("Table contact created successfully") 
@app.route("/")
def index():
    return render_template("virtual.html")
@app.route("/vw")
def vw():
    return render_template("vw.html")
@app.route("/login", methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form  :
        email = request.form['email']
        password = request.form['password']
        con = sqlite3.connect("vw1.db")  
        print("Database opened successfully in login")  
        con.row_factory = sqlite3.Row  
        cur = con.cursor()  
        cur.execute('SELECT * FROM account WHERE email = ? AND password = ?', (email, password, ))  
        rows = cur.fetchone()
        if rows :
            session['loggedin'] = True
            #session['id'] = cur['id']
            session['email'] = rows['email']
            msg = 'Logged in successfully !'
           
            return render_template('vw.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('virtual.html', msg = msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('email', None)
    return render_template('virtual.html')    
#fname,lname,email,mobile,message 
@app.route("/contact", methods =['GET', 'POST'])
def contact():
    msg = ''
    if request.method == 'POST' and 'fname' in request.form and 'lname' in request.form and 'email' in request.form  and 'mobile' in request.form and 'info' in request.form:
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        mobile = request.form['mobile']
        info=request.form['info']
         
        print("Database opened successfully in contact")  
        
        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', lname):
                msg = 'User lastname must contain only characters and numbers !'
        elif not re.match(r'[A-Za-z0-9]+', fname):
            msg = 'User firstname must contain only characters and numbers !'
        elif not fname or not lname or not email or not mobile or not info:
            msg = 'Please fill out the complete contact form !'
        else:
            s='INSERT INTO contact(fname,lname,email,mobile,msg) VALUES ( ?,?,?,?,?)', (fname,lname, email, mobile, info)
            print(s)
            con = sqlite3.connect("vw1.db")
            con.row_factory = sqlite3.Row   
            cursor = con.cursor()
            cursor.execute('INSERT INTO contact(fname,lname,email,mobile,msg) VALUES (?,?,?,?,?)', (fname,lname, email, mobile, info))
         
            #cursor.execute(s)
            con.commit()
            msg = 'Your contact message stored successfully  !'
            
    #elif request.method == 'POST':
    #    msg = 'Please fill the complete contact form !'
    return render_template('virtual.html', msg = msg)
    
@app.route("/register", methods =['GET', 'POST'])
def register():
    '''msg = ''
    if request.method == 'POST':# and 'fname' in request.form and 'lname' in request.form and 'email' in request.form  and 'password' in request.form and 'cpassword' in request.form and 'tc' in  request.form:
        tc=request.form['tc']
        if not tc:
                msg = 'Please check Agree button in terms and conditions !'
        else:
            fname = request.form['fname']
            lname = request.form['lname']
            email = request.form['email']
            password = request.form['password']
            cpassword = request.form['cpassword']
        
       
            print('tc=',tc)
            con = sqlite3.connect("vw1.db")  
            print("Database opened successfully in registration")  
            con.row_factory = sqlite3.Row  
            cursor = con.cursor()  
            cursor.execute("SELECT * FROM account WHERE email = ?  and password = ?",(email, password))  
        
            account = cursor.fetchone()
            if account:
                msg = 'Account already exists !'
            elif password != cpassword:
                msg="Password and confirm password does not match"    
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = 'Invalid email address !'
            elif not re.match(r'[A-Za-z0-9]+', lname):
                msg = 'User lastname must contain only characters and numbers !'
            elif not re.match(r'[A-Za-z0-9]+', fname):
                msg = 'User firstname must contain only characters and numbers !'
            elif not fname or not lname or not email or not password:
                msg = 'Please fill out the form !'
            else:
                s='INSERT INTO account(fname,lname,email,password) VALUES ( ?,?,?,?)', (fname,lname, email, password )
                print(s)
            
                cursor.execute('INSERT INTO account(fname,lname,email,password) VALUES (?,?,?,?)', (fname, lname,  email , password  ))
         
            #cursor.execute(s)
                con.commit()
                msg = 'You have successfully registered !'
            
    elif request.method == 'POST':
        msg = 'Please fill the complete form !'
    return render_template('virtual.html', msg = msg)'''
    msg = ''
    if request.method == 'POST' and 'fname' in request.form and 'lname' in request.form and 'email' in request.form  and 'password' in request.form :
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        password = request.form['password']
        #cpassword = request.form['cpassword']  
        #tc=request.form['tc']
        #if not tc:
        #        msg = 'Please check Agree button in terms and conditions !'     
        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', lname):
                msg = 'User lastname must contain only characters and numbers !'
        elif not re.match(r'[A-Za-z0-9]+', fname):
            msg = 'User firstname must contain only characters and numbers !'
        elif not fname or not lname or not email or not password :
            msg = 'Please fill out the complete contact form !'
        else:
            s='INSERT INTO account(fname,lname,email,password) VALUES ( ?,?,?,?)', (fname,lname, email, password)
            print(s)
            con = sqlite3.connect("vw1.db")
            con.row_factory = sqlite3.Row   
            cursor = con.cursor()
            cursor.execute('INSERT INTO account(fname,lname,email,password) VALUES (?,?,?,?)', (fname,lname, email, password))
         
            #cursor.execute(s)
            con.commit()
            msg = 'Your account opened successfully  !'
            
    #elif request.method == 'POST':
    #    msg = 'Please fill the complete contact form !'
    return render_template('virtual.html', msg = msg)





if __name__ == "__main__":
	app.run()