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

def calcPSTTM(PS_list, stock_price):
	'''
	Combine four latest quarters together and return sum
	'''
	list_lenght = len(PS_list)
	share_price = float(stock_price)
	float_value = 0.0 # format value
	ps_ttm = 0.0

	if list_lenght < 4:
		# List less than four quarters are not TTM. Return with mark.
		for value in PS_list:
			float_value += float(value)

		ps_ttm = share_price / float_value
		palaute = str(f'{ps_ttm:.2f}') + '*'
		return palaute

	elif list_lenght == 4:

		for value in PS_list:
			float_value += float(value)

		ps_ttm = share_price / float_value
		return str(f'{ps_ttm:.2f}')

	elif list_lenght > 4:

		for value in PS_list[-4:]:
			# Last four quarters of the list
			float_value += float(value)

		ps_ttm = share_price / float_value
		return str(f'{ps_ttm:.2f}')


def displayData(*args):
	# How many lines will be printed
	rows = len(args[0])

	print('quarter\t\t P/B\t P/S\t P/S(TTM)')
	print('_______\t\t ___\t ____\t ________')

	for i in range(rows):
		ttm_i = i + 1
		ps_ttm = calcPSTTM(args[2][:ttm_i], args[3][i])
		print(args[0][i]+'\t\t'+args[1][i]+'\t'+args[2][i]+'\t'+ps_ttm)

def isInteger(n):
	try:
		float(n)
	except ValueError:
		return False
	else:
		return float(n).is_integer()

def scaleValue(csv_line):
	'''
	Scale number by multiply it correspondingly:

	B/b billions
	M/m millions
	K/k thousands

	Return modified list
	'''
	modified_list = []

	for value in csv_line:
		if str.isdecimal(value[-1:]):
			modified_list.append(value)
		else:
			if value[-1:] == 'B' or value[-1:] == 'b':
				multiplier = 1000000000
			elif value[-1:] == 'M' or value[-1:] == 'm':
				multiplier = 1000000
			elif value[-1:] == 'K' or value[-1:] == 'k':
				multiplier = 1000
			else:
				modified_list.append(value)

			if isInteger(value[:-1]) == True:
				value = int(value[:-1])
				palaute = value * multiplier
				value = str(palaute)	# replace original value
				modified_list.append(value)

			else:
				if isInteger(value[:-1]) == False: # This will skip quarterly string
					pass
				else:
					value = float(value[:-1])
					palaute = value * multiplier
					value = str(palaute)	# replace original value
					modified_list.append(value)

	return modified_list

list_of_PB = []
list_of_PS = []
list_of_quarters = []
list_of_PE = []
list_of_stock_price = []

'''
Take CSV file as command line argument e.g. osake.py osake.csv
'''
osake_file = sys.argv

with open(osake_file[1]) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	row = 0

	for value in csv_reader:
		if row == 0:
			# skip first row
			row += 1
		else:
			row += 1
			value = scaleValue(value)
			list_of_PB.append(calcPB(value[1], value[2], value[3], value[4]))
			list_of_PS.append(calcPS(value[1], value[2], value[0]))
			list_of_quarters.append(value[5])
			list_of_stock_price.append(value[1])

displayData(list_of_quarters, list_of_PB, list_of_PS, list_of_stock_price)
