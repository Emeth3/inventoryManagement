from flask import Flask, redirect, render_template

from src.model.item import Item

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/home")

@app.route('/home')
def home():
    item1 = Item("Aaa")
    item2 = Item("Bbb")
    item3 = Item("Ccc")
    item4 = Item("Ddd")
    items = [item1, item2, item3, item4]

    return render_template("index.html", items=items)
