# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import sparse


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/index', methods=['GET', 'POST'])
def handleForm():
    if request.method == 'GET':
        return render_template("indexhtml")
    else:
        props = {
            'name': request.form['name'],
            'birthday': sparse(request.form['birthday'])


        }
        return render_template("results.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
