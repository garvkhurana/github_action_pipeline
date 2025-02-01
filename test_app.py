from app import app

def test_home():  
    """Test the home route."""
    response = app.test_client().get('/')
    
    assert response.status_code == 200
    assert response.data == b"hello world"  # Convert expected output to bytes
