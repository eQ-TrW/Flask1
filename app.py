from flask import Flask
from datetime import datetime
from flask import render_template
import math
from flask import Flask, flash, redirect, render_template, request, session, abort
from werkzeug.debug import console

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    # Variables
    # Calculator
    result = 0
    if request.method == 'Post':
        firstnum = int(request.form["calc-a"])
        secondnum = int(request.form["calc-b"])

        if request.form["submit"] == "Equals":
            result = firstnum + secondnum

    return render_template('Page.html', Result=result)


if __name__ == '__main__':
    app.run()
