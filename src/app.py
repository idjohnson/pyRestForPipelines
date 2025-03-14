from flask import Flask, request, jsonify

app = Flask(__name__)

# Initial status
status = {"status": "pending"}

@app.route('/approved', methods=['GET', 'POST'])
def approved():
    global status
    if request.method == 'GET':
        return jsonify(status)
    elif request.method == 'POST':
        data = request.get_json()
        if data and "status" in data:
            status["status"] = data["status"]
            return jsonify(status), 200
        return jsonify({"error": "Invalid payload"}), 400

if __name__ == '__main__':
    app.run(debug=True)