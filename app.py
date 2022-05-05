# from flask import Flask
from flask import Flask,render_template
# app = Flask(__name__)
app = Flask(__name__, static_url_path='/')

@app.route('/')
def home():
     return render_template("login.html")


@app.route('/login')
def login():
    return render_template("login.html")
    
@app.route('/signup')
def signup():
    return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)



# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#   return 'Hello World!'
# if __name__ == '__main__':
#   app.run(host='0.0.0.0')