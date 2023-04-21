import requests


def make_request(url):
    try:
            return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

with open('subdomain_list.txt','r') as subdomain_list:

    for word in subdomain_list:
        word = word.strip()
        target_url = 'http://'+ word + '.' + 'google.com'
        response = make_request(target_url)
        if response:
            print(f'Found target url subdomin ---> {target_url}')
        else:
            print(f'This domain is not the subdomain of the target url ---> {target_url}')