#!/usr/bin/env python3
import requests
import os
import sys

token = sys.argv[1]
chat_id = sys.argv[2]

tmp = list(os.scandir('.'))
for i in tmp:
  if 'mp3' in i.name:
    if os.path.isfile(i.name):
      file ={"document": open(f'{i.name}', 'rb')}
      res = requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={chat_id}", files=file)
      print(res.content)

