from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user database (for example purposes)
user_data = {
"19192": {"authenticated": False},
"38329": {"authenticated": False},
"74929": {"authenticated": False},
"74244": {"authenticated": False},
#"46373": {"authenticated": False},
#"26272": {"authenticated": False},
#"74257": {"authenticated": False},
#"78257": {"authenticated": False},
#"78611": {"authenticated": False},
#"26262": {"authenticated": False},
#"26327": {"authenticated": False},
#"89184": {"authenticated": False},
# "98941": {"authenticated": False},
#"12352": {"authenticated": False},
    
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










