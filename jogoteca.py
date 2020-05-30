from flask import Flask, render_template

app = Flask(__name__) #__name__ it's the package name

@app.route("/inicio") #defining a route for the function
def ola():
    return render_template("lista.html")

app.run()
