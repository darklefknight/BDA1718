import argparse
import sys
import numpy as np

def calcColumnMeanFromCSV(filename,column):
    """
    Calculates the Mean of a column given as number from a CSV file.

    :param filename: name of csv-file (str)
    :param column:   number of column (int)
    :return:         mean of the column (float)
    """
    with open(filename, "r") as f:
        content = f.readlines()

    del content[0]  # we are not using the column names here, so we delete them

    partLen = len(content[0].split(","))
    if column > partLen: # check if column exists in file
        print("The desired columnnumber %i does not exist in the file which has just %i columns."%(column,partLen))
        sys.exit(1)

    sum = 0
    for line in content:
        useElement = line.split(",")[column-1].rstrip() # just use the desired column and get rid of newline character
        try:
            useElement = float(useElement)
        except:
            print("The Column you would like to know the mean from does not contain numbers.")
            sys.exit(1)
        sum += useElement

    mean = np.divide(sum,len(content))
    return mean


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='File')
    parser.add_argument(type=str, dest="file",
                        help='Provide the filename.')

    parser.add_argument(type=int, dest="column",
                        help='Provide the column of which you want to calculate the mean from. ' +
                             'The left most column has the number 1.')

    file = parser.parse_args().file
    column = parser.parse_args().column

    mean = calcColumnMeanFromCSV(file,column)
    print("The mean of column %i is %f" %(column,mean))
