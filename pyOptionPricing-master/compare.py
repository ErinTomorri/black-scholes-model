import apiCall
import httphandler
import math
import time


import threading

priceMax = 1000000


class Algo:
    def __init__(self, conList, pLimit, spread, timer, name):
        self.conList = conList
        self.pLimit = pLimit
        self.spread = spread
        self.timer = timer
        self.name = name
        self.running = True
        self.timestamp = time.localtime()

    def __repr__(self):
        return '<Algo Object: ' + self.name + '>'

    def start(self):
        self.running = True
        self.algo()
    def stop(self):
        self.running = False
    def setTimer(self, timer):
        self.timer = timer
    def setLimit(self, limit):
        self.pLimit = limit
    def setSpread(self, spread):
        self.spread = spread
            
    def algo(self):
        i = 1
        while True:
            try:
                self.timestamp = time.localtime()
                apiCallList = []
                cancelList = []
                jList = httphandler.getOrders() # could change to see transactions
                for con in self.conList:
                    # this can be implementede faster
                    oldBuy = None
                    oldSell = None
                    for j in jList:
                        if j['ContractId'] == con.conID:
                            if j['Type'] == 'Bid':
                                oldBuy = j
                            if j['Type'] == 'Ask':
                                oldSell = j
                    value = con.calculate()
                    buy = int(math.floor(value * 100.0) / 100.0 * priceMax) - self.spread
                    sell = int(math.ceil(value * 100.0) / 100.0 * priceMax) + self.spread# temporary
                    # if there isn't any order
                    #FIXME : dont go to sell if buy has none,

                    # get amount
                    if oldBuy == None and oldSell == None:
                        bidAmt = self.pLimit
                        askAmt = self.pLimit
                    elif oldBuy == None:
                        bidAmt = self.pLimit
                        askAmt = oldSell['QuantityLeft']
                    elif oldSell == None:
                        bidAmt = oldBuy['QuantityLeft']
                        askAmt = self.pLimit
                    else:
                        if oldBuy['QuantityLeft'] >= oldSell['QuantityLeft']:
                            bidAmt = self.pLimit
                            askAmt = self.pLimit - abs(oldBuy['QuantityLeft'] - oldSell['QuantityLeft'])
                        else:
                            bidAmt = self.pLimit - abs(oldBuy['QuantityLeft'] - oldSell['QuantityLeft'])
                            askAmt = self.pLimi

                    # Update cancel orders and post orders
                    # FIXME: If buy > 1000000, then sell it at 1000000 vice versa with SEll
                    if (oldBuy == None or buy != oldBuy['Price']) and buy > 0 and buy < 1000000:
                        if oldBuy != None:
                            cancelList.append(oldBuy['OrderId'])
                        apiCallList.append(apiCall.apiCall(con.conID, False, bidAmt, buy))
                    if (oldSell == None or sell != oldSell['Price']) and sell > 0 and sell < 1000000:
                        if oldSell != None:
                            cancelList.append(oldSell['OrderId'])
                        apiCall.append(apiCall.Order(con.conID, True, askAmt, sell))
                   
                cancelstr = apiCall.cancel2str(cancelList)
                orderstr = apiCall.order2str(apiCall)
                if cancelList:
                    httphandler.postCancelOrders(cancelstr)
                if apiCall:
                    httphandler.postAddOrders(orderstr)
            except Exception as e:
                pass
            time.sleep(300)
            i = i + 1

# make sure conList is referenced, and not copied because list might change when update contracts

# FIXME: when 0, it dispears, so doesnt do the right ammount for risk
# maybe solve: even if same price, delete order and ADD new, easier to manage
    
#Note : When Quantitiy left goes to 0, what happens? [disapears] or 0