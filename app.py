from flask import Flask,render_template,request
from deployment import recommendation_knn

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend',methods=['POST'])

def predict():
    try:
        if request.method == 'POST':
            message = request.form['message']
            data = message
            my_recommend, links = recommendation_knn(data)
            return render_template('recommend.html',recommendation = my_recommend,book = data, links = links)

    except Exception as e:
        return render_template('error.html',book = data)

if __name__=='__main__':
    app.run(debug=True)
