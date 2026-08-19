import requests


def extract_users(url):
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    return response.json()


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"

    users = extract_users(url)

    print(f"Total users extracted: {len(users)}")
