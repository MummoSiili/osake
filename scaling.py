import csv, sys

'''
FUNCTIONS
'''

def scaleValue(value):
    print(value)

    return value


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
            print('ok')
