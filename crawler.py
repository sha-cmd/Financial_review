import argparse
import requests
import logging
import http.client
import re
import joblib
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from http import HTTPStatus

def get_link(url):
    parsed_source = urlparse(url)
    result = requests.get(url)
    if result.status_code != HTTPStatus.OK:
        logging.error(f'Error retrieving {url}: {url}')
        return []

    if 'html' not in result.headers['Content-type']:
        logging.info(f'Link {url} is not an HTML page')
        return []

    page = BeautifulSoup(result.text, 'html.parser')
    with open('page.txt', 'w') as f:
        for line in page:
            f.writelines(str(line) + '\n')

def parse():
    with open('page.txt', 'r') as f:
        result = f.read()
    page = BeautifulSoup(result, 'html.parser')
    print(len(page.find_all('p')))
    text = 'Objectif'
    for line in page.find_all('p'):
        search = match(line.text)
        if search is not None:
            #print(line.text)
            res = line.text.replace('\n', '').split(' ')
            scores = [x for x in res if ((x != '') & (x != '\n'))]
            print(scores[6], scores[-1][:-1])

def match(line):
    m = re.search('Objectif', line)
    return m

def parse_div():
    with open('page.txt', 'r') as f:
        result = f.read()
    page = BeautifulSoup(result, 'html.parser')
    l = page.find('div', "c-median-gauge__tooltip")
    print(l.text)



def main(url):
    #get_link(url)
    parse()
    #parse_div()
    #match()
    #print(str.isdecimal('23.32'))
if __name__ == '__main__':
    main('https://www.boursorama.com/cours/1rPGTT/')
