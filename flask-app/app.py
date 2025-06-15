from flask import Flask, render_template, request
from preprocessing_utility import normalize_text
import mlflow
import dagshub
import pickle

mlflow.set_tracking_uri("https://dagshub.com/imakash665/mlops-mini-project.mlflow")
dagshub.init(repo_owner='imakash665', repo_name='mlops-mini-project', mlflow=True)

#load model from registry
model_name = "my_model"
model_version = 5

model_uri = f'models:/{model_name}/{model_version}'
model = mlflow.pyfunc.load_model(model_uri)


vectorizer = pickle.load(open('models/vectorizer.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",result = None)
@app.route('/predict', methods = ['POST'])
def predict():
    text = request.form['text']

    text = normalize_text(text)

    features = vectorizer.transform([text])

    result = model.predict(features)

    return render_template('index.html',result = result[0])

    return text

app.run(debug=True)