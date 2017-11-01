importData = function(filename){

    #Import the data and restructure from moby-dick.csv
    #
    #   param filename: name of csv-file (str)
    #   return:         chapter, chapterLength, words, wordOccurrence (list)

    # bad way to read the csv file and split it, but it works
    dataFile = read.csv(file=filename, header=TRUE, sep=",")

    chapter = dataFile[[1]]
    chapterLength = dataFile[[2]]

    words = vector("list", length=length(chapter))
    wordOccurrence = vector("list", length=length(chapter))

    for(numChapter in 1:length(chapter)){
        chapterWordOccurrence = gsub('[\"{}]',
            "",
            unlist(strsplit(unlist(strsplit(toString(dataFile[[3]][numChapter]), ", ")), ": "))
        )

        wordOccurrence[numChapter] = list(chapterWordOccurrence[seq(2,length(chapterWordOccurrence),2)])
        words[numChapter] = list(chapterWordOccurrence[seq(1,length(chapterWordOccurrence),2)])

    }


    dataFile = list(chapter, chapterLength, words, wordOccurrence)

    return(dataFile)
}

averageWordOccurence = function(dataFile, specWord){

    #Average occurrences of any word
    #
    #   param dataFile: chapter, chapterLength, words, wordOccurrence (list)
    #   param word:     word for analysis (str)
    #   return:         meanWordOccurrence (float)

    chapter = dataFile[[1]]
    chapterLength = dataFile[[2]]
    words = dataFile[[3]]
    wordOccurrences = dataFile[[4]]

    specWordOccurrence = matrix(0, length(chapter), 1)

    for(numChapter in 1:length(chapter)){
        specWordOccurrence[numChapter] = as.numeric(
            unlist(wordOccurrences[[numChapter]][grep(specWord, words[numChapter])])
        )
    }

    meanWordOccurrence = mean(specWordOccurrence)

    return(list(specWordOccurrence, meanWordOccurrence))
}

histFrequency = function(averageWord, specWord){

    #Create a histogram showing frequency distributions of any give word across all chapters
    #
    #   param dataFile: specWordOccurrence, meanWordOccurrence (list)

    pdf(file="../../WORK/Blatt2/plot.pdf")

    chapterWordOccurrence = as.vector(averageWord[[1]])

    print(chapterWordOccurrence)

    barplot(chapterWordOccurrence,
        main=paste("Histogram of frequency distribution of \"",specWord,"\" over all chapters.", sep=""),
        xlab="Chapters (1...134)"
    )

    #axis(1, seq(1,134,67),c(1,134))
    #, cex.names=0.8
    #names.arg=c(1:length(chapterWordOccurrence))

    dev.off()
}


myData = importData("../../WORK/Blatt2/moby-dick.csv")

specWord = ""

averageWord = averageWordOccurence(myData, specWord)

histFrequency(averageWord, specWord)

#warnings()