
from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about/")
def about():
    return render_template('about.html')

@app.route("/work/")
def work():
    return render_template('work.html')

@app.route("/contact/")
def contact():
    return render_template('contact.html')

@app.route("/privacy/")
def privacy():
    return render_template('privacy.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=0)