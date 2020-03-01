from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/nfc', methods=['POST'])
def nfc_input():
    uuid = request.form['uuid']
    date = request.form['date']
    hour = request.form['hour']
    minutes = request.form['minutes']
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    print('\nNFC RESPONSE')
    print('Date: ', date, ' ', hour + ':' + minutes)
    print('UUID: ', uuid)
    print('Location: ', latitude, ', ', longitude)
    print('DONE\n')
    return uuid

app.run()
