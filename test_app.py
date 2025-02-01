from app import app

def test_home():  #3if we want pytest library to act we have to make functions and files starting name with test 
    response=app.test_client().get('/')
    
    assert response.status_code==200
    assert response.data==b"Hello world"