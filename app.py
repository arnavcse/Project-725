# app.py
import os
import pickle
import joblib
import numpy as np 

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def enter():
    return render_template("enter.html")

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        try:
            # Extract form data
            gender = int(request.form['gender'])
            # Extract other form fields...

            # Validate and process form data as needed

            # Replace the following line with your logic to determine stroke or no stroke
            result_data = "Your result data goes here"

            return render_template('result.html', result_data=result_data)

        except KeyError as e:
            error_message = f"KeyError: {str(e)} is missing in form data."
            return render_template('error.html', error_message=error_message)
        except ValueError as ve:
            error_message = f"ValueError: {str(ve)}"
            return render_template('error.html', error_message=error_message)

    # If it's a GET request, render the form template
    return render_template('form.html')

@app.route('/result', methods=['POST'])

def result():

    try:
        gender = int(request.form['gender'])
        age = int(request.form['age'])
        hypertension = int(request.form['hypertension'])
        heart_disease = int(request.form['heart_disease'])
        ever_married = int(request.form['ever_married'])
        work_type = int(request.form['work_type'])
        residence_type = int(request.form['Residence_type'])
        avg_glucose_level = float(request.form['avg_glucose_level'])
        bmi = float(request.form['bmi'])
        smoking_status = int(request.form['smoking_status'])

        # Validate input values (add more validation if needed)
        if age < 0 or avg_glucose_level < 0 or bmi < 0:
            raise ValueError("Invalid input values")

        x = np.array([gender, age, hypertension, heart_disease, ever_married, work_type, residence_type,
                      avg_glucose_level, bmi, smoking_status]).reshape(1, -1)

        # Load scaler
        scaler_path_mac = '/Users/arnav/Desktop/FML Project/Code/models/scaler.pkl'
        scaler = None
        try:
            with open(scaler_path_mac, 'rb') as scaler_file:
                scaler = pickle.load(scaler_file)
        except Exception as e:
            return render_template('error.html', error_message=f"Error loading scaler: {str(e)}")

        # Transform input features using the loaded scaler
        x = scaler.transform(x)

        # Load the model
        model_path = os.path.join('/Users/arnav/Desktop/FML Project/Code/models/random_forest_model.pkl')
        dt = None
        try:
            dt = joblib.load(model_path)
        except Exception as e:
            return render_template('error.html', error_message=f"Error loading model: {str(e)}")

        # Make predictions
        y_pred = int(round(dt.predict(x)[0]))

        # Render templates based on predictions
        if y_pred == 0:
            return render_template('nostroke.html')
        else:
            return render_template('stroke.html')

    except KeyError as e:
        # Handle missing keys in form data
        error_message = f"KeyError: {str(e)} is missing in form data."
        return render_template('error.html', error_message=error_message)
    except ValueError as ve:
        # Handle invalid input values
        error_message = f"ValueError: {str(ve)}"
        return render_template('error.html', error_message=error_message)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/legal')
def legal():
    return render_template('dis.html')

@app.route('/privacy_policy')
def privacy_policy():
    return render_template('privacy_policy.html')

@app.route('/terms_of_use')
def terms_of_use():
    return render_template('termsofuse.html')

@app.route('/sales_policy')
def sales_policy():
    return render_template('salespolicy.html')



@app.route('/buzzbeat')
def buzzbeat():
    return render_template('buzzbeat.html')

if __name__ == "__main__":
    app.run(debug=True, port=7384)
