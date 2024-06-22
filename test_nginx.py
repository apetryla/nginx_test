import requests
import sys


EXPECTED_STRING = "Hello world"


def check_nginx():
    response = get_response()

    if is_expected_response(response.text):
        handle_expected_response()
    else:
        handle_unexpected_response(response.text)

def get_response():
    try:
        return requests.get("http://localhost")
    except requests.ConnectionError:
        handle_failed_connection()

def is_expected_response(response_text):
    return EXPECTED_STRING in response_text

def handle_expected_response():
    print("OK")
    sys.exit(0)

def handle_unexpected_response(response_text):
    print(f"Expected '{EXPECTED_STRING}' in the response, got:\n{response_text}")
    sys.exit(2)

def handle_failed_connection():
    print("Failed to connect to Nginx.")
    sys.exit(1)


if __name__ == "__main__":
    check_nginx()
