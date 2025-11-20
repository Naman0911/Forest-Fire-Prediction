import pickle 
from flask import Flask, request , jsonify , render_template
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

WebApp = Flask(__name__)
# Used to create an flask application named by Webapp
app = WebApp
# Ṇow the app refers to the flaks application


# import ridge and stadardscaler model
ridge_model = pickle.load(open(r"C:\Users\Admin\OneDrive\Desktop\Data Science\Python\Deployment\Deploy1\models\Ridge_Regression_Forest_Fire.pkl",'rb'))
Standard_Scaler = pickle.load(open(r"C:\Users\Admin\OneDrive\Desktop\Data Science\Python\Deployment\Deploy1\models\Standard_Scaler_Forest_Fire.pkl",'rb'))



# Whenever we write / in the search bar it will triger this function
@app.route("/")
def index():
    return render_template("index.html")
# here the render_template function will go check in the floder of templates is there any index.html file is there or not and then if will execute that file



'''
--------------- GET ------------------- 
When you want to see or fetch or retrive data from the URL
You are only requesting information.

Examples:
View a webpage
Search something
Read data
Get product details

You are not sending private data. 
 
 
 
--------------- POST --------------------
POST
When you want to send or submit the data in request body
You are giving information to the server.

Examples:
Login form
Signup form
Upload file
Submit feedback
Add new data to database

Used for actions that send data and may change something.
 
'''

# GET  --> Basically URL pe jo search kiya waha se kiya get kyuki waha se khula hai ek server or the default page like when we go and search for the google in the URL section , then the home page of the google will appear, this is GET method
# POST --> Basically Ab Google's Homepage is Opened and then we typed somthing in the google search bar then a new page will appear according to the given inforamtion in which we sended the data , this is called as POST method

# Example :- 
# Viewing The Menu --> GET Method
# Ordering Something or Paying Bill --> POST method

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method == "POST":
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))
        scaled_data = Standard_Scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result = ridge_model.predict(scaled_data)
        return render_template('home.html',results = result[0])
    
    else:
        return render_template('home.html')



if __name__ == "__main__":
    app.run(host="0.0.0.0")
    # When we use this host = 0.0.0.0 then it automatically maps to the local ip of the device and it will not be publicaly available
    # The bydefault port value is 5000 we can change it using port parameter of the .run()