from flask import Flask,render_template,request

app=Flask(__name__)


@app.route("/")
def hi():
    return render_template("index.html")


@app.route("/login",methods=["post"])
def login_data():
    user=request.form["login_txt"]
    password=request.form["password_txt"]
    if user=="omar"and password=="1234":
        return render_template("video.html")
    else:
        return render_template("404.html")















if __name__=="__main__":
    app.run(debug=True)