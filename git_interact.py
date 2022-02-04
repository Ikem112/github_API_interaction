import re
import requests

base_url = "https://api.github.com"

def request_page(gitHub_profile_name):
    
    

    user_url = f"{base_url}/users/{gitHub_profile_name}"
    response = requests.get(user_url)
    response = response.json()

    request = {
        'userName': response['login'],
        'userImage': response['avatar_url'],
        'profileURL': response['html_url'],
        'userCompany': response['company'],
        'userLocation': response['location'],
        'userEmail': response['email'],
        'userBio': response['bio'],
        'userTwitter': response['twitter_username'],
        'userRepo': response['public_repos'],
        'userGists': response['public_gists'],
        'userFollowers': response['followers'],
        'userFollowing': response['following'],
        'pageCreateDay': response['created_at'],
        'pageUpdateDay': response['updated_at'],

    }

    print(request)

def request_repo(gitHub_profile_name):
    user_url = f"{base_url}/users/{gitHub_profile_name}/repos"
    response = requests.get(user_url)
    response = response.json()

    request = []
    for repo in response:
        data = {
            'repo_name': repo['html_url'],
            'repo_desc': repo['description'],
            'repo_lang': repo['language'],
            'repo_created': repo['created_at'],
            'repo_updated': repo['updated_at'],
            'repo_push': repo['pushed_at'],
        }

        request.append(data)
            


    print(request)

def main():

    reply = input('select 1 if you want to view user docs or 2 if you want to view repo docs: ')
    reply = int(reply)

    if reply == 1:
        request_page(input('enter name of the page you would like to pull: '))
    elif reply == 2:
        request_repo(input('enter name of the page you would like to pull: '))
    else:
        print('please enter either 1 or 2')

main()



        
