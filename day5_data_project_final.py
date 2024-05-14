import statistics                  # USING STATS MODULE INSTEAD OF WRITING FUNCTIONS FROM SCRATCH ... FUGGEDABOUDIT

outFileName = 'compare_semester.txt'
compare = open(outFileName, "w")   # WRITES NEW REPORT TO FILE

def read_file(fileName):
    dataFile = open(fileName)
    i = 0
    list1 = []
    list2 = []

    for line in dataFile:           # CONSUME FUNC RETURNS TO NEW VARIABLE
        ls_result = line_score(line)
        # print(ls_result)
        # print(line_score(line))
        semester = ls_result[0]
        # print(semester)
        score = ls_result[1]
        # print(score)
        # print(semester == str('Fall 2016'))  # TEST BOOLEAN ON LIST SPLITTER

        if semester == 'Fall 2016':    # SPLIT AND APPEND SCORES TO SEMESTER LISTS
            list1.append(int(score))
        else:
            list2.append(int(score))

        i += 1  # iterate lines in file

    # print(list1)                          # TESTING STATS FUNCTIONS
    # print(round(mean_calc(list1), 2))
    # print(median_calc(list1))
    # print(round(std_dev_calc(list1), 2))
    #
    # print(list2)
    # print(round(mean_calc(list2), 2))
    # print(median_calc(list2))
    # print(round(std_dev_calc(list2), 2))

#******************************************
# GENERATES REPORT
#******************************************

    print("Source File:", fileName, ":", str(i), "lines")       # PRINT REPORT TO CONSOLE
    print()
    print("     ", "Fall 2016", "Spring 2016")
    print("Mean:    ", round(mean_calc(list1), 2),'', round(mean_calc(list2), 2))
    print("Median:   ", median_calc(list1),'', median_calc(list2))
    print("STD:      ", round(std_dev_calc(list1), 2),'', round(std_dev_calc(list2), 2) )

    # print(fileName,":", i, "lines,")

    output1 = ["Source File:", fileName, ":", str(i), "lines"]
    output2 = ''
    output3 = ["     ", "Fall 2016", "Spring 2016"]
    output4 = ["Mean:    ", str(round(mean_calc(list1), 2)), '', str(round(mean_calc(list2), 2))]
    output5 = ["Median:   ", str(median_calc(list1)), '', str(median_calc(list2))]
    output6 = ["STD:      ", str(round(std_dev_calc(list1), 2)), '', str(round(std_dev_calc(list2), 2))]

    separator = ' '                                 # PRINT REPORT TO FILE ... THIS NEEDS TO BE MORE ELEGANT
    print(separator.join(output1), file=compare)
    print(separator.join(output2), file=compare)
    print(separator.join(output3), file=compare)
    print(separator.join(output4), file=compare)
    print(separator.join(output5), file=compare)
    print(separator.join(output6), file=compare)

    dataFile.close()

#******************************************
# SUBROUTINES
#******************************************

def line_score(line):               # CONSUME LINE LIST ITEMS
    line_values = line.split(',')
    # print(line_values)
    l_semester = line_values[1]
    # print(l_semester)
    l_score = line_values[2]
    # print(l_score)
    return [l_semester, l_score]

def mean_calc(list1):  # CALCULATES MEAN FROM LISTS
#   mean = print("The mean for this dataset is: ", int(total_score/i))
    mean = statistics.mean(list1)
    return mean

def median_calc(list1):  # CALCULATES MEDIAN FROM LISTS
    med = statistics.median(list1)
    return med

def std_dev_calc(list1):  # CACULATES STD DEV FROM LISTS
    std = statistics.stdev(list1)
    return std

#******************************************
# MAIN FUNC
#******************************************

def main():
    fileName = 'sample_grades.csv'
    print(read_file(fileName))

main()

