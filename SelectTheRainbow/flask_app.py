from flask import Flask, render_template, request
from jinja2 import escape, Markup

app=Flask(__name__)

@app.route('/')
def start():
    color = "white"
    return render_template("rainbow.html", color=color)
    
@app.route('/changeBackground', methods=['GET'])
def changeBackground():
    color = request.args.get('color')
    return render_template("rainbow.html", color=color)
    
if __name__ =='__main__':
	app.run(debug=True)
