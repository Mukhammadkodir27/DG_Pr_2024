from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

# def create_app():
#     app = Flask(__name__)
#     project_dir = os.path.dirname(os.path.abspath(__file__))
#     database_file = "sqlite:///{}".format(os.path.join(project_dir, "mydatabase.db"))
#     app.config["SQLALCHEMY_DATABASE_URI"] = database_file
#     db.init_app(app)
#     return app

# db = SQLAlchemy()
# app = create_app() 

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "mydatabase.db"))


app = Flask(__name__)   
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50), nullable=False)
    expensename = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50), nullable=False)


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
   expense = Expense(date=date, expensename=expensename, amount=amount, category=category)
   db.session.add(expense)
   db.session.commit()
   return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
    
