import csv, sys

def calcPB(stock_price, shares, assets, liabilities):
	if isInteger == True:
		share_price = int(stock_price)
	else:
		share_price = float(stock_price)

	if isInteger == True:
		amount_shares = int(shares)
	else:
		amount_shares = float(shares)

	if isInteger == True:
		total_assets = int(assets)
	else:
		total_assets = float(assets)

	if isInteger == True:
		total_liabilities = int(liabilities)
	else:
		total_liabilities = float(liabilities)

	PB_value = share_price / ((total_assets - total_liabilities) / amount_shares)
	return f'{PB_value:.2f}'

def calcPS(stock_price, shares, sales):
	if isInteger == True:
		share_price = int(stock_price)
	else:
		share_price = float(stock_price)

	if isInteger == True:
		amount_shares = int(shares)
	else:
		amount_shares = float(shares)

	if isInteger == True:
		total_sales = int(sales)
	else:
		total_sales = float(sales)

	PS_value = share_price / (total_sales / amount_shares)
	return f'{PS_value:.2f}'

# Return PSTTM value
def calcPSTTM(stock_price, ps_ttm, shares):
	palautus = stock_price / (ps_ttm / shares)

	return palautus

def displayData(*args):
	# How many lines will be printed
	rows = len(args[0])

	print('quarter\t\t P/B\t P/S\t P/S(TTM)')
	print('_______\t\t ___\t ____\t ________')

	for i in range(rows):
		print('{0}\t\t{1}\t{2}\t{3}'
		.format(args[0][i], args[1][i], args[2][i], args[3][i]))


def isInteger(n):
	try:
		float(n)
	except ValueError:
		return False
	else:
		return float(n).is_integer()

def isFloat(n):
	try:
		float(n)
	except ValueError:
		return False
	else:
		return True

def scaleValue(csv_line):
	'''
	Scale number by multiply it correspondingly:

	B/b billions
	M/m millions
	K/k thousands

	Return modified list
	'''
	modified_list = []
	multiplier = 0

	for value in csv_line:
		if isInteger(value):
			modified_list.append(int(value))
		elif isFloat(value):
			modified_list.append(float(value))

		else:
			if value[-1:] == 'B' or value[-1:] == 'b':
				multiplier = 1000000000
			elif value[-1:] == 'M' or value[-1:] == 'm':
				multiplier = 1000000
			elif value[-1:] == 'K' or value[-1:] == 'k':
				multiplier = 1000
			else:
				modified_list.append(value)

			if multiplier > 0:
				if isInteger(value[:-1]):
					value = int(value[:-1])
					value = value * multiplier
					modified_list.append(value)
				else:
					value = float(value[:-1])
					value = value * multiplier
					modified_list.append(value)

	return modified_list

def displayData2(stock_dict):
	print("quarter\t\t	P/B")
	print("-------\t\t	---")
	for x,y in stock_dict.items():
		print(x,y)

def getPB(stock_dict):
	'''
	Return a list of PB values
	'''
	palautus_lista = []
	try:
		for value in stock_dict:
			shares = stock_dict[value]['shares']
			price = stock_dict[value]['price']
			assets = stock_dict[value]['assets']
			liabilities = stock_dict[value]['liabilities']
			book_per_share = (assets - liabilities) / shares
			pb_value = price / book_per_share
			palautus_lista.append(round(pb_value, 2))

	except Exception as e:
		raise

	return palautus_lista

def getPS(stock_dict):
	'''
	Return a list of PS values
	'''
	palautus_lista = []

	try:
		for value in stock_dict:
			price = stock_dict[value]['price']
			sales = stock_dict[value]['revenue']
			shares = stock_dict[value]['shares']
			pe_value = price / (sales / shares)
			palautus_lista.append(round(pe_value, 2))
	except Exception as e:
		raise

	return palautus_lista

def getPSTTM(list_of_revenue, list_of_stock_price, list_of_shares):
	'''
	Return a list of PS TTM values. Values in str(). Place * mark after value if
	there is no enough quarters (<4)
	'''
	palautus_lista = []
	ps_ttm = 0.0
	start = 0
	gap = 0
	list_lenght = len(list_of_revenue)

	for value in list_of_revenue:
		if (gap < 4):
		# First items when list is smaller than 4
			ps_ttm += value
			ps_ttm = calcPSTTM(list_of_stock_price[gap], ps_ttm, list_of_shares[gap])
			palautus_lista.append(round(ps_ttm, 2))
			gap += 1
		else:
		# Gap of four items with starting point moving along
			gap_buffer = gap
			ps_ttm = 0.0
			start += 1
			gap += 1
			for four in list_of_revenue[start:gap]:
				ps_ttm += four

			ps_ttm = calcPSTTM(list_of_stock_price[gap_buffer], ps_ttm, list_of_shares[gap_buffer])
			palautus_lista.append(round(ps_ttm, 2))

	if list_lenght < 4:
		for i in range(len(palautus_lista)):
			palautus_lista[i] = str(palautus_lista[i]) + '*'
	else:
		for i in range(3):
			palautus_lista[i] = str(palautus_lista[i]) + '*'

	return palautus_lista

def getQuarters(stock_dict):
	# Return a list of quarters from dictionary keys
	palautus_lista = []

	for x in stock_dict:
		palautus_lista.append(x)

	return palautus_lista

# Return list of stock prices
def getStockPrice(stock_dict):
	palautus_lista = []

	for value in stock_dict:
		palautus_lista.append(stock_dict[value]['price'])

	return palautus_lista

def getRevenue(stock_dict):
	palautus_lista = []

	for value in stock_dict:
		palautus_lista.append(stock_dict[value]['revenue'])

	return palautus_lista

def getShareAmount(stock_dict):
	palautus_lista = []

	for value in stock_dict:
		palautus_lista.append(stock_dict[value]['shares'])

	return palautus_lista

'''
GLOBAL VARIABLES
'''
list_of_PB = []
list_of_PS = []
list_of_PSTTM = []
list_of_quarters = []
list_of_PE = []
list_of_stock_price = []
key_list = []

stock_dict = {}

osake_file = sys.argv

'''
Version 2

Create dictionary with preliminary stock values.
'''
with open(osake_file[1]) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	row = 0

	for value in csv_reader:
		'''
		First value of the CSV file must be quarter. Those will be used dict keys.
		'''
		length = len(value)

		if row == 0:
			# skip first row
			row += 1

			for i in range(length):
				'''
				Collect first row value to a list that will be placed to dict
				keys later in else statement.
				'''
				if i == 0:
					pass
				else:
					key_list.append(value[i]) # key_list is a global variable

		else:
			'''
			Fill dict with keys i.e. stock data
			'''
			stock_dict[value[0]] = {}
			key_list_length = len(key_list)

			for i in range(key_list_length):
				stock_dict[value[0]][key_list[i]] = ''


'''
Fill dictionary with real data
'''

with open(osake_file[1]) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	row = 0

	for value in csv_reader:
		first_element = 0
		if row == 0:
			row += 1 # skip first row
		else:
			value = scaleValue(value)
			for i in range(1, len(value)):
				'''
				Value 0 = quarter = dict key. Fill all stock variables to key
				values
				'''
				stock_dict[value[0]][key_list[first_element]] = value[i]
				if first_element < len(key_list):
					first_element += 1


list_of_PB = getPB(stock_dict)
list_of_PS = getPS(stock_dict)
list_of_stock_price = getStockPrice(stock_dict)
list_of_revenue = getRevenue(stock_dict)
list_of_shares = getShareAmount(stock_dict)
list_of_PSTTM = getPSTTM(list_of_revenue, list_of_stock_price, list_of_shares)
list_of_quarters = getQuarters(stock_dict)
displayData(list_of_quarters, list_of_PB, list_of_PS, list_of_PSTTM)