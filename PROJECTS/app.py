from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('stafflogin.html')

@app.route('/')
def index():
    return render_template('adminlogin.html')

@app.route('/home', methods=['POST'])
def logverify():
    un = str(request.form['un'])
    pwd = request.form['pwd']
    if un=="PSG":
        if pwd=='123':
            return render_template('home.html')
        else:
            result='password'
            return render_template('adminlogin.html',result=result)
    else:
        result='username'
        return render_template('adminlogin.html',result=result)

records=[]

import csv
filename = "menu.csv"
with open(filename, "r", newline='', encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)  # To skip the header row
    for row in reader:
        records.append(row)

@app.route('/home/menu')
def menu():
    return render_template('menu.html',records=records)

@app.route('/home/accounts')
def accounts():
    return render_template('accounts.html')

if __name__ == '__main__':
    app.run(debug=True)