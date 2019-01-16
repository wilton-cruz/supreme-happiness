
from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about-us/")
def about():
    return render_template('about.html')

@app.route("/our-product/")
def work():
    return render_template('product.html')

@app.route("/contact-us/")
def contact():
    return render_template('contact.html')

# routes for services
@app.route("/vinyl-fencing/")
def vinyl():
    return render_template('vinyl-fencing.html')
@app.route("/aluminum-fencing/")
def aluminum():
    return render_template('aluminum.html')

@app.route("/farm-fencing/")
def farm():
    return render_template('farm-fence.html')

@app.route("/residential-fencing/")
def residential():
    return render_template('residential.html')
# city Routes
@app.route("/kings-mountain-fencing/")
def kings():
    return render_template('kings-mountain.html')

@app.route("/mount-holly-fencing/")
def mountholly():
    return render_template('mount-holly.html')

@app.route("/belmont-fencing/")
def belmont():
    return render_template('belmont.html')

@app.route("/charlotte-fencing/")
def charlotte():
    return render_template('charlotte.html')

@app.route("/gastonia-fencing/")
def gastonia():
    return render_template('gastonia.html')

@app.route("/privacy/")
def privacy():
    return render_template('privacy.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=0)