import requests


base_url = "https://api.github.com"
repo = "https://github.com/Ikem112?tab=repositories"

user_url = f"{base_url}/users/ikem112"

response = requests.get(repo)


print(response.content)

