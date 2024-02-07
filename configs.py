"""configs are stores here"""
from os import path

BASE_DOMAIN = 'github.com'

REPO_OWNER = 'shabane'

REPO_NAME = 'mp3tor2tel'

API_URL = path.join('https://api.' + BASE_DOMAIN, 'repos', REPO_OWNER, REPO_NAME, 'issues')

REPO_ADDR = path.join('https://', BASE_DOMAIN, REPO_OWNER, REPO_NAME + '.git')

