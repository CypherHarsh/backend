from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user database (for example purposes)
user_data = {
    "rdxedx818@gmail.com": {"authenticated": True},
    "gauri1574.be22@chitkara.edu.in": {"authenticated": false},
    "user2@example.com": {"authenticated": True},
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
