#!/usr/bin/env python
# coding: utf-8

# In[11]:


from flask import Flask, render_template, request
import joblib
import numpy as np
app = Flask(__name__)
model = joblib.load('iris_model.pkl')
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict', methods=['POST'])
def predict
    try:
           features = [float(request.form[f'feature{i}']) for i in range(1, 5)]
    except ValueError:
        return render_tempalte('result.html', prediction="Invalid input. Please enter numeric values.")
    prediction = model.predict([features])[0]
    class_names = ['Setosa', 'Verstcolor', 'Virginica']
    result = class_names[prediction]
    return render_template('result.html', prediction=result)
if__name__=='main':
    app.run(debug=True)


# In[ ]:




