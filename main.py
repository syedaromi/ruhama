from flask import Flask, request, render_template
from a import text_to_speech


# Flask constructor
app = Flask(__name__)  
 
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    print('reached')
    if request.method == "POST":
       print("Post method")
       # getting input with name = fname in HTML form
       finalText = request.form.get("speech")
       # getting input with name = lname in HTML form
       
       text_to_speech(finalText,'Male')
       #return "Your name is "+first_name + last_name
    return render_template("index.html")
 
if __name__=='__main__':
   app.run()