#############################
# Implemention of function
computeMeanCSV = function(filename, column){

    #Calculates the Mean of a column given as number from a CSV file.
    #
    #   param filename: name of csv-file (str)
    #   param column:   number of column (int)
    #   return:         mean of the column (float)


    # Input
    csv_file = file(filename, open="r")
    csv_lines = readLines(csv_file)
    close(csv_file)

    # Data processing
    csv_lines = csv_lines[-1] # remove header of file (first line)

    csv_lines = strsplit(csv_lines, ",") # split lines seperated by ","

    # sum the requested column
    sum = 0
    for(line in csv_lines){
        sum = sum + as.numeric(line[column])
    }

    mean_column = sum/length(csv_lines)

    # Output
    return(mean_column)
}

#############################
# main part of script
args = commandArgs(trailingOnly = TRUE)

filename = args[1]
column = as.numeric(args[2])

if((length(args)==2) & (!is.na(column))){
    result = computeMeanCSV(filename, column)

    print(paste(c("The mean of the column", column, 'is', result), collapse=" "))
} else{
    print("ERROR: The first argument has to be the filename and the second the integer column number.")
}
