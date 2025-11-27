from flask import Flask, request, render_template, jsonify
import csv

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

@app.route('/home/menu')
def menu():
    soup=[]
    starters=[]
    biryani=[]
    gravy=[]
    rice_noodles=[]
    drinks=[]
    desserts=[]
    filename = "menu.csv"
    with open(filename, "r", newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)  # To skip the header row
        for row in reader:
            if row[4]=='Starters':
                starters.append(row)
            elif row[4]=='Biryani':
                biryani.append(row)
            elif row[4]=='Gravy':
                gravy.append(row)
            elif row[4]=='Rice/Noodles':
                rice_noodles.append(row)
            elif row[4]=='Soup':
                soup.append(row)
            elif row[4]=='Drinks':
                drinks.append(row)
            elif row[4]=='Desserts':
                desserts.append(row)
    return render_template('menu.html',soup=soup,starters=starters,biryani=biryani,gravy=gravy,rice_noodles=rice_noodles,drinks=drinks,desserts=desserts)

@app.route('/home/accounts')
def accounts():
    return render_template('accounts.html')

if __name__ == '__main__':
    app.run(debug=True)