# -*- coding: utf-8 -*-
import requests
import re
import os
import random
from bs4 import BeautifulSoup
from flask import Flask, request, abort
#from imgurpython import ImgurClient
from argparse import ArgumentParser

def fgo_articles():

    target_url = 'https://forum.gamer.com.tw/B.php?bsn=26742&subbsn=0'
    print('Start parsing fgo_article....')
    rs = requests.session()
    res = rs.get(target_url, verify=True)
    soup = BeautifulSoup(res.text, 'html.parser')

    list_links = [] # Create empty list

    link = soup.select("td[class='b-list__main']")[0].find('a').get('href')


    aaa=soup.select("tr[class='b-list__row']")

    for a in aaa:
        a=a.select("a[class='b-list__main__title']")
        for a in a:
            list_links.append(a.get('href').replace("C.php","https://forum.gamer.com.tw/C.php"))
            print(a.get('href').replace("C.php","https://forum.gamer.com.tw/C.php"))
        

    fgo_articles_content0 = ''
    fgo_articles_content1 = ''
    fgo_articles_content2 = ''
    fgo_articles_content3 = ''
    fgo_articles_content4 = ''
    print("\n")
    fgo_articles_content0=list_links[0]
    fgo_articles_content1=list_links[1]
    fgo_articles_content2=list_links[2]
    fgo_articles_content3=list_links[3]
    fgo_articles_content4=list_links[4]
    
    print(fgo_articles_content0)
    print(fgo_articles_content1)
    print(fgo_articles_content2)
    print(fgo_articles_content3)  
    print(fgo_articles_content4)
    
    return fgo_articles_content0, fgo_articles_content1, fgo_articles_content2, fgo_articles_content3, fgo_articles_content4
