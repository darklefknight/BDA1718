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

histOneFrequency = function(averageWord, chapterLength, specWord){

    #Create a histogram showing frequency distributions of any give word across all chapters
    #
    #   param dataFile: specWordOccurrence, meanWordOccurrence (list)

    pdf(file="../../WORK/Blatt2/2-1-histOneFrequency.pdf")

    chapterWordOccurrence = as.vector(averageWord[[1]])

    freqDist = chapterWordOccurrence/chapterLength

    barplot(freqDist,
        main=paste("Histogram of frequency distribution of \"",specWord,"\" over all chapters.", sep=""),
        xlab="Chapters (1...134)"
    )

    #axis(1, seq(1,134,67),c(1,134))
    #, cex.names=0.8
    #names.arg=c(1:length(chapterWordOccurrence))

    dev.off()
}

histAllFrequency = function(dataFile){

    #Create a histogram showing frequency distributions of all words across chapters
    #
    #   param chapterLength : word length of chapters (list)



    ##################################
    # just an idea/misunderstanding?!
    #words = dataFile[[3]]
    #wordOccurrences = dataFile[[4]]
    #uniWords = unique(unlist(words))
    #uniWordOccurrences = vector("list", length=length(uniWords))
    #for(numWord in 1:length(uniWords)){
    #    sumWord = 0
    #    for(numChapter in grep(uniWords[numWord], words)){
    #        sumWord = sumWord + as.numeric(wordOccurrences[[numChapter]][grep(uniWords[numWord], words[numChapter])])
    #    }
    #    uniWordOccurrences[numWord] = sumWord
    #    print(uniWordOccurrences[numWord])
    #    print(uniWords[numWord])
    #}


    pdf(file="../../WORK/Blatt2/2-2-histAllFrequency.pdf")

    chapterLength = dataFile[[2]]

    freqDist = chapterLength/sum(chapterLength)

    barplot(freqDist,
        main="Histogram of frequency distribution of all words (chapter length).",
        xlab="Chapters (1...134)"
    )

    dev.off()
}

densityOne = function(averageWord, specWord){

    #Plot the density of the number of times a word occurs
    #
    #   param averageWord: (list)
    #   param specWord: (str)

    pdf(file="../../WORK/Blatt2/2-3-densityOneWord.pdf")

    chapterWordOccurrence = as.vector(averageWord[[1]])

    plot(c(1:134), chapterWordOccurrence,
        type="l",
        main=paste("Density curve of \"",specWord,"\" over all chapters.", sep=""),
        xlab="Chapters",
        ylab="Occurrence"
    )

    dev.off()
}

insignificantWord = function(dataFile){
    #Try to find a strategy to filter out words that are of little indication to a chapter’s subject matter. That
    #means that they do not carry relevant information. Use your strategy to create a list of words that should
    #be excluded from data analysis.

    #i suggest, if the word occurres less in the chapter, it is probably insignificant:

    chapter = dataFile[[1]]
    chapterLength = dataFile[[2]]
    words = dataFile[[3]]
    wordOccurrences = dataFile[[4]]

    outFile = file("./2-exclude-words.txt", "a")

    for(numChapter in 1:length(chapter)){
        write(unlist(lapply(chapter[[numChapter]], paste, collapse=" ")),
            outFile,
            append=TRUE
        )
        write(unlist(lapply(words[[numChapter]][grep("[1234]", wordOccurrences[[numChapter]])], paste, collapse=",")),
            outFile,
            append=TRUE
        )
    }

    close(outFile)

}

insignificantWord = function(dataFile){
    #Try to find a strategy to filter out words that are of little indication to a chapter’s subject matter. That
    #means that they do not carry relevant information. Use your strategy to create a list of words that should
    #be excluded from data analysis.

    #i suggest, if the word occurres less in the chapter, it is probably insignificant:

    chapter = dataFile[[1]]
    chapterLength = dataFile[[2]]
    words = dataFile[[3]]
    wordOccurrences = dataFile[[4]]

    outFile = file("./2-exclude-words.txt", "a")

    for(numChapter in 1:length(chapter)){
        write(unlist(lapply(chapter[[numChapter]], paste, collapse=" ")),
            outFile,
            append=TRUE
        )
        write(unlist(lapply(words[[numChapter]][grep("[1234]", wordOccurrences[[numChapter]])], paste, collapse=",")),
            outFile,
            append=TRUE
        )
    }

    close(outFile)

}

myData = importData("../../WORK/Blatt2/moby-dick.csv")

specWord = ""

averageWord = averageWordOccurence(myData, specWord)

histOneFrequency(averageWord, myData[[2]], specWord)

histAllFrequency(myData)

densityOne(averageWord, specWord)

insignificantWord(myData)

#warnings()