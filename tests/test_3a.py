"""As the first task you should use pet swagger: https://petstore.swagger.io/
Endpoint - users.
You need to write CRUD operation tests for testing this endpoint."""

import requests

address = 'https://petstore.swagger.io/v2/user/'

myfirstUser = {
  "username": "Mich",
  "firstName": "Michael",
  "lastName": "Yakunin",
  "email": "Voyak.email",
  "password": "222333",
  "phone": "111111111",
  "userStatus": 0
}

mysecondUser = {
  "username": "Petrok",
  "firstName": "Petr",
  "lastName": "Simolov",
  "email": "Petrok.email",
  "password": "323232",
  "phone": "22222222",
  "userStatus": 1
}

url_1 = f'{address}{myfirstUser["username"]}'
url_2 = f'{address}{mysecondUser["username"]}'

def test_delete_exist_user():
    response = requests.get(address + 'logout')
    assert response.status_code == 200
    response = requests.get(url_1)
    if response.status_code == 200:
        a = requests.delete(url_1)
        print('User ' + myfirstUser["username"] + ' is successfully deleted')
    else:
        assert response.status_code == 404
        print('User ' + myfirstUser["username"] + ' is not found')

def test_create_new_user():
    response = requests.post(
        url=f'{address}',
        json=myfirstUser)
    assert response.status_code == 200
    print('User ' + myfirstUser["username"] + ' is created successfully')
    response = requests.get(url_1)
    fields = response.json()
    del fields['id']
    if fields == myfirstUser:
        print('User ' + myfirstUser["username"] + ' is successfully added')
    else:
        print('Some problems with adding')

def test_read_exist_user():
    response = requests.get(url_1)
    assert response.status_code == 200

def test_read_no_exist_user():
    response = requests.get(url_2)
    assert response.status_code == 404
    requests.delete(url_1)
    response = requests.get(url_1)
    assert response.status_code == 404


def test_update_exist_no_logged_user():
    response = requests.get(url_1)
    if response.status_code == 404:
        requests.post(url=f'{address}', json=myfirstUser)
        print('User ' + myfirstUser["username"] + ' successfully create')
    logout = requests.get(address + 'logout')
    assert logout.status_code == 200
    response = requests.get(url_1)
    num = response.json()['id']
    response = requests.put(url_1, json={
        "id": num,
        "username": "Mich",
        "firstName": "Michael",
        "lastName": "Yakunin",
        "email": "Voyak.email",
        "password": "222333",
        "phone": "13",
        "userStatus": 0
    })
    response = requests.get(url_1)
    fields = response.json()
    del fields['id']
    assert fields != myfirstUser
    print("No-logged user is updated")

def test_update_exist_logged_user():
    response = requests.get(url_1)
    if response.status_code == 404:
        requests.post(url=f'{address}', json=myfirstUser)
        print('User ' + myfirstUser["username"] + ' successfully create')
    login = requests.get(address + 'login', params={
        "username": myfirstUser["username"],
        "password": myfirstUser["password"]
    })
    assert login.status_code == 200
    response = requests.get(url_1)
    num = response.json()['id']
    response = requests.put(url_1, json={
        "id": num,
        "username": "Mich",
        "firstName": "Michael",
        "lastName": "Yakunin",
        "email": "Voyak.email",
        "password": "222333",
        "phone": "12",
        "userStatus": 0
    })
    response = requests.get(url_1)
    fields = response.json()
    del fields['id']
    assert fields != myfirstUser
    print("Logged User is successfully updated")
    logout = requests.get(address + 'logout')
    assert logout.status_code == 200

def test_update_not_exist_user():
    response = requests.get(url_2)
    if response.status_code == 200:
        requests.delete(url_2)
        print('User ' + mysecondUser["username"] + ' successfully delete')
    response = requests.put(url_2, json=mysecondUser)
    assert response.status_code == 200                  # there is maybe mistake, because method PUT
    print("Can update non-exist user")                  # during swagger documentation must return status_code 404
    assert requests.get(url_2).status_code == 200      # if you want to update non-existed user
    print("User is defined")
    response = requests.delete(url_2)
    assert response.status_code == 200

def test_delete_existed_logged_user():
    response = requests.get(url_1)
    login = requests.get(address + 'login', params={
        "username": myfirstUser["username"],
        "password": myfirstUser["password"]
    })
    assert response.status_code == 200
    response = requests.delete(url_1)              # during swagger documentation must return status_code 404
    assert response.status_code == 200             # because logged in users can't be deleted

def test_delete_existed_no_logged_user():
    response = requests.get(url_1)
    if response.status_code == 404:
        requests.post(url=f'{address}', json=myfirstUser)
        print('User ' + myfirstUser["username"] + ' successfully create')
    response = requests.get(url_1)
    assert response.status_code == 200
    logout = requests.get(address + 'logout')
    assert logout.status_code == 200
    response = requests.delete(url_1)
    print('User ' + myfirstUser["username"] + ' is successfully deleted')
    assert response.status_code == 200

def test_delete_no_existed_user():
    response = requests.get(url_1)
    if response.status_code == 200:
        requests.delete(url_1)
        print('User ' + myfirstUser["username"] + ' is successfully deleted')
    response = requests.get(url_1)
    assert response.status_code == 404
    response = requests.delete(url_1)
    assert response.status_code == 404
    response = requests.delete(url_2)
    assert response.status_code == 404
    print('User ' + mysecondUser["username"] + ' is not defined')

