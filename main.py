from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('final_model', 'rb')) 

@app.route("/")
# @app.route("/home")
def home_page():
    return  render_template("index.html")


@app.route("/about")
def about_page():
    return  render_template("about.html")


@app.route("/service") 
def service_page():
    return  render_template("service.html")

@app.route("/contact")
def contact_page():
    return  render_template("contact.html") 


@app.route("/result", methods =['POST'])  
def result_page(): 
    if request.method == 'POST':
        Pregnancies = float(request.form['pregnancies'])
        Glucose = float(request.form['glucose'])
        BP = float(request.form['blood_pressure'])
        S_Thickness = float(request.form['skin_thickness'])
        Insulin = float(request.form['insulin'])
        BMI = float(request.form['bmi'])
        Diabetes_PF = float(request.form['diabetes_pf'])
        Age = float(request.form['age'])  

        prediction = model.predict([[Pregnancies,Glucose,BP,S_Thickness,Insulin,BMI,Diabetes_PF,Age]])
        
        if prediction == 0:
            return render_template('result.html', prediction_text="Congrats! You don't have diabetes")
        else:
            return render_template('result.html', prediction_text="Oops! You have diabetes") 
    else:
        return render_template('service.html')     



if __name__=="__main__":
    app.run()
    