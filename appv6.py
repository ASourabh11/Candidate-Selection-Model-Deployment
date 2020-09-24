from flask import Flask,request, redirect,jsonify, render_template
import sklearn
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('Candidate_SelectionV6')


@app.route('/')
def home():
    
    return render_template("New.html")

@app.route('/predict',methods=['POST'])
def predict():
    
    
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    a = 'Candidate is eligible for Interview'
    b = 'Candidate is not eligible for Interview'
    
    if prediction == 1 : 
        output = a 
    elif prediction == 0 :
        output = b 
    

    return render_template('result.html', Decision ='{}'.format(output))
    

    
    

if __name__ == '__main__':
    app.run()