#!/usr/bin/python
#https://github.com/ihebski/XSS-Payloads

import time
import argparse
import requests


def xss(url, payload):
	xss = requests.post(url + payload)
	if payload in xss.text:
		print("Vulnerable a xss el payload es: ", url+payload)
		#print(payload)
	else:
		print("No vulnerablea xss...")


parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, 
                                 description="###############         Aureliohacking        ###############\n" \
                                             "          Simple guerza bruta ssh\n"
                                             "Usar: python xss.py --url url --P Lista de payload\n\n" \
                                             "Demo: xxxxxxxxxxxxxxxxxxxx\n"\
                       "GitHub:  github.com/aureliohacking\n" \
                                             "Contact: aureliocheveroni182@gmail.com")

parser.add_argument('--url', action = 'store', dest = 'url', required = True, help = 'Digita la URL')
parser.add_argument('--P', action = 'store', dest = 'payload', required = True, help = 'Listado de Password')

arguments = parser.parse_args()

url = arguments.url
listado_payload =  arguments.payload

lista = open(listado_payload, 'r')

for lista in lista.read().split("\n"):
	xss(url, lista)