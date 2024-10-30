from flask import Flask,redirect,url_for,render_template
app=Flask(__name__)
@app.route("/<name>")
def value(name):
    return render_template("main.html",content=name,r=['tt','gg'])
if __name__=='__main__':
    app.run()