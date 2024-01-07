from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def add():
    return render_template("add.html")

@app.route("/addexpense", methods=["POST"])
def addexpense(): 
   date = request.form["date"]
   expensename = request.form["expensename"]
   amount = request.form["amount"]
   category = request.form["category"]
   print(date+""+expensename+""+amount+""+category)
   return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
    
