from flask import Flask,redirect,url_for
app=Flask(__name__)
@app.route("/")
def home():
    return "flask <h1>jj<h1>"
@app.route("/<name>")
def value(name):
    return name
@app.route("/first")
def redirct():
    return redirect(url_for("home"))
    
if __name__=='__main__':
    app.run()