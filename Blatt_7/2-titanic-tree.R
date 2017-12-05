library(rpart)

dTitanic = read.csv("/home/finn/Schreibtisch/Studium/17_WiSe/BigDataAnalytics/WORK/Blatt7/titanic.csv", header=T, sep=",", quote="\"")

colnames(dTitanic)[1] = "Num"

# Create a decision tree 
m = rpart(Survived ~ Class, data=dTitanic, method="class",
          control = rpart.control(minsplit=5, cp = 0.05))