from flask import Flask, render_template,request
from urllib.request import urlopen
from bs4 import BeautifulSoup
#import pandas as pd
app = Flask(__name__)

# two decorators, same function
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    bad=0
    if request.method == "POST":
        url = request.form.get("fname")
        html = urlopen(url).read()
        soup = BeautifulSoup(html, features="html.parser")

        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()  # rip it out

        # get text
        text = soup.get_text()

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)

        ls = text.split("\n")
        

        courses = {
            "Perform Foundational Infrastructure Tasks in Google Cloud": 0,
            "Essential Google Cloud Infrastructure: Core Services": 0,
            "Getting Started with Google Kubernetes Engine": 0,
            "Set Up and Configure a Cloud Environment in Google Cloud": 0,
            "Create and Manage Cloud Resources": 0,
            "Essential Google Cloud Infrastructure: Foundation": 0,
            "Google Cloud Fundamentals: Core Infrastructure": 0
        }

        st = "Earn a skill badge by completing the Perform Foundational Infrastructure Tasks in Google Cloud quest, where you learn how to build and connect storage-centric cloud infrastructure using the basic capabilities of the of the following technologies: Cloud Storage, Identity and Access Management, Cloud Functions, and Pub/Sub."
        bad=0
        for i in range(len(ls)):
            try:
                if ls[i]==st:
                    break
                if ((not courses[ls[i]]) and (('Dec' in ls[i+1]) or ('Nov' in ls[i+1]))):
                    bad+=1
                    courses[ls[i]]+=1
            except:
                bad+=0
        

        
    return render_template("base.html",r="No of Badges"+str(bad))

if __name__ == '__main__':
    app.run(debug=True)
