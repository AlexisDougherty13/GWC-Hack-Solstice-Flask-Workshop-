from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def start():
    return render_template("helloworld.html")
    
if __name__ =='__main__':
	app.run(debug=True)
    
    
