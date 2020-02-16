from flask import Flask, jsonify

app = Flask(__name__)

accounts = [
    {'name':'Raj', 'balance': 100},
    {'name':'Sunandan', 'balance': 10000},
]

@app.route("/accounts", methods=["GET"])
def getaccounts():
    return jsonify(accounts)

@app.route("/accounts/<id>", methods=["GET"])
def getaccountsById(id):
    id = int(id) -1
    return jsonify(accounts[id])

if(__name__ == '__main__'):
    app.run(port=8081)