
from email import message
import this
from urllib import response
from flask import Flask
from flask import Flask, request, jsonify, render_template,session
import numpy as np
import pandas as pd
from csv import writer
import math
from collections import defaultdict
import csv
from pickle import load
import os
                                                      # Model Class
import pickle
import csv
from os.path import dirname, realpath
import sqlite3  
import re
#model = pickle.load(open('./svc.pkl', 'rb'))
#scaler = pickle.load(open('./scaler.pkl', 'rb'))
app = Flask(__name__)
#lask.Flask(__name__) 
app.static_folder = 'static'  
app.secret_key = '12345'  




con = sqlite3.connect("vw1.db")  
print("Database opened successfully in login")  
     
  
con.execute("create table if not exists account ( fname TEXT NOT NULL, lname TEXT NOT NULL, email TEXT  NOT NULL, password TEXT NOT NULL)")  
  
print("Table account created successfully")  
con.execute("create table if not exists contact ( fname TEXT NOT NULL, lname TEXT NOT NULL, email TEXT  NOT NULL, mobile TEXT NOT NULL,msg text not null )")  
  
print("Table contact created successfully") 
import cv2
import mediapipe as mp
import numpy as np

'''@app.route('/open')
def open():
    if not cap.isOpened():
        cap = cv2.VideoCapture(0) 
    return render_template("vw.html")
@app.route('/done')
def done():
    if cap.isOpened():
        print("Releasing cam feed")
        cap.release()
        cv2.destroyAllWindows()
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('email', None)
    return render_template('virtual.html')
    return render_template("vw.html")'''
# Angles

def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)

    if angle > 180.0:
        angle = 360-angle

    return angle
def generate_frame1():
    
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose

    cap = cv2.VideoCapture(0)
    counter = 0
    stage = None
    #cap = cv2.VideoCapture(0)
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            results = pose.process(image)

            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

#-------------------------------------------------------------------------------
# Curl Counter

            try:
                landmarks = results.pose_landmarks.landmark
                

                shoulder = [ landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                elbow = [ landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                wrist = [ landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]


                angle = calculate_angle(shoulder, elbow, wrist)

            # visualize angle
                cv2.putText(image, str(angle),
                           tuple(np.multiply(elbow, [640, 480]).astype(int)),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                 )
                if angle > 160:
                    stage = "down"
                if angle < 30 and stage == 'down':
                    stage = "up"
                    counter += 1
                    print(counter)

                
            except:
                pass

#-------------------------------------------------------------------------------
# Show

            cv2.rectangle(image, (0,0), (255,83), (245,117,16), -1)

            # Curls Data
            cv2.putText(image, 'Curls', (20,12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
            cv2.putText(image, str(counter),
                    (10,60),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)

            # stage
            cv2.putText(image, 'STAGE', (90,12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
            cv2.putText(image, stage,
                    (90,60),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)


            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2),

                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                                 )


            cv2.imshow("MediaPipe Image Curl Project", image)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        session.pop('loggedin', None)
        session.pop('id', None)
        session.pop('email', None)        
        cap.release()
        cv2.destroyAllWindows()  
    return render_template('virtual.html')  
def generate_frame2():
    
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose

    cap = cv2.VideoCapture(0)
    counter = 0
    stage = None
    #cap = cv2.VideoCapture(0)
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            results = pose.process(image)

            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

#-------------------------------------------------------------------------------
# triceps Counter

            try:
                landmarks = results.pose_landmarks.landmark
                

                shoulder = [ landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                elbow = [ landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                wrist = [ landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]


                angle = calculate_angle(shoulder, elbow, wrist)

            # visualize angle
                cv2.putText(image, str(angle),
                           tuple(np.multiply(elbow, [640, 480]).astype(int)),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                 )
                if angle > 155: 
                    stage = "up"
                if angle < 90 and stage == 'up':
                    stage = "down"
                    counter += 1
                    print(counter)

                
            except:
                pass

#-------------------------------------------------------------------------------
# Show

            cv2.rectangle(image, (0,0), (255,83), (245,117,16), -1)

            # Curls Data
            cv2.putText(image, 'Curls', (20,12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
            cv2.putText(image, str(counter),
                    (10,60),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)

            # stage
            cv2.putText(image, 'STAGE', (90,12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
            cv2.putText(image, stage,
                    (90,60),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)


            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2),

                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                                 )


            cv2.imshow("MediaPipe Image Curl Project", image)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        session.pop('loggedin', None)
        session.pop('id', None)
        session.pop('email', None)        
        cap.release()
        cv2.destroyAllWindows()  
    return render_template('virtual.html')      
def generate_frame3():
    
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose

    cap = cv2.VideoCapture(0)
    counter = 0
    stage = None
    #cap = cv2.VideoCapture(0)
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            results = pose.process(image)

            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

#-------------------------------------------------------------------------------
# Shoulders Counter

            try:
                landmarks = results.pose_landmarks.landmark
                

                shoulder = [ landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                elbow = [ landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                wrist = [ landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]


                angle = calculate_angle(shoulder, elbow, wrist)

            # visualize angle
                cv2.putText(image, str(angle),
                           tuple(np.multiply(elbow, [640, 480]).astype(int)),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                 )
                if angle > 155: #chest
                    stage = "up"
                if angle < 65 and stage == 'up':
                    stage = "down"
                    counter += 1
                    print(counter)

                
            except:
                pass

#-------------------------------------------------------------------------------
# Show

            cv2.rectangle(image, (0,0), (255,83), (245,117,16), -1)

            # Curls Data
            cv2.putText(image, 'Curls', (20,12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
            cv2.putText(image, str(counter),
                    (10,60),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)

            # stage
            cv2.putText(image, 'STAGE', (90,12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
            cv2.putText(image, stage,
                    (90,60),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)


            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2),

                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                                 )


            cv2.imshow("MediaPipe Image Curl Project", image)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        session.pop('loggedin', None)
        session.pop('id', None)
        session.pop('email', None)        
        cap.release()
        cv2.destroyAllWindows()  
    return render_template('virtual.html')    
@app.route('/e1')
def e1():
    return response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/e2')
def e2():
    return response(generate_frame1(), mimetype='multipart/x-mixed-replace; boundary=frame')
 
@app.route('/e3')
def e3():
    return response(generate_frame2(), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/e4')
def e4():
    return response(generate_frame3(), mimetype='multipart/x-mixed-replace; boundary=frame')


def generate_frames():
    
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose

    cap = cv2.VideoCapture(0)
    counter = 0
    stage = None
    #cap = cv2.VideoCapture(0)
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            results = pose.process(image)

            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

#-------------------------------------------------------------------------------
# Chest-press Counter

            try:
                landmarks = results.pose_landmarks.landmark
                

                shoulder = [ landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                elbow = [ landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                wrist = [ landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]


                angle = calculate_angle(shoulder, elbow, wrist)

            # visualize angle
                cv2.putText(image, str(angle),
                           tuple(np.multiply(elbow, [640, 480]).astype(int)),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                                 )

                if angle > 160:
                    stage = "down"
                if angle < 30 and stage == 'down':
                    stage = "up"
                    counter += 1
                    print(counter)

            except:
                pass

#-------------------------------------------------------------------------------
# Show

            cv2.rectangle(image, (0,0), (255,83), (245,117,16), -1)

            # Curls Data
            cv2.putText(image, 'Curls', (20,12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
            cv2.putText(image, str(counter),
                    (10,60),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)

            # stage
            cv2.putText(image, 'STAGE', (90,12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
            cv2.putText(image, stage,
                    (90,60),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)


            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2),

                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                                 )


            cv2.imshow("MediaPipe Image Curl Project", image)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        session.pop('loggedin', None)
        session.pop('id', None)
        session.pop('email', None)        
        cap.release()
        cv2.destroyAllWindows()
        
    
    return render_template('virtual.html') 
    #return render_template('virtual.html')
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
	app.run()#debug=True)