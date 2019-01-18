
from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('pages/index.html')

@app.route("/about-us/")
def about():
    return render_template('pages/about.html')

@app.route("/our-product/")
def work():
    return render_template('pages/product.html')

@app.route("/contact-us/")
def contact():
    return render_template('pages/contact.html')

# routes for Product fence folder
@app.route("/vinyl-fencing/")
def vinyl():
    return render_template('fence/vinyl-fencing.html')
@app.route("/aluminum-fencing/")
def aluminum():
    return render_template('fence/aluminum.html')

@app.route("/farm-fencing/")
def farm():
    return render_template('fence/farm-fence.html')

@app.route("/residential-fencing/")
def residential():
    return render_template('fence/residential.html')
# city Routes Folder
@app.route("/kings-mountain-fencing/")
def kings():
    return render_template('city/kings-mountain.html')

@app.route("/mount-holly-fencing/")
def mountholly():
    return render_template('city/mount-holly.html')

@app.route("/belmont-fencing/")
def belmont():
    return render_template('city/belmont.html')

@app.route("/charlotte-fencing/")
def charlotte():
    return render_template('city/charlotte.html')

@app.route("/gastonia-fencing/")
def gastonia():
    return render_template('city/gastonia.html')
# Legal
@app.route("/privacy/")
def privacy():
    return render_template('pages/privacy.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('pages/404.html')

if __name__ == '__main__':
    app.run(debug=0)