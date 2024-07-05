import requests

def check_application_health(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"The application at {url} is UP.")
        else:
            print(f"The application at {url} is DOWN. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"The application at {url} is DOWN. Error: {e}")

if __name__ == "__main__":
    url =  "http://example.com/nonexistentpage" 
    check_application_health(url)
