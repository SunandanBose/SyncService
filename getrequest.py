from flask import Flask, jsonify

app = Flask(__name__)

accounts = [
    {'name':'Raj', 'balance': 100},
    {'name':'Sunandan', 'balance': 10000},
]

@app.route("/accounts", methods=["GET"])
def getaccounts():
    return jsonify(accounts)

if(__name__ == '__main__'):
    app.run(port=8081)