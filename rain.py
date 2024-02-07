#!/usr/bin/env python3
from configs import API_URL, REPO_ADDR, REPO_NAME
import requests
import re
import os
import subprocess


def basher(magnet: str, token: str, chatid: str, **kwargs) -> None:
    """ set the the environment variable with passed arg.name to arg.value and then run the main.sh

    :param kwargs: key pair of environment variables
    :return: None
    """

    for i in kwargs:
        os.environ.setdefault(i, kwargs[i])

    subprocess.run(['./main.sh', magnet, token, chatid])


def getIssueContext(response: dict) -> dict:
    """
    this function will get a dict which contain an issue and then return a context of its body, title and attachment_link.

    :param response:
    :return: dict
    """

    x = dict(magnet='', token='', chatid='')
    _ = response.get('body').split('\r\n')
    x['magnet'] = _[0]
    x['token'] = _[1]
    x['chatid'] = _[2]

    return x


res = requests.get(API_URL)
while res.status_code != 200:
    res = requests.get(API_URL)


for issue in res.json():
    if issue.get('state') == 'open':
        if(labels := issue.get('labels')):
            for label in labels:
                if label.get('name') in ['download', 'upload']:
                    x = getIssueContext(issue)
                    basher(magnet=x['magnet'], token=x['token'], chatid=x['chatid'])

