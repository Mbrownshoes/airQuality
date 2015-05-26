# O3_hourly.csv and create daily average
import csv
from datetime import datetime

with open('test_hourly.csv', 'rb') as f:
    reader = csv.reader(f)
    fields = reader.next()
    print(fields)

    subset = {}
    # row = [1,5,5]

    for row in reader:
        for i, val in enumerate(row):
            if i == 1:
                StaName = val
                # print(StaName)
                continue

            if StaName not in subset:
                subset[StaName] = {}

            column_name = fields[i]

            #set up dict keys
            if column_name not in subset[StaName]:
                subset[StaName][column_name] = []

            #store the data

            subset[StaName][column_name].append(val)
    # print(subset)

    newDict = {}
    # print(subset)
    # with open('newData.csv', "w") as output:
    #     writer = csv.writer(output, lineterminator='\n')
    #     writer.writerow(fields) # header
    #     # print(subset)
    for sta_name, sta_data in subset.iteritems():
        print(sta_name)
        if sta_name not in newDict:
            newDict[sta_name] = {}
            for col_name, col_vals in sta_data.iteritems():


                d = []

                if col_name == 'date_time':
                    alldates = [0]
                    stuff=[0]
                    count = 0
                    for j, tm in enumerate(col_vals):

                        # find unique dates for each station
                        if str(datetime.strptime(tm, "%Y-%m-%d %H:%M:%S").date()) not in d:
                            d.append(str(datetime.strptime(tm, "%Y-%m-%d %H:%M:%S").date()))
                            # if count > 0:
                            #     alldates.append(count)

                            count = 0
                            # alldates.append(count)
                        else:
                            count += 1


                            if (count - alldates[-1]) != 1:
                                # print('append: ' + str(alldates[-1]+1))
                                stuff.append((alldates[-1]+1))
                                # print(stuff)
                            else:
                                stuff[-1] = count+1

                            alldates.append(count)


                    # add unique dates list
                    newDict[sta_name][col_name] =d
                    newDict[sta_name]['count'] =stuff
                # v = []
                elif col_name == "value":
                    # for j, val in enumerate(col_vals):
                    #     # print(val)
                    #     # print(newDict[sta_name]['count'])
                    build = 0
                    for ind, v in enumerate(newDict[sta_name]['count']):
                        print('value: ')
                        print(v)
                        avg = col_vals[build:v+build]
                        print(avg)
                        numlist = [float(x) for x in avg]
                        print(sum(numlist)/len(numlist))
                        newDict[sta_name]['O3_Avg'] = sum(numlist)/len(numlist)
                        newDict[sta_name]['O3_Max'] = max(numlist)
                        newDict[sta_name]['O3_Min'] = min(numlist)
                        build+=v


                # print('all the dates: ')
                # print(len(alldates))


                    #
            print(newDict)

                # print(sum(float(col_vals)))
                # for val in col_vals:
                #     print(val)

    # print(newDict)
                # break;
    #         for col_name, col_vals in sta_data.iteritems():
    #             try:
    #                 print(col_name)
    #                 total = sum(column_values)
    #                 # print(total)
    #             except TypeError:
    #                 pass



            # print(sta_data)
                #get total number of days
            # counter = 0
            # if column_name == 'date_time':
            #     for j, tm in enumerate(column_values):
            #         if j == 0:
            #             d = datetime.strptime(tm, "%Y-%m-%d %H:%M:%S").date()
            #             writer.writerow([str(d),])
            #
            #         d1 = datetime.strptime(tm, "%Y-%m-%d %H:%M:%S").date()
            #         if d1 == d:
            #             counter += 1
            #
            #         else: # new day, write average value for previous day for all columns.
            #
            #             # writer.writerow([column_values[:counter]])
            #         # print('days '+str(count))
            # print(column_name)
            # print(counter)
            # for column_name, column_values in sorted(sta_data):
        #     total = sum(column_values)

        # print(total)
