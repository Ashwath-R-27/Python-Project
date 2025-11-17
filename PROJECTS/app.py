from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('adminlogin.html')

@app.route('/verify', methods=['POST'])
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
if __name__ == '__main__':
    app.run(debug=True)