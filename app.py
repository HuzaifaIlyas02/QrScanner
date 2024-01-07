from flask import Flask, render_template, request
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import os
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan_qr():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    
    if file:
        filename = os.path.join('uploads', file.filename)
        file.save(filename)

        # Now we scan the saved image
        img = cv2.imread(filename)
        decoded_objects = decode(img)
        for obj in decoded_objects:
            # Check in the database if the QR code is authorized
            qr_data = obj.data.decode('utf-8')
            if is_authorized(qr_data):
                return "Authorized Access"
            else:
                return "Un-Authorized Access"

def is_authorized(qr_data):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM authorized_users WHERE qr_data=?", (qr_data,))
    result = c.fetchone()
    conn.close()
    return result is not None

if __name__ == '__main__':
    app.run(debug=True)
