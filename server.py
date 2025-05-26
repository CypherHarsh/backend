from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user database (for example purposes)
user_data = {
  "durgesh1551.be22@chitkara.edu.in": {"authenticated": False},
  #   # "uday2474.be22@chitkara.edu.in": {"authenticated": False},
  #  "gaurav1572.be22@chitkara.edu.in": {"authenticated": False},
  # "kartik1751.be22@chitkara.edu.in": {"authenticated": False},
   "hardik1607.be22@chitkara.edu.in": {"authenticated": False},
  "ritika2168.be22@chitkara.edu.in": {"authenticated": False},
  #  "nikhil0587.becse24@chitkara.edu.in": {"authenticated": False},
 # "2": {"authenticated": False},
    "nikhil0587.becse24@chitkara.edu.in": {"authenticated": False},
  "1": {"authenticated": False},
  "paras637.be22@chitkara.edu.in": {"authenticated": False},
  "naman594.be22@chitkara.edu.in": {"authenticated": False},
    
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
