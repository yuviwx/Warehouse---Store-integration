import bs4
from bs4 import BeautifulSoup
import requests;
import pandas as pd
import csv

def checker(queryParam):
    flag = False
    url= "http://www.buyballoons.com/heb/seearch?sarch="
    endPoint = url + queryParam
    res = requests.get(endPoint)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    item = soup.select(".row-product-box")
    if item==[]:
        print(queryParam + " doesn't exist")
        return flag
    if(len(item) > 1):
        for product in item:
            i = product.select("div:nth-child(3) > div > div.col-md-7.col-12.add-tocart.pr-0 > div > div.col-12.text-left")
            if i[0].text == ("מק'ט: " + queryParam):
                flag = True
        return flag
    else:
        i = item[0].select("div:nth-child(3) > div > div.col-md-7.col-12.add-tocart.pr-0 > div > div.col-12.text-left")
        if i[0].text == ("מק'ט: " + queryParam):
            return True
    return flag


with open('bbb.csv') as csvfile:
    reader = csv.reader(csvfile)
    count = 0

    for row in reader:
        count += 1
        if count == 2 or count == 1:
            continue
        queryParam = row[0]
        if int(row[1]) > 0:
            if checker(queryParam) == False:
                print(queryParam + " doesn't exist")
        if count > 854:
            break;
