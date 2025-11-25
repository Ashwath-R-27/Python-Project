from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('adminlogin.html')

@app.route('/dashboard', methods=['POST'])
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

records=[[101,'Veg Biriyani',10,100],
         [102,'Chilly chicken',12,165],
         [103,'Idly',25,30],
         [104,'Dosa',30,25],
         [105,'Chappathi',25,15]]
expense=[]
for i in records:
    i.append(i[2]*i[3])
    expense.append(i)

@app.route('/dashboard/accounts')
def accounts():
    return render_template('accounts.html',records=expense)

if __name__ == '__main__':
    app.run(debug=True)