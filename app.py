from flask import Flask, render_template, request #flask is a web framework for Python that allows one to build web application.
import numpy as np

app = Flask(__name__) #create an instance of the web framework for python, where name = root path of the application
@app.route("/",methods=["GET","POST"]) #use flask to map to root URL endpoint denoted by "/". #GET = retrieve from server when URL is accessed, #POST = submit a form
#GET from SG to US, and POST is US to SG
def index(): #when "/" is called, generate function called index
        return(render_template("index.html")) # Flask function will look to index.html under templates for the generation

#BANKRUPTCY ASSESSMENT
#Function to run the Button at the Front End
@app.route("/bankruptcy_assessment",methods=["GET","POST"])
def bankruptcy_assessment():
        return(render_template("bankruptcy_assessment.html")) #synchronise front and back-end.

#Setting up the BANKRUPTCY ASSESSMENT RESULT Page
@app.route("/bankruptcy_assessment_result",methods=["GET","POST"])
def bankruptcy_assessment_result():
        q= float(request.form.get("q"))# wsgi is text by default, therefore to force to float, where q is the variable
        q1=float(request.form.get("q1"))
        q2=float(request.form.get("q2"))
        q3=float(request.form.get("q3"))
        q4=float(request.form.get("q4"))

        r=(-2.999810*q+2.303792*q1+1.966006*q2+1.946442*q3-1.863458*q4)-5.59682635
        r=np.where(r>=0.5,"High","Low")

        return(render_template("bankruptcy_assessment_result.html",r=r)) #synchronise front and back-end.
if __name__ == "__main__":
    app.run(debug=True, port=5000)  # You can change the port number if needed