from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)
@app.route("/", methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("getpost.html")
    else:
        user=request.form["name"]
        return redirect(url_for("user",usr=user))

@app.route("/<usr>")
def user(usr):
    return f'<h1>{usr}</h1>'

if __name__=='__main__':
    app.run(debug=True)