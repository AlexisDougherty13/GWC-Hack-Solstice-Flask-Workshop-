from flask import Flask, render_template, request
from jinja2 import escape, Markup

app=Flask(__name__)

@app.route('/')  
def upload():  
    return render_template("beamup.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        file = request.files['file']  
        file.save(file.filename)  
        return render_template("success.html", name=file.filename)  
    
if __name__ =='__main__':
	app.run(debug=True)
