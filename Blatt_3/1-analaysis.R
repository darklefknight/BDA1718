library(ggplot2)
data(diamonds)
summary(diamonds)

#Preperations:
#Make the cut correlateable:
diamonds_cut = diamonds["cut"]
for (i in c(0:nrow(diamonds_cut))){
  val = diamonds_cut[i,1]
  if (val == "Good"){
    print(val)
  }
}

#Correlations:
carat_cor = cor(diamonds["price"],diamonds["carat"])
cut_cor = cor(diamonds["price"],diamonds["cut"])
color_cor = cor(diamonds["price"],diamonds["color"])
clarity_cor = cor(diamonds["price"],diamonds["clarity"])
depth_corr = cor(diamonds["price"],diamonds["depth"])