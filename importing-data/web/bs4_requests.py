import requests
from bs4 import BeautifulSoup
import warnings

warnings.filterwarnings('ignore')


def print_status(stage, status_code):
    print(stage, 'OK' if status_code == requests.codes.ok else 'Not found')


def get_token(s):
    p = s.get(repo_url, verify=False)
    print_status('token', p.status_code)
    soup = BeautifulSoup(p.text)
    t = soup.find('meta', {'name': 'csrf-token'})
    token = t['content']
    return token


def sign_in(s, token):
    url_login = repo_url + 'users/auth/ldapmain/callback'
    data = {}
    data['username'] = 'b0xxxxxx'
    data['password'] = 'xxxxxxxxx'
    data['utf8'] = u'\u2713'  # check mark ✓
    data['authenticity_token'] = token
    r = s.post(url_login, data=data, verify=False)
    print_status('sign_in', r.status_code)


repos = ['ilog_oerulesappprescoring',
         'ilog_oerulesappecash',
         'ilog_oerulessbf',
         'ilog_oerulesappagr']
release = 'REL_2017_4_ILOG_4'
repo_url = 'https://git.pl.xxx-xx/'

with requests.Session() as s:
    token = get_token(s)
    sign_in(s, token)

    for repo in repos:
        url_branch = repo_url + 'DAD_WKD/' + repo + '/tree/' + release
        r = s.get(url_branch, verify=False)
        print_status(repo, r.status_code)
