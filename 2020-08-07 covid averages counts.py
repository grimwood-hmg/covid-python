#!/usr/bin/python

opened_file = open('/Users/rawr/Library/Mobile Documents/com~apple~CloudDocs/xcode/COVID Python/data-aVs3O.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

print(apps_data[:1])

total_new_cases = []
for new_cases in apps_data[1:]:
	cases = int(new_cases[1])
	total_new_cases.append(cases)
for date in apps_data[1:]:
	date = str(date[0])
average_total = sum(total_new_cases) / len(total_new_cases)
print(average_total)
print('The average daily case count, as of', date, 'is', average_total,'.')
print(sum(total_new_cases))
print('As of', date, 'there were a cumulative', sum(total_new_cases), 'cases.')