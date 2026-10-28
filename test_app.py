from app import greet, add

def test_greet():
    assert greet("Shreya") == "Hello, Shreya!"

def test_add():
    assert add(5, 3) == 8
    assert add(-1, 1) == 0
