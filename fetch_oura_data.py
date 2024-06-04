import requests

def get_sleep_data(access_token):
    url = "https://api.ouraring.com/v1/sleep"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json()

if __name__ == "__main__":
    access_token = "your_access_token_here"
    sleep_data = get_sleep_data(access_token)
    print(sleep_data)
