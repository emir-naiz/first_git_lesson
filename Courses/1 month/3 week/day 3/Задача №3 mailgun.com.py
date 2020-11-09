import requests
def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/sandbox06a5a878e99348299d2b7540febd9ea6.mailgun.org/messages",
		auth=("api", "0c861052fd4572c23dfa4314ca92b022-9b1bf5d3-ace468ed"),
		data={"from": "naizabekoff@mail.ru",
			"to": ["maximneveraa@gmail.com"],
			"subject": "Hello",
			"text": "Здааровааааааааа!"})

send_simple_message()