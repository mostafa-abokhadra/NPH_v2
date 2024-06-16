#!/usr/bin/python3
"""starting point"""
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__, static_url_path='/static')


@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
@app.route('/NPH', strict_slashes=False)
def home():
    title = 'NPH'
    return render_template('home.html', title=title)

@app.route('/signUp', methods=["POST", "GET"])
def signUp():
    if request.method == 'POST':
        return redirect(url_for("test", request.POST))
    title = signUp
    return render_template('signUp.html', title=title)

@app.route('/test/<req>')
def test(req):
    return render_template('test.html', req=req)

if __name__ == '__main__':
    app.run(debug=True)