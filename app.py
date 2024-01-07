from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

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

@app.route("/expenses")
def expenses():
    expenses = Expense.query.all()
    return render_template("expenses.html", expenses=expenses)

@app.route("/addexpense", methods=["POST"])
def addexpense():
    date = request.form["date"]
    expensename = request.form["expensename"]
    amount = request.form["amount"]
    category = request.form["category"]
    print(date + "" + expensename + "" + amount + "" + category)
    expense = Expense(date=date, expensename=expensename, amount=amount, category=category)

    with app.app_context():
        db.create_all()

    db.session.add(expense)
    db.session.commit()
    return redirect("/expenses")

if __name__ == '__main__':
    app.run(debug=True)
