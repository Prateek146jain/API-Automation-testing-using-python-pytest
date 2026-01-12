import pytest
import requests

token = "5a3a0dc0493f9577761fd2395d9f8a380ce179da3dc75781ee44ff6e94fdf638"

baseurl="https://gorest.co.in/public/v2/users"

headers={
    "Authorization":f"Bearer {token}",
    "Content-Type":"application/json"
}

user_id =[]
req=requests.get(f'{baseurl}',headers=headers)
data=req.json()
if data["email"]=="%jain%":
    print(data)
# for id in data:

    