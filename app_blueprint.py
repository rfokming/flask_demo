from flask import Blueprint, render_template,request

app_blueprint = Blueprint('app_blueprint',__name__)
first_name = ""

#variables
popular_products = [
    {'name':'Johan','size':'small','price':5,'img':'/img/rome.jpg'},
    {'name':'Robert','size':'med','price':6,'img':'/img/rome.jpg'},
    {'name':'David','size':'large','price':7,'img':'/img/rome.jpg'}
]

@app_blueprint.route('/')
def index():
        #return "<h1>Homepage2<h1>"
        return render_template("index.html",popular_products=popular_products)

@app_blueprint.route('/about5')
def about3():
        #return "<h1>Homepage2<h1>"
        return render_template("about.html",first_name=first_name)


@app_blueprint.route('/contact')
def contact():
        #return "<h1>Homepage2<h1>"
        return render_template("contact.html")

# A decorator used to tell the application
# which URL is associated function
@app_blueprint.route('/nameForm', methods =["GET", "POST"])
def nameForm():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       # getting input with name = lname in HTML form
       last_name = request.form.get("lname")
       #return "Your name is "+first_name + last_name
       return render_template("about.html",first_name=first_name)
    return render_template("name_form.html")