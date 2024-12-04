# Referente aos dados "nypd.csv" de ocorrência de crimes em Nova Iorque : 

# a - A que tipo de informação a terceira coluna da tabela se refere ?

setwd("C:/Users/joaon/Desktop/Python/DS Github/Intro/R/dados")
tab <- read.table("nypd.csv", sep = ",", header = T)
tab
tab[,3]

# b - Crie um novo data frame com apenas as linhas pares da tabela (até a linha 20)

df <- tab[c(2, 4, 6, 8, 
            10, 12, 14, 
            16, 18, 20),]
df

# c - A partir do data frame criado anteriormente (b), crie um novo data frame sub-selecionando as 
# colunas referentes ao horário do crime (OCCUR TIME), a idade da vítima (VIC_AGE_GROUP), o sexo da
# da vítima (VIC_SEX) e o grupo étnico da vítima (VIC_RACE)

head(df)
subset <- df[,c(3, 12:14)]
subset

# d - Qual a Latitude e Longitude Média dos crimes ocorridos ?

colnames(df)
mean(df$Latitude)
mean(df$Longitude)
mean(df$Y_COORD_CD)
mean(df$X_COORD_CD)

# e - Qual o intervalo temporal dos dados ? 

min(df$OCCUR_DATE)
max(df$OCCUR_DATE)

class(df$OCCUR_DATE)


