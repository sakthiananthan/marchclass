from flask import Flask, render_template,request,redirect
from fun import *

app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def homepage():
    if request.method=="POST":
        register_stud(request.form["name"],request.form["age"],request.form["course"],request.form["address"])
    data=read_json()
    return render_template("homepage.html",stud_data=data["students"])

@app.route("/delete/<sno>")
def delete_stud(sno):
    print(type(sno))
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")