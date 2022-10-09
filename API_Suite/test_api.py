import pytest
from API_Suite.ConnectHelper import ConnectHelper as api_connector

def test_create_default_user(point):
    default_user = point.post_users(api_connector.User, api_connector.Lastname, api_connector.Phone, api_connector.Password)
    assert default_user.status_code in [200, 400]
    print(default_user.json())

def test_user_list(token):
    users = token.get_users()
    assert users.status_code == 200
    print(f"User List: {users.json()['payload']}")
    assert users.json()['status'] == 'SUCCESS'
    assert api_connector.User in users.json()['payload']

def test_user_info(token):
    user_info = token.get_user()
    assert user_info.status_code == 200
    print(f"User info: {user_info.json()['payload']}")
    assert api_connector.User in user_info.json()['payload']['firstname']
    assert api_connector.Lastname in user_info.json()['payload']['lastname']
    assert api_connector.Phone in user_info.json()['payload']['phone']
    assert user_info.json()['status'] == 'SUCCESS'

def test_create_same_user_again(point):
    same_user = point.post_users()
    assert same_user.status_code == 400
    print(f"{same_user.json()}")
    assert same_user.json()['status'] == 'FAILURE'
    assert same_user.json()['message'] == 'User exists'

def test_create_a_different_user(point):
    new_user = point.post_users(user_name="KennyDestroyer", last_name="Jofou", phone="000000", pass_word="12345", first_name="Kenny" )
    assert new_user.status_code in [400, 200]
    print(new_user.json())

def test_change_user_something(token):
    req = token.put_user('KennyDestroyer', last_name = 'Bolte', phone = '2222222333')
    assert req.status_code == 201
    print(req.json())
    assert req.json()['status'] == 'SUCCESS'
    assert req.json()['message'] == 'Updated'

def test_change_prohibited(token):
    req = token.put_user('KennyDestroyer', user_name = 'Casper')
    assert req.status_code == 403
    print(req.json())
    assert req.json()['status'] == 'FAILURE'
    assert req.json()['message'] == 'Field update not allowed'

def test_updated_user_info(token):
    user_info = token.get_user('KennyDestroyer')
    assert user_info.status_code == 200
    print(f"User info: {user_info.json()['payload']}")
    assert user_info.json()['status'] == 'SUCCESS'
    assert 'Kenny' in user_info.json()['payload']['firstname']
    assert 'Bolte' in user_info.json()['payload']['lastname']
    assert '2222222333' in user_info.json()['payload']['phone']
    assert user_info.json()['status'] == 'SUCCESS'

def test_nonexisted_user_info(token):
    user_info = token.get_user('ThereIsNothingHere')
    assert user_info.status_code == 500

