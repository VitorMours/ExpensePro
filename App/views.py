from flask import ( Blueprint, 
                    render_template, 
                    request, 
                    flash)



views = Blueprint('views', __name__)




@views.route("/", methods=["GET"])
def index_page():
    flash("Login feito")
    return render_template("index.html")






