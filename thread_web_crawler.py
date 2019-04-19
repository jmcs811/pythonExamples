#!/usr/bin/evn python

import threading
import requests
import re

def get_links(body: str):
    links = re.findall('"((http)?://.*?)"', body)
    return links  

def get_website(url: str):
    #gets html from website
    html_data = requests.get(url)
    return html_data.text

def main():
    html = get_website('http://www.google.com')
    found_links = get_links(html)
    print(found_links)
    threads = []
    for link in found_links:
        try:
            t = threading.Thread(target=get_website, args=(link,))
            threads.append(t)
            t.start()
        except:
            pass

main()