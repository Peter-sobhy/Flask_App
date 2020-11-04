from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load('model.pkl')

@app.route("/")
def home():
    return render_template('index.html')



@app.route("/predict", methods=["POST"])
def predict():
    results = {}
    cement =  request.form['cement']
    furnace_slag =  request.form['furnace_slag']
    fly_ash =  request.form['fly_ash']
    water =  request.form['water']
    super_plasticizer =  request.form['super_plasticizer']
    coarse_agg =  request.form['coarse_agg']
    fine_agg = request.form['fine_agg']
    age = request.form['age']
    result = int(round(model.predict([[cement, furnace_slag, fly_ash, water, super_plasticizer, coarse_agg, fine_agg, age]])[0]))
    results['cement'] = cement
    results['furnace_slag'] = furnace_slag
    results['fly_ash'] = fly_ash
    results['water'] = water
    results['super_plasticizer'] = super_plasticizer
    results['coarse_agg'] = coarse_agg
    results['fine_agg'] = fine_agg
    results['age'] = age
    results['prediction in Mpa'] = result
    return render_template("index.html", results=results)




if __name__ == "__main__":
    app.run()
