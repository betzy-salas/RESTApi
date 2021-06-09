from flask import Flask, json, jsonify, request, make_response, Response
import Token.Aplication.GetToken as getTokenAplication
import Infraestructure.Messages as messages
from functools import wraps

app = Flask(__name__)

@app.route("/unprotected")
def unprotected():
    return jsonify({"message" : messages.MessageUser("Do I really look like a guy with a plan? You know what I am? I'm a dog chasing cars. I wouldn't know what to do with one if I caught it.  You know? I just do things. Joker The Dark Night")})

@app.route("/")
def healthy():
    return jsonify({"message" : messages.MessageUser("Remember, remember the Fifth of November, The Gunpowder Treason and Plot, I know of no reason Why the Gunpowder Treason Should ever be forgot... V for Vendetta")})

@app.route("/token", methods = ['POST'])
def token():
    responseUser = getTokenAplication.getToken(request.get_json())
    if responseUser:  
        flaskResponse = Response(responseUser)
    else:
        data = json.dumps({'message': messages.MessageUser("Could not verify the user!!!")})
        flaskResponse = Response(data)
        flaskResponse.status_code = 403
    flaskResponse.headers["Content-Type"] = "application/json"    
    return flaskResponse

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)
