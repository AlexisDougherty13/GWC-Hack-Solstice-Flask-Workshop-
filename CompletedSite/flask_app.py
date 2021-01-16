from flask import Flask, render_template, request
from jinja2 import escape, Markup


app=Flask(__name__)


@app.route('/')
def start():
    return render_template("login.html")
    
    
@app.route('/home')
def home():
    return render_template("login.html")
    
    
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    file = open("accounts.txt", "r")
    accounts = file.readlines()
    file.close()
    for account in accounts:
        if(username == account[:account.find("|")] and password == account[account.find("|")+1:].strip("\n")):
            images = []
            file2 = open("images.txt", "r")
            temp = file2.readlines()
            file2.close()
            index = len(temp)-1
            while index >= 0:
                images.append(temp[index]) 
                index = index - 1
            return render_template('posts.html', username=username, images=images)
    message = 'incorrect username or password'
    return render_template('login.html', message=message)
    
 
@app.route('/uploaded', methods = ['POST'])  
def uploaded():  
    if request.method == 'POST': 
        username = request.form['username']
        f = request.files['file']  
        f.save("./static/" + f.filename) 
        file = open("images.txt", "a")
        file.write("../static/" + f.filename + "\n")
        file.close()
        images = []
        file2 = open("images.txt", "r")
        temp = file2.readlines()
        file2.close()
        index = len(temp)-1
        while index >= 0:
            images.append(temp[index]) 
            index = index - 1
        return render_template("posts.html", username=username, images=images) 
        
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    
    
if __name__ =='__main__':
	app.run(debug=True)
    
    