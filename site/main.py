# created by Vincent Munyalo

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/articles')
def articles():
    return render_template('articles.html')

@app.route('/about_us')
def about_us():
    return render_template('aboutus.html')

@app.route('/contact_us')
def contact_us():
    return render_template('contactus.html')

@app.route('/feedback')
def report():
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(debug=True)