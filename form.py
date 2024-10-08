from flask import Flask, render_template, request
from pymongo import MongoClient
app = Flask(__name__)
client=MongoClient('mongodb+srv://<Suhail-kp00>:<Suhail@123>@cluster0.tuhmo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db=client['Cluster0']
collection=db['submissions']
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        collection.insert_one({'name': name, 'email': email})
        submissions=list(collection.find({},{'_id':0,'name':1,'email':1}))
    return render_template('index.html', submissions=submissions)
if __name__ == '__main__':
    app.run(debug=True)
