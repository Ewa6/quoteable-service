import requests

def test_api():
    r = requests.get("https://httpbin.org/get", timeout=5)
    print("Status:", r.status_code)
    print("Keys:", list(r.json().keys())[:3])

if __name__ == "__main__":
    test_api()