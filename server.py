from flask import Flask
app = Flask(__name__)

@app.route("/",methods=["GET"])
def root():
    return '<h1 style="color:pink">Welcome to my app...!!</h1>'
app.run(host="0.0.0.0", port=4400)    
