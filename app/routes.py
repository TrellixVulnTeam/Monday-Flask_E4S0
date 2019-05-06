from app import app

from flask import render_template,url_for,redirect

@app.route('/')
def hello_world():
    name = "Jon Snow"

    characters = {
        "females": ["Arya","Daenarys"],
        "males":["Jamie","Jon","Ned","Tyrion"]
    }
    return render_template("index.html",name = name, characters = characters)

@app.route('/profile/<gender>/<name>', methods = ["GET"])
def profile (name, gender):
    info = {}

    if gender == 'male':
        gender = 'Male'

    else:
        gender = "Female"
    
    if name == "Arya":
        info = {
            "profile_pic": "http://placehold.it/250x250",
            "house": "Stark",
            "home": "Winterfell",
            "weapon": "Needle"
        }
    elif name == "Jamie":
        info = {
            "profile_pic": "http://placehold.it/250x250",
            "house": "Lannister",
            "home": "Castille Rock",
            "weapon": "Sword"
        }
    return render_template("profile.html", name = name, info = info, gender = gender)