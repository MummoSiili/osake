import sys
import csv
import pymongo

# Read 'data.csv' file and return a list

def read_csv_file(file_name):

    list_return = []

    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            list_return.append(row)
        return list_return

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
def scale_value(list_of_values):
    '''
    	Scale number by multiply it correspondingly:

    	B/b billions
    	M/m millions
    	K/k thousands

    	Return modified list
    	'''
    modified_list = []
    multiplier = 0

    for value in list_of_values:
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

def add_to_db(usage_list, db_collection):
    # delete existing db first to insert new one from csv
    db_collection.delete_many({})

    # create new db from csv
    db_list = []
    id = 1
    for i in range(1, len(usage_list)):
        usage_list[i] = scale_value(usage_list[i])
        db_list.append({'_id': id, 'quarter': usage_list[i][0], 'shares': usage_list[i][1], 'revenue': usage_list[i][2],
                        'assets': usage_list[i][3], 'liabilities': usage_list[i][4], 'price': usage_list[i][5]})
        id += 1

    db_collection.insert_many(db_list)

def show_tickers(list):
    print('\ncurrent tickers:')
    for value in list:
        print(value)
def add_remove_collection(database):
    while True:
        collection_list = database.list_collection_names()  # real all tickers to list
        show_tickers(collection_list)
        print('''
(1) add ticker
(2) remove ticker
(3) exit
choose what to do: ''', end='')
        valinta = input()

        if valinta == '1':
            show_tickers(collection_list)
            print('\ntype "exit" to cancel.')
            while True:
                # loop until new ticker is seen
                stock_ticker = input('give name of stock ticker: ')
                if stock_ticker in collection_list:
                    print('ticker already exists. choose another one.')
                else:
                    break

            if stock_ticker != 'exit': # do not run further. just exit
                testdict = {'_id': 1, 'quarter': '', 'shares': '', 'revenue': '', 'assets': '', 'liabilities': '',
                            'price': ''}
                dbret = database[stock_ticker]
                dbret.insert_one(testdict)

        elif valinta == '2':
            show_tickers(collection_list)
            print('\ntype "exit" to cancel.')
            while True:
                # loop until ticker is mathed
                stock_ticker = input('remove ticker: ')
                if stock_ticker in collection_list:
                    removecol = database[stock_ticker]
                    removecol.drop()
                    break
                elif stock_ticker == 'exit':
                    break
                else:
                    print('choose correct ticker!')

        elif valinta == '3':
            break


def read_collections(database):
    show_collections(database)
    collection_list = database.list_collection_names()
    while True:
        valinta = input('write ticker: ')
        if valinta in collection_list:
            break
        else:
            print('choose correct ticker!')

    collection = database[valinta]
    for value in collection.find():
        print(value)

def show_collections(col):
    collection_list = col.list_collection_names()
    print('current tickers:')
    for value in collection_list:
        print(value)
def main():
    # create and use db
    db_client = pymongo.MongoClient('mongodb://localhost:27017')
    mydb = db_client['stock_db']  # define db

    while True:
        print('''
(1) import CSV file
(2) add or remove ticker
(3) read data
(4) exit

Choose what to do? ''', end='')

        valinta = int(input())

        if valinta == 1:
            stock_ticker = input('Give name of stock ticker: ')
            db_collection = mydb[stock_ticker]  # collection / stock ticker in this case
            file_name = input('Give CSV file name: ')
            csv_list = read_csv_file(file_name)
            add_to_db(csv_list, db_collection)
        elif valinta == 2:
            add_remove_collection(mydb)
        elif valinta == 3:
            read_collections(mydb)
        elif valinta == 4:
            sys.exit(0)


if __name__ == "__main__":
    main()