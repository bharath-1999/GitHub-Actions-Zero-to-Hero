# app.py
# This is a test commit
# demo actions testing ok
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
