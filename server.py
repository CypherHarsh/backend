from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user database (for example purposes)
user_data = {
"4812": {"authenticated": False},
"1415": {"authenticated": False},
"1513": {"authenticated": False},
"5153": {"authenticated": False},
"9513": {"authenticated": False},
"1463": {"authenticated": False},
"9241": {"authenticated": False},
"8623": {"authenticated": False},
"3466": {"authenticated": False},
"1111": {"authenticated": False},
"25253": {"authenticated": False},
"14145": {"authenticated": False},
 "15355": {"authenticated": False},
"12626": {"authenticated": False},
    
    }

@app.route('/authenticate', methods=['POST'])
def authenticate():
    app.logger.debug("Received POST request at /authenticate")
    data = request.json
    email = data.get('email')

    if email not in user_data:
        return jsonify({"success": False, "message": "Email not found"}), 404

    user = user_data[email]
    if user["authenticated"]:
        return jsonify({"success": False, "message": "Already authenticated"}), 403

    user["authenticated"] = True
    return jsonify({"success": True, "message": "Authentication successful"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)







