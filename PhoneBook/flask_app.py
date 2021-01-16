from flask import Flask, render_template, request
import random
from jinja2 import escape, Markup

app=Flask(__name__)

class Contact:
  def __init__(self, name, phone, email):
    self.name = name
    self.phone = phone
    self.email = email

@app.route('/')
def start():
    person1 = Contact("Alexis", "123-456-7890", "alexisiscool@email.com")
    person2 = Contact("Micayla", "345-678-9012", "mickeyd@email.com")
    person3 = Contact("Colton", "567-890-1234", "coltontrent@email.com")
    person4 = Contact("Carter", "789-012-3456", "potstirer@email.com")
    person5 = Contact("Larissa", "901-234-5678", "merica@email.com")
    contacts = [person1, person2, person3, person4, person5]
    message5 = "This message will display only if there are 5 contacts"
    message4 = "This message will display only if there are 4 contacts"
    return render_template("contacts.html", contacts=contacts, message5=message5, message4=message4)
    
if __name__ =='__main__':
	app.run(debug=True)
    
    
