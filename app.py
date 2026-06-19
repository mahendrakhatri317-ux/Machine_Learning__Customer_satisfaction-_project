from flask import Flask, render_template, request
import joblib

model = joblib.load(r"C:\Users\Jaishree\OneDrive\Desktop\Flask\proiject\Customer\customer_model.pkl")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("predict.html")

@app.route('/predict', methods=['GET','POST'])
def predict():

    prediction = None

    if request.method == "POST":

        Gender = int(request.form['Gender'])
        Customer_Type = int(request.form['Customer_Type'])
        Type_of_Travel = int(request.form['Type_of_Travel'])
        Class = int(request.form['Class'])
        Age = int(request.form['Age'])
        Flight_Distance = int(request.form['Flight_Distance'])
        Inflight_entertainment = int(request.form['Inflight_entertainment'])
        Baggage_handling = int(request.form['Baggage_handling'])
        Cleanliness = int(request.form['Cleanliness'])
        Departure_Delay_in_Minutes = int(request.form['Departure_Delay_in_Minutes'])
        Arrival_Delay_in_Minutes = float(request.form['Arrival_Delay_in_Minutes'])

        data = [[
            Gender,
            Customer_Type,
            Type_of_Travel,
            Class,
            Age,
            Flight_Distance,
            Inflight_entertainment,
            Baggage_handling,
            Cleanliness,
            Departure_Delay_in_Minutes,
            Arrival_Delay_in_Minutes
        ]]

        pred = model.predict(data)[0]

        if pred == 1:
            prediction = "Satisfied"
        else:
            prediction = "Neutral or Dissatisfied"

    return render_template(
        "predict.html",
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)