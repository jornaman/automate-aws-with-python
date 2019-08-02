# coding: utf-8
import requests
url = '' # Replace with slack webhook url
data = { "text": "Hello, world." }
requests.post(url, json=data)
