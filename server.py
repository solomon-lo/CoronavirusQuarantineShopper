from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# alreadysentfirstText = False

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    number = request.values.get('From', None)

    print(number)

    # Start our TwiML response
    resp = MessagingResponse()
    
    # if not alreadysentfirstText:
    #     resp.message("You are enrolled in Solomon James Rushil inventory service. To buy toilet paper, text 1. To buy hand saniter, text 2.")
    #     #tempBool = True
    
    #alreadysentfirstText = tempBool
    # Determine the right reply for this message
    if body == '1':
        resp.message("We will text you when toilet paper is available")
    elif body == '2':
        resp.message("We will text you when hand sanitizer is available")
    else:
        resp.message("You are enrolled in Solomon James Rushil inventory service. To buy toilet paper, text 1. To buy hand saniter, text 2.")
    # alreadysentfirstText = True
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

storeNames = []

listOfNumbers = []