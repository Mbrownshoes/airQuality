# O3_hourly.csv and create daily average
import csv
from datetime import datetime

with open('test_hourly.csv', 'rb') as f:
    reader = csv.reader(f)
    fields = reader.next()
    print(fields)

    dicte = {}
    # row = [1,5,5]

    for row in reader:
        for i, val in enumerate(row):
            if i == 1:
                StaName = val
                print(StaName)
                continue

            if StaName not in dicte:
                dicte[StaName] = {}
            column_name = fields[i]
            if column_name not in dicte[StaName]:
                dicte[StaName][column_name] = []

            #store the data
            dicte[StaName][column_name].append(val)
    # print(dicte)

    for sta_name, sta_data in dicte.iteritems():
         for column_name, column_values in sta_data.iteritems():
            # total = sum(column_values)
            # with open('newData.csv', "w") as output:
            #     writer = csv.writer(output, lineterminator='\n')
            #     writer.writerow(fields) # header

                #get total number of days
            counter = 0
            if column_name == 'date_time':
                for j, tm in enumerate(column_values):
                    if j == 0:
                        d = datetime.strptime(tm, "%Y-%m-%d %H:%M:%S").date()
                        writer.writerow([str(d),])

                    d1 = datetime.strptime(tm, "%Y-%m-%d %H:%M:%S").date()
                    if d1 == d:
                        counter += 1

                    else: # new day, write average value for previous day for all columns.

                        # writer.writerow([column_values[:counter]])
                    # print('days '+str(count))
            print(column_name)
            print(counter)
            # for column_name, column_values in sorted(sta_data):
        #     total = sum(column_values)

        # print(total)
