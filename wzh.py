
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by betalun on 3/31/17

"""
a ask zhihu command tool
inspired by howdoi
"""

import argparse
import requests
import random
import logging
import pyquery as pq

SEARCH_ENGINE_URL = 'http://www.google.com/search?q=site:{0}%20{1}'
BASE_SITE = 'https://www.zhihu.com/'
USER_AGENTS = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
               'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
               'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
               ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) '
                'Chrome/19.0.1084.46 Safari/536.5'),
               ('Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46'
                'Safari/536.5'), )



def get_instructions(args):
    url = SEARCH_ENGINE_URL.format(BASE_SITE,'%20'.join(args['query']))
    doc = pq(requests.get(url,headers={"User-Agent":random.choice(USER_AGENTS)}).text)
    pass


def main():
    args = argparse.ArgumentParser("==== ask me everything ====")
    args.add_argument('query',action='store',help='descripe your question',nargs='*')
    args = vars(args.parse_args())
    print(get_instructions(args))

if __name__ == '__main__':
    main()