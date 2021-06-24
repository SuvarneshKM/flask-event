from flask import Flask, jsonify, request
from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


app = Flask(__name__)


CLIENT_SECRET_FILE = 'client_secret_id.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
 

@app.route('/api', methods=['GET'])
def index():
	return {
		'name': 'Hello World'
	}

@app.route('/api/game', methods=['POST'])
def game():
	return {
	'game': 'passed'
	}

@app.route('/api/send', methods=['POST'])
def send():
	request_data = request.get_json()
	print(request_data)
	# name = request_data['name']
	email = request_data['email']
	# phone = request_data['phone']
	# semester = request_data['semester']
	# branch = request_data['branch']
	# print('name : ' + name)
	# print('email : ' + email)
	# print('phone : ' + phone)
	# print('semester : ' + semester)
	# print('branch : ' + branch)
	# emailMsg = 'Remember ' + name + ' Rafikka Uyir'
	emailMsg = 'Remember suvarnesh Rafikka Uyir'
	mimeMessage = MIMEMultipart()
	mimeMessage['to'] = email
	mimeMessage['subject'] = 'Rafikka Uyir'
	mimeMessage.attach(MIMEText(emailMsg, 'plain'))
	raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

	message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
	print(message)
	return 'Done', 201

if __name__ == '__main__':
	app.run(debug=True)

