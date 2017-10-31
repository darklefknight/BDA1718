
importData = function(filename){
    con = file(filename, "r")

    while(TRUE){
        line = readLines(con, n = 1)
        if(length(line) == 0){
            break
        }
        print(line)
    }

    close(con)
}