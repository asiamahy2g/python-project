import requests

url = [ "htt://google.com", 'http://45.33.11.12:8082','https://cnn.com', 'https://aws.amazon.com']

resp = requests.get(url)
for link in url:
    if resp.status_code == 200:
        print("Site is up")
    else:
        print("Site is down")