from flask import Flask, request, jsonify, render_template
from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import SyncGrant


app = Flask(__name__)
fake = Faker()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/token')
def generate_token():
    TWILIO_ACCOUNT_SID = 'Enter id here'
    TWILIO_SYNC_SERVICE_SID = 'Enter id here'
    TWILIO_API_KEY = 'Enter Key here'
    TWILIO_API_SECRET = 'Enter Key here'

    username = request.args.get('username', fake.user_name())

    token = AccessToken(TWILIO_ACCOUNT_SID, TWILIO_API_KEY, TWILIO_API_SECRET, identity=username)

    sync_grant_access = SyncGrant(TWILIO_SYNC_SERVICE_SID)
    token.add_grant(sync_grant_access)
    return jsonify(identity=username, token=token.to_jwt())



if __name__ == "__main__":
    app.run()

