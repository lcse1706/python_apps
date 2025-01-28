from flask import Flask,  render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return "Contact me at: 0788652134"

@app.route('/about')
def about():
    return "I am a software engineer."

@app.route('/portfolio')
def portfolio():
    return "Check out my portfolio at: www.myportfolio.com"

@app.route('/blog')
def blog():
    return "This is my blog."

@app.route('/<name>')
def name(name):
    return f"Hello, my name is {name}."

@app.route('/index')
def index():
    return "<h1>Welcome to the index page.</h1>"



  
if __name__ == "__main__":
    app.run(debug=True)
    