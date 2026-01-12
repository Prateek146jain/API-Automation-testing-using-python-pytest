import requests
import random
import pytest


# Global variables

User_id=None

print(User_id)
User_email=None
User_name=None

payloads={
    "name":"Tester", 
    "gender":"Male", 
    "email":f"Prateek{random.randint(111,999)}@gmail.com", 
    "status":"Active"
    }

baseurl="https://gorest.co.in/public/v2/users" #Base URl

token="" #Authorization Token

headers={
    "Authorization":f"Bearer {token}",
    "Content-Type":"application/json"
}


# Create New User
@pytest.mark.dependency()
@pytest.mark.order(1)
def test_create_newuser():
    global User_id  # Initiate the Userid value as a global 
    res=requests.post(baseurl,json=payloads,headers=headers)
    data=res.json()
    print(data)
    print(f"User_id:",res.json()["id"])
    assert res.status_code==201 , "Wrong Status code" 
    # assert res.headers["Content-Type"] == "application/json", "Wrong Contant type" 
    assert "application/json" in res.headers["Content-Type"]
    # assert res.elapsed.total_seconds()<2, "Too Slow"

    User_id=data["id"]

  #fetch the user details 
@pytest.mark.order(2)
def test_get_user_details():
    res=requests.get(f"{baseurl}/{User_id}", headers=headers)
    assert res.status_code==200, "Wrong status code"
    # assert res.elapsed.total_seconds()<2, "too slow"
    assert "application/json" in res.headers["Content-Type"], "wrong contant-type"
    # assert res.json("id") ==User_id , "not Same user id "

    data= res.json()
    print(data)


@pytest.mark.order(4)
def test_get_user_update_details():
    res=requests.get(f"{baseurl}/{User_id}", headers=headers)
    assert res.status_code==200, "Wrong status code"
    # assert res.elapsed.total_seconds()<2, "too slow"
    assert "application/json" in res.headers["Content-Type"], "wrong contant-type"
    # assert res.json("id") ==User_id , "not Same user id "

    data= res.json()
    print(data)

    #update the user detials 
@pytest.mark.order(3)
@pytest.mark.dependency(depends=["test_create_newuser"])

def test_update_user_details():  # put request
    update_data={
        "name":"Jainwpkj",
        "email":f"jain{random.randint(1111,9999)}@gmail.com",
        "status":"active"
    }
    
    res = requests.put(f"{baseurl}/{User_id}",json=update_data,headers=headers)
    assert res.status_code == 200, "wrong Status code"
    assert "application/json" in res.headers["Content-Type"], "wrong Contant-type"
    data = res.json()
    print(data)

@pytest.mark.order(5)
def test_delete_user():
    res =requests.delete(f'{baseurl}/{User_id}',headers=headers)
    print(User_id)
    assert res.status_code==204


def test_get_user_delete_details():
    res=requests.get(f"{baseurl}/{User_id}", headers=headers)
    assert res.status_code==404, "Wrong status code"
    # assert res.elapsed.total_seconds()<2, "too slow"
    assert "application/json" in res.headers["Content-Type"], "wrong contant-type"
    # assert res.json("id") ==User_id , "not Same user id "
    print(User_id)