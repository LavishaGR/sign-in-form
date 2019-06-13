from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("base.html")

@app.route('/signin/', method=['POST'])
def collect_data():
    name= request.form['name']
    username= request.form['username']
    password= request.form['password']
    createUser(name,username,password)

if __name__ == '__main__':
    app.run(debug=True)