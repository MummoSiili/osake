import csv

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

def calcPB(stock_price, shares, assets, liabilities):
	share_price = float(stock_price)
	amount_shares = int(shares)
	total_assets = int(assets)
	total_liabilities = int(liabilities)
	PB_value = share_price / ((total_assets - total_liabilities) / amount_shares)
	return f'{PB_value:.2f}'

def calcPS(stock_price, shares, sales):
	share_price = float(stock_price)
	amount_shares = int(shares)
	total_sales = int(sales)
	PS_value = share_price / (total_sales / amount_shares)
	return f'{PS_value:.2f}'

def displayData(*argv):
	# How many lines will be printed
	rows = len(argv)
	for value in rows:
		print(value)

list_of_PB = []
list_of_PS = []

with open('osake.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')

	row = 0
	for value in csv_reader:
		if row == 0:
			# skip first row
			row += 1
		else:
			row += 1
			list_of_PB.append(calcPB(value[1], value[2], value[3], value[4]))
			list_of_PS.append(calcPS(value[1], value[2], value[0]))

displayData(list_of_PB, list_of_PS)
# print(list_of_PB)
# print(list_of_PS)
