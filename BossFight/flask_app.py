#This is part of the Boss Fight Hands On Assignment
#Parts of this project are complete. 
#There are notes ("FILLIN") through this file where something is missing. 
#Add in the missing bits to complete the website. Good luck!

from flask import Flask, render_template, request
from jinja2 import escape, Markup

#FILLIN Create an instance of the Flask class


#FILLIN default app.route
def start():
    return render_template("login.html")
    
    
#FILLIN app.route that redirectes to the login page (used on the 404 page to redirect the user to a better place)
def home():
    return render_template("login.html")
    
    
#FILLIN app.route for the login form
def login():
    username = "FILLIN the username from the form"
    password = "FILLIN the password from the form"
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
    return 0 #FILLIN the login HTML page and the message variable
    
 

#FILLIN app.route for the upload form 
def uploaded():  
    if request.method == 'POST': 
        username = "FILLIN the username from the form"
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
        return 0 #FILLIN the posts HTML page, username variable, and the images array

       
#FILLIN 404 Error Function     
    
if __name__ =='__main__':
	app.run(debug=True)
    
    
