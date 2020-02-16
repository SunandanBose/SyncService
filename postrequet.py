from flask import Flask, jsonify, request

app = Flask(__name__)

accounts = [
    {'name':'Raj', 'balance': 100},
    {'name':'Sunandan', 'balance': 10000},
]

@app.route("/accounts", methods=["GET"])
def getaccounts():
    return jsonify(accounts)

@app.route("/account/<id>", methods=["GET"])
def getaccountsById(id):
    id = int(id) -1
    return jsonify(accounts[id])

@app.route("/account", methods=["POST"])
def addAccount():
    name = request.json['name']
    balance = request.json['balance']
    data = {'name' : name, 'balance': balance}
    accounts.append(data)
    return jsonify(accounts)

if(__name__ == '__main__'):
    app.run(port=8081)