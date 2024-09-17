from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle

app = Flask(__name__)
model = pickle.load(open("D:\\EDA\\PlantGrowth_Predictor v1.0\\PlantGrowth_Predictor.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("WebApp.html")


@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        Soil_Type = request.form['Soil_Type']
        if Soil_Type == 'loam':
            Soil_Type = 1
        elif Soil_Type == 'sandy':
            Soil_Type = 2
        else:
            Soil_Type = 3
            
        Sunlight_Hours = float(request.form['Sunlight_Hours'])
        
        Water_Frequency = request.form['Water_Frequency']
        if Water_Frequency == 'bi-weekly':
            Water_Frequency = 1
        elif Water_Frequency == 'weekly':
            Water_Frequency = 2
        else:
            Water_Frequency = 3
            
        Fertilizer_Type = request.form['Fertilizer_Type']
        if Fertilizer_Type == 'chemical':
            Fertilizer_Type = 1
        elif Fertilizer_Type == 'organic':
            Fertilizer_Type = 2
        else:
            Fertilizer_Type = 3
            
        Temperature = float(request.form['Temperature'])
        Humidity = float(request.form['Humidity'])
        
        prediction = model.predict([[Soil_Type, Sunlight_Hours, Water_Frequency, Fertilizer_Type, Temperature, Humidity]])
        output = prediction[0]
        
        if output == 1:
            result = "The plant growth will occur."
        else:
            result = "The plant growth will not occur."

        return render_template('WebApp.html', prediction_text=result)

    return render_template("WebApp.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)