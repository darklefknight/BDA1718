# Exploration of the IRIS Data Set

data(iris)

summary(iris)

# Draw a matrix of all variables
pdf(file="../../WORK/Blatt2/1-1-summary.pdf")
plt1 = plot(iris[,1:4], col=iris$Species, main="Summary")
dev.off()

# Density estimation of Petal.Length
pdf(file="../../WORK/Blatt2/1-2-density.pdf")
d = density(iris$Petal.Length, bw="SJ", kernel="gaussian")
plot(d, main="Density estimation of Petal Length")
dev.off()

# Histogram of petal length
pdf(file="../../WORK/Blatt2/1-3-histogram.pdf")
hist(iris$Petal.Length, nclass=25, main="Petal length")
dev.off()

# correlation
cor(iris[,1:4])

#sources:
#https://rstudio-pubs-static.s3.amazonaws.com/204918_d5ccf842cbc540e78b3d6d3287e6ad38.html