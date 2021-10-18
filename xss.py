import requests
url = input("Digite la URL >>>  ")
payload = "<script>alert(123)</script>"
xss = requests.post(url + payload)
if payload in xss.text:
	print("Vulnerable a xss..")
	#print(payload)
else: 
	print("No vulnerablea xss...")