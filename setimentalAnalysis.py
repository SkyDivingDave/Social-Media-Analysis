# coding = utf8
# author = miles.gw
# date = 2016.12.22

from __future__ import print_function, unicode_literals
from bosonnlp import BosonNLP
import csv

import doubanCrawler


if __name__ == "__main__":

    nlp = BosonNLP('iRUYrpjx.11226.6ZDWPI_ZPhf5')

    with open('douban_taijiong.csv', 'rb') as f:
        reader = csv.reader(f)

        for item in reader:
            result = nlp.sentiment(item[-1])
            print (str(result) + "  " + str(item[1]))