
from flask import Flask, render_template, request, jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://rupa:rupa@cluster0.jjvlc0m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db=client.dbusers
app = Flask(__name__)
@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def save_order():
        name_receive = request.form['name_give']
        count_receive = request.form['count_give']
        address_receive = request.form['address_give']
        phone_receive = request.form['phone_give']
        doc = {
            'name': name_receive,
            'count': count_receive,
            'address': address_receive,
            'phone': phone_receive
        }

        db.orders.insert_one(doc)
        return jsonify({"msg":"complete!"})

@app.route('/order', methods=['GET'])
def view_orders():
    orders_list = list(db.orders.find({}, {'_id': False}))
    return jsonify({'orders': orders_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
