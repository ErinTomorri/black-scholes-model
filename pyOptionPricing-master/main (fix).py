
import sys
import compare
#import wallet #code for saving data
import httphandler
from threading import Thread
import objectCache
import time
import apiCall
import black
import pyXmlScraper.scrape as scrape
from price import price

compare_threads = []

def startDacompare():
    global compare_threads
    gold_end = compare.compare(\
            objectCache.CachedDict().Traded['Gold']['End'],\
            5,\
            100000,\
            30,\
            "GoldEnd")
    silver_end = compare.compare(\
            objectCache.CachedDict().Traded['Silver']['End'],\
            5,\
            100000,\
            30,\
            "SilverEnd")
    dow_above = compare.compare(\
            objectCache.CachedDict().Traded['Dow']['Above'],\
            5,\
            100000,\
            30,\
            "DowAbove")
    thread_gold = Thread(target = gold_end.compare, args = [])
    thread_silver = Thread(target = silver_end.compare, args = [])
    thread_gold.daemon = True
    thread_silver.daemon = True
    thread_gold.start()
    time.sleep(60)
    thread_silver.start()

def threadManager():
    # Reads in config file every half a second, see if anything changes
    # Apply changes accordingly like deleting threads
    f = open('../log/compare.log', 'r')
    f.readline()
    param_name = (f.readline()).split(',')
    

if __name__ == "__main__":
    price() # test
    startDacompare()
    #displayThreads()
    while(1):
        time.sleep(1)