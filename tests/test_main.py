from src import my_one_function

def test_main():
    assert my_one_function("hello") == "hello"

if __name__ == "__main__":
    test_main()
