
from flask import Flask,render_template,request
import pickle

model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_placement():
    cgpa = float(request.form.get('cgpa'))
    iq = int(request.form.get('iq'))
    profile_score = int(request.form.get('profile_score'))


    result = model.predict([[cgpa,iq,profile_score]])

    print(result[0])
    if result[0] == 1:
        result = 'Student Placed'
    else:
        result = 'Student Not Placed'

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=8080)
