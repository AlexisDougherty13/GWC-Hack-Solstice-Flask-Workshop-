from flask import Flask, render_template, request
import random
from jinja2 import escape, Markup

app=Flask(__name__)

@app.route('/')
def start():
    names = ["Alice", "Bob", "Carla", "Dan", "Eve"]
    winner = names[random.randrange(0,len(names))]
    return render_template("winner.html", winner=winner)
    
if __name__ =='__main__':
	app.run(debug=True)
    
    
