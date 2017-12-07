library(knitr)
library(markdown)
library(rpart)
library(rpart.plot)
library(plyr)
library(ggplot2)

# Import data
dTitanic = read.csv("/home/finn/Schreibtisch/Studium/17_WiSe/BigDataAnalytics/WORK/Blatt7/titanic.csv",
                    header=T,
                    sep=",",
                    quote="\"")

colnames(dTitanic)[1] = "Num"

dTitanic$Survived = gsub("No", "died", dTitanic$Survived)
dTitanic$Survived = gsub("Yes", "survived", dTitanic$Survived)

# Create one training dataset
#mask = sample(2, nrow(dTitanic), repl=T, prob=c(0.9,0.1))
#validation = dTitanic[mask==1, ]
#training = dTitanic[mask==2, ]

set.seed(123)

# create 10 folds
folds = split(dTitanic, cut(sample(1:nrow(dTitanic)),10))
errs = rep(NA, length(folds))
errFP = rep(NA, length(folds))
errFN = rep(NA, length(folds))

for (i in 1:length(folds)) {
 validation = ldply(folds[i], data.frame)
 training = ldply(folds[-i], data.frame)

 m = rpart(Survived ~ Age+Class+Sex,
          data=training,
          method="class")

 p = predict(m,
             newdata = validation,
             type = "class")

 confmat = table(validation$Survived, p)

 # Compute the error rate of the predictions
 errs[i] = 1-sum(diag(confmat))/sum(confmat)
 errFN[i] = sum(confmat[2,1])/sum(confmat)
 errFP[i] = sum(confmat[1,2])/sum(confmat)
}

rpart.plot(m,
           extra=104, box.palette="GnBu",
           branch.lty=3, shadow.col="gray", nn=TRUE)


# evaluate the accuracy of your decision tree
print(sprintf("average error using k-fold cross-validation: %.3f percent", 100*mean(errs)))


# Create data
dataFN=data.frame(folds=seq(1,10), errorFalseNegative=errFN)
dataFP=data.frame(folds=seq(1,10), errorFalsePositive=errFP)

plot = ggplot() +
  geom_line(data=dataFN, aes(x=folds, y=errorFalseNegative, colour="FalseNegative")) +
  geom_line(data=dataFP, aes(x=folds, y=errorFalsePositive, colour="FalsePositive")) +
  scale_color_manual(values = c(FalseNegative="red", FalsePositive="blue")) +
  labs(color="Indices") +
  xlab("folds") +
  ylab("error") +
  ggtitle("Computation of the error rate of the predictions")

plot