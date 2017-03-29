
import urllib.request as u
from bs4 import BeautifulSoup as bs
import pandas as pd

"""
First visit www.Finviz.com and get the base url for the quote page.
example: http://finviz.com/quote.ashx?t=aapl

Then write a simple function to retrieve the desired ratio.
In this example I'm grabbing Price-to-Book (mrq) ratio
"""


listt = ''''Index	DJIA S&P500	P/E	17.22	EPS (ttm)	8.35	Insider Own	0.03%	Shs Outstand	5.26B	Perf Week	2.83%
Market Cap	755.96B	Forward P/E	14.17	EPS next Y	10.15	Insider Trans	-42.27%	Shs Float	5.24B	Perf Month	5.02%
Income	45.22B	PEG	1.86	EPS next Q	2.01	Inst Own	61.20%	Short Float	1.01%	Perf Quarter	23.95%
Sales	218.12B	P/S	3.47	EPS this Y	-9.90%	Inst Trans	0.59%	Short Ratio	1.95	Perf Half Y	28.60%
Book/sh	24.99	P/B	5.75	EPS next Y	13.51%	ROA	14.30%	Target Price	144.48	Perf Year	36.37%
Cash/sh	11.53	P/C	12.47	EPS next 5Y	9.25%	ROE	34.90%	52W Range	88.15 - 142.80	Perf YTD	24.70%
Dividend	2.28	P/FCF	18.83	EPS past 5Y	16.00%	ROI	20.60%	52W High	0.70%	Beta	1.17
Dividend %	1.59%	Quick Ratio	1.20	Sales past 5Y	14.80%	Gross Margin	38.50%	52W Low	63.13%	ATR	1.58
Employees	116000	Current Ratio	1.20	Sales Q/Q	3.30%	Oper. Margin	27.10%	RSI (14)	75.23	Volatility	1.46% 1.08%
Optionable	Yes	Debt/Eq	0.66	EPS Q/Q	2.30%	Profit Margin	20.70%	Rel Volume	1.23	Prev Close	140.88
Shortable	Yes	LT Debt/Eq	0.56	Earnings	May 02 AMC	Payout	26.60%	Avg Volume	27.15M	Price	143.8'''

list1 = listt.split("\t" or "\n")


list2 = []

unneeded = ["\n","%",".",",","+","-"]

for i in range(0, len(list1)):
    word = list(list1[i])

    no = 0
    nb = 0
    for j in range(0, len(word)):
        charac = word[j]
        if charac.isdigit():
            no += 1
        elif charac == "\n":
            nb += 1


    if no == 0:
        list2.append(list1[i])
    if nb != 0:
        word2 = []
        for k in range(0,len(word)):
            charac2 = word[k]
            if charac2.isdigit() or charac2 in unneeded:
                continue
            else:
                word2.append(charac2)

        list2.append("".join(word2))

list2.remove('Yes')
list2.remove('Yes')




class GetFIN:
    @staticmethod
    def get_price2book(self):
            try:
                url = r'http://finviz.com/quote.ashx?t='+format(sym.lower())
                html = u.urlopen(url).read()
                soup = bs(html, 'lxml')
                # Change the text below to get a diff metric
                pb = soup.find(text = r'P/B')
                pb_ = pb.find_next(class_='snapshot-td2').text
                print('{} price to book = {}'.format(sym, pb_))
                return pb_
            except Exception as e:
                print("Error in get_price2book:",e)

    def geto(self,tick,data):
        try:
            self.tick = tick
            self.data = data
            url = r'http://finviz.com/quote.ashx?t=' + format(tick.lower())
            html = u.urlopen(url).read()
            soup = bs(html, 'lxml')
            # Change the text below to get a diff metric
            pb = soup.find(text=data)
            pb_ = pb.find_next(class_='snapshot-td2').text
            print(data+" of "+tick+" = "+pb_ )
            return pb_
        except Exception as e:
            print("Error in getting finc:", e)

"""
Construct a pandas series whose index is the list/array
of stock symbols of interest.

Run a loop assigning the function output to the series
"""
stock_list = ['XOM','AMZN','AAPL','SWKS']


CClas = GetFIN()

verbs = ["find","search","get"]
pronouns = ["of","to"]

print("How can I help?")
userinput=input()
splited = userinput.split(" ")
fund = ""
ticker = ""
for i in range(0,len(splited)):
    if splited[i].lower() in verbs:
        fund = splited[i+1]
    elif splited[i] in pronouns:
        ticker = splited[i+1]


CClas.geto(ticker,fund)


