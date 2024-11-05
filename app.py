from flask import Flask ,jsonify,request,abort;
from flask_cors import CORS
import jwt
from datetime import datetime ,timedelta

app =Flask(__name__);
CORS(app)
app.config["SECRET"]="super secret"

SECRET ='my Secret'

@app.route("/create",methods=["GET"])
def create():
    identity={
        "email":request.get_json().get("email"),
        "password":request.get_json().get("password"),
        "iat":datetime.utcnow(),
        "exp":datetime.utcnow()+timedelta(minutes=1),
        "fresh":True
    }
    access_token=jwt.encode(identity,SECRET,algoritm="HS256")
    return jsonify({
        "create":access_token
    })

@app.route("/token",methods=["POST"])
def token():
    payload ={
        "sub":request.get_json().get("email")
    }

    token=jwt.encode(payload,app.config["SECRET"],algorithm="HS256")
    return jsonify({
        "token":token
    })

if __name__=="__main__":
    app.run(debug=True)