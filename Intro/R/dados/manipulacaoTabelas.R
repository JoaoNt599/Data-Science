
# CSV
setwd("C:/Users/joaon/Desktop/Python/DS Github/Intro/R/dados")

tab <- read.table("hydranten.csv", sep = ",", header = T)
head(tab)
?read.table()

ol <- read.table("olympics.txt", sep = " ", header = T)
ol

csv <- read.csv("hydranten.csv", header = T)
head(csv)

csv <- read.table("hydranten.csv", sep = ",", header = T)
head(csv)



# Excel
install.packages("xlsx")

library(xlsx) 

excel <- read.xlsx("CPI2015.xlsx", "CPI 2015", header = T, startRow = 2)

head(excel)


# Data Frame
country <- c('USA', 'China', 'Japan', 'UK', 'Russia', 'Australia')
gold <- c(39, 38, 27, 22, 20, 17)
silver <- c(41, 32, 14, 21, 28, 7)
bronze <- c(33, 18, 17, 22, 23, 22)

olympics <- data.frame(country, gold, silver, bronze)
olympics

olympics <- data.frame(
  country = c('USA', 'China', 'Japan', 'UK', 'Russia', 'Australia'),
  gold = c(39, 38, 27, 22, 20, 17),
  silver = c(41, 32, 14, 21, 28, 7),
  bronze = c(33, 18, 17, 22, 23, 22)
)
olympics    

olympics <- data.frame(country, gold, silver, bronze)

write.table(olympics, "olympics.txt", sep = " ", col.names = TRUE)




