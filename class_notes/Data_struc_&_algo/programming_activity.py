#pop one off
#print(prices.pop()) #pops last item off the list, acts as stack.

#how to get it to act as a queue, pop the first item off the list.
#print(prices.pop(0)) #pops first item off the list, acts as queue

#convert to a queue

import os

# load all the prices from the file, into a Python List
# stock prices file
curr_dir = os.path.dirname(__file__) # get the current directory of this file

tkr = "AAPL"
stock_fil = curr_dir + "/" + tkr + ".txt" # dirname and __file__ (this file) returns the current folder

file = open(stock_fil, "r")

prices_queue = [float(x) for x in file.readlines()]

prices = []
prices.append(file)
prices.append(float(file.readline()))
prices.append(float(file.readline()))
prices.append(float(file.readline()))
prices.append(float(file.readline()))
prices.append(float(file.readline()))
prices.append(float(file.readline()))



# iterate through prices in list and run strategy
days= 5
buy = 0
profit = 0.0
for i in range(len(prices)):
    p = prices[-1]

    avg = (prices[0] + prices[1] + prices[2] + prices[3] + prices[4]) / 5

    if i >= days:
        p = prices[i]
        
        if p > avg and buy == 0: #buy
            print("buying at: ", p)
            buy = p
        elif p < avg and buy != 0: #sell
            print("selling at: ", p)
            profit += p - buy
            
            print("trade profit: ", p - buy)
            buy = 0
        else:
            pass # do nothing today, except hopefully my position is becoming more profitable
        
        
print("profit: ", profit)
print("percentage returns%: ", 100 * (profit/prices[0]))

input("press enter")