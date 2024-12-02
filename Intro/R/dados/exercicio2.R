# a - Importe a tabela "nypd.csv" de ocorrência de tiros em Nova Iorque

setwd("C:/Users/joaon/Desktop/Python/DS Github/Intro/R/dados")
tab <- read.table("nypd.csv", sep = ",", header = T)


# b - Visualize as primeiras linhas da tabela importada e verifique se ela parece correta.

head(tab, 10)
tail(tab, 6)
?read.table()


# c - Exporte a tabela em questão com separação por tabulação

write.table(tab,"nypd_tab.txt", sep = "\t", col.names = TRUE)
read.table("nypd_tab.txt", sep = "\t", header = TRUE)


