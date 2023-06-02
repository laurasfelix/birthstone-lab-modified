# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import sparse
from model import holy


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/index', methods=['GET', 'POST'])
def handleForm():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        bithday = request.form['birthday']
        image, borthy = sparse(bithday)
        country_name = request.form['country']
        props = {
            'name': request.form['name'],
            'birthday': borthy,
            'image': image +".png",
            'country': holy(country_name, bithday)
        }
        return render_template("results.html", props=props)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
