import mimetypes
from flask import Flask, Response, request
from twilio.twiml.messaging_response import MessagingResponse
from facts_eng import facts
from resp_int import read_response

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def reply():
    body = request.values.get('Body').lower()
    resp =  MessagingResponse()
    read = read_response(body)
    if isinstance(read, str):
        resp.message(read_response(body))
    else:
        content_var = facts(body)
        formatted = content_var.split('\n\n', 1)[1]
        resp.message(formatted)
        
    return Response(str(resp), mimetype="application/xml")

if __name__ == "__main__":
    app.run(debug=True)
