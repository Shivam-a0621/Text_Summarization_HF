
from flask import Flask, render_template,url_for
import requests
from flask import request as rqst


app=Flask(__name__)
@app.route("/",methods=["GET", "POST"])

def index():

    return render_template('index.html')

@app.route("/Summarize",methods=["GET", "POST"])
def Summarize():
    if rqst.method =="POST":
       

        API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
        headers = {"Authorization": "Bearer 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"}
        
        data = rqst.form.get("data")
        minL=20
        maxL=int(rqst.form.get("maxL"))

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
            
        output = query({
            "inputs": data,
            "paramaters":{"min_length":minL,"max_length":maxL}
        })[0]
        return render_template("index.html",results=output["summary_text"])    
    else:
        return render_template("index.html")
    
    
        
        


    
if __name__ == "__main__":
    
    app.run(debug=True)    