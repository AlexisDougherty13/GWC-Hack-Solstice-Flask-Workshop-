from flask import Flask, render_template, request
from jinja2 import escape, Markup

app=Flask(__name__)

@app.route('/')
def start():
    return render_template("question.html")
    
@app.route('/question', methods=['POST'])
def question():
    message = "Incorrect. You shall not pass."
    ans = request.form['answer']
    if(int(ans) == 150):
        message = "Correct. You may pass."
    return render_template("question.html", message=message)
    
if __name__ =='__main__':
	app.run(debug=True)
    
    
