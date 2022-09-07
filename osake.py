def amountOfStocks():
	stocks = int(input("Amount of stocks: "))
	return stocks	

def shareValue():
	sharevalue = float(input("Share value: "))
	return sharevalue
	
def stockHoldEq():
	assets = int(input("Total assets: "))
	liabilities = int(input("Total liabilities: "))
	stock_eq = assets - liabilities

	return stock_eq

def calcPB():
	stocks = amountOfStocks()
	sharevalue = shareValue()
	book = stockHoldEq()
	pb_value = sharevalue / (book/stocks)
	return round(pb_value, 2)

print(calcPB())
#amountOfStocks('123k')

