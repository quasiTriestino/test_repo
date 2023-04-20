from src import my_one_function

def test_main_hello():
    assert my_one_function("hello") == "hello"

# def test_main_nerp():
#     assert my_one_function("nerp") == "hello"

if __name__ == "__main__":
    test_main_hello()
#    test_main_nerp()
