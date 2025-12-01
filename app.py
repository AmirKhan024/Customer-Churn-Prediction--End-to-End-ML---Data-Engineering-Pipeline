import pandas as pd
from flask import Flask, request, render_template
import joblib

app = Flask("__name__")

df_1 = pd.read_csv("first_telc.csv")

model = joblib.load('my_model.sav')

@app.route("/")
def loadPage():
    return render_template('home.html', query="")

@app.route("/", methods=['POST'])
def predict():
    inputQuery1 = request.form['query1']
    inputQuery2 = request.form['query2']
    inputQuery3 = request.form['query3']
    inputQuery4 = request.form['query4']
    inputQuery5 = request.form['query5']
    inputQuery6 = request.form['query6']
    inputQuery7 = request.form['query7']
    inputQuery8 = request.form['query8']
    inputQuery9 = request.form['query9']
    inputQuery10 = request.form['query10']
    inputQuery11 = request.form['query11']
    inputQuery12 = request.form['query12']
    inputQuery13 = request.form['query13']
    inputQuery14 = request.form['query14']
    inputQuery15 = request.form['query15']
    inputQuery16 = request.form['query16']
    inputQuery17 = request.form['query17']
    inputQuery18 = request.form['query18']
    inputQuery19 = request.form['query19']
    
  
    data = [[inputQuery1, inputQuery2, inputQuery3, inputQuery4, inputQuery5, inputQuery6, inputQuery7,
             inputQuery8, inputQuery9, inputQuery10, inputQuery11, inputQuery12, inputQuery13, inputQuery14,
             inputQuery15, inputQuery16, inputQuery17, inputQuery18, inputQuery19]]
    
    new_df = pd.DataFrame(data, columns = ['SeniorCitizen', 'MonthlyCharges', 'TotalCharges', 'gender', 
                                           'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService',
                                           'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
                                           'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
                                           'PaymentMethod', 'tenure'])

    labels = ["{0} - {1}".format(i, i + 11) for i in range(1, 72, 12)]
    new_df['tenure_group'] = pd.cut(new_df['tenure'].astype(int), range(1, 80, 12), right=False, labels=labels)

    new_df.drop(columns=['tenure'], axis=1, inplace=True)

    new_df_dummies = pd.get_dummies(new_df[['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService',
                                             'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
                                             'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
                                             'Contract', 'PaperlessBilling', 'PaymentMethod', 'tenure_group']])


    new_df_dummies = new_df_dummies.reindex(columns=model.feature_names_in_, fill_value=0)

    prediction = model.predict(new_df_dummies)
    probablity = model.predict_proba(new_df_dummies)[:, 1]

    if prediction == 1:
        result = "This customer is likely to churn!!"
        confidence = f"Confidence: {probablity[0]*100:.2f}%"
    else:
        result = "This customer is likely to continue!!"
        confidence = f"Confidence: {probablity[0]*100:.2f}%"
    
    return render_template('home.html', output1=result, output2=confidence,
                           query1=inputQuery1, query2=inputQuery2, query3=inputQuery3, query4=inputQuery4,
                           query5=inputQuery5, query6=inputQuery6, query7=inputQuery7, query8=inputQuery8,
                           query9=inputQuery9, query10=inputQuery10, query11=inputQuery11, query12=inputQuery12,
                           query13=inputQuery13, query14=inputQuery14, query15=inputQuery15, query16=inputQuery16,
                           query17=inputQuery17, query18=inputQuery18, query19=inputQuery19)

if __name__ == '__main__':
    app.run(debug=True)

