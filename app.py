# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login' , methods=['POST'])
def verify_otp():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']

    if username == 'verify' and password == '12345':   
        account_sid = 'ACfe274bc92bb5c1d1e10712dc7749d3e4'
        auth_token = '16e2170a1b96480152fb79c4989d7d69'
        client = Client(account_sid, auth_token)

        verification = client.verify \
            .services('MGf7c738642bd5de8d850ab05ac512452f') \
            .verifications \
            .create(to=mobile_number, channel='sms')

        print(verification.status)
        return render_template('otp_verify.html')
    else:
        return render_template('user_error.html')



@app.route('/otp', methods=['POST'])
def get_otp():
    print('processing')

    received_otp = request.form['received_otp']
    mobile_number = request.form['number']

    account_sid = 'ACfe274bc92bb5c1d1e10712dc7749d3e4'
    auth_token = '16e2170a1b96480152fb79c4989d7d69'
    client = Client(account_sid, auth_token)
                                            
    verification_check = client.verify \
        .services(' MGf7c738642bd5de8d850ab05ac512452f') \
        .verification_checks \
        .create(to=mobile_number, code=received_otp)
    print(verification_check.status)

    if verification_check.status == "pending":
        return render_template('Pass otp_verify html page here')    # Write code here
    else:
        return redirect("https://project-c272.onrender.com/")


if __name__ == "__main__":
    app.run()

