from flask import Flask, request, jsonify

app = Flask(__name__)

# Global variable to store status
current_status = "pending"

@app.route('/approved', methods=['GET', 'POST'])
def approved():
    global current_status
    
    if request.method == 'POST':
        data = request.get_json()
        if data and 'status' in data:
            if data['status'] in ['pending', 'approved']:
                current_status = data['status']
                return jsonify({"status": current_status})
            return jsonify({"error": "Invalid status value"}), 400
        return jsonify({"error": "Invalid request payload"}), 400
    
    return jsonify({"status": current_status})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)