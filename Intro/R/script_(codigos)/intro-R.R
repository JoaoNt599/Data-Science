
# Esse Script pertence ao Curso de Introdução ao R da Beta Analítica
# Autor : Huriel Ruan Reichel



######## Sintaxe em R: carregar e ler dados e instalar pacotes ########

# 1 : Primeiros passos

# Funções ----> function (argument1 = value1, argument2 = value2, argument)

# Case sensitive ----> S != s

# Warning & Error

# Atribuição / chamando uma função ou objeto
obj <- "carro"
valor = 1

# Dicas : - não use acentos ou espaços
#         - o ponto (.) separa decimais 
#         - não esqueça de fechar os parenteses, chaves e colchetes
#         - no RStudio, use o Ctrl + Enter para executar um comando
#         - Mantenha-se sempre organizado com seus dados!
#         - Função help()

# 1.2 Pacotes
install.packages("cluster")
library(cluster)
require(cluster) #instala se não for encontrado na library (cuidado!)
## *obs : atenção ao versionamento e alocação dos pacotes

# 1.3 Objetos
# Programação Orientada a objetos

# 1.3.1 Vetores
# Numéricos

x <- 100
x

# Caracteres
name <- "Huriel"
name

# Concatenate

x <- c(1, 10 , 100, 1000, 10000)
y <- c(2, 5, 3, 8, 18, 36 ,65 , 688 )
cars <- c("Ford", "Chevrolet", "Volkswagen", "Land Rover", "Fiat")

# Fator
evaluation <- c("good", "very good", "enough", "bad", "very bad")
eval.factor <- factor(evaluation)
eval.factor # note como foi feita a ordem
evel.factor <- factor(evaluation, levels = c("very bad", "bad", "enough", "good", "very good"))
evel.factor
tf <- c(TRUE, FALSE, TRUE, TRUE, FALSE)
class(tf)

# Matriz 
vector1 <- c(2, 3, 5, 6, 8)
vector2 <- c(5, 6, 9, 1, 2)

matrix_by_row <- rbind(vector1, vector2)
matrix_by_row

matrix_by_col <- cbind(vector1, vector2)
matrix_by_col

matrix <- matrix(c(100, 250 , 150, 125, 566, 852, 50, 2, 200, 175, 30, 33, 60, 10, 500), ncol = 5)
matrix

matrix2 <- matrix(c(100, 250 , 150, 125, 566, 852, 50, 2, 200, 175, 30, 33, 60, 10, 500), nrow = 3)
matrix2

# matrizes com vetores de diferentes tipos
char <- c("Wolverine", "Ciclope", "Prof. X", "Besta", "Tempestade")
num <- c(5, 6, 8, 5, 6)

matrix(c(char, num), ncol = 5) # repare o que ocorre com os números

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

# Lista
ls <- list(vector1, matrix, evaluation, olympics)
ls

# EXERCÍCIO 1 
# a - Crie um vetor com dados categóricos
# b - Crie uma matrix 5x5  
# c - Crie uma matrix 6x3
# d - Crie um data.frame 4x3


######## Manipulação de Tabelas ######## 

### Importação e visualização
                                       
# Genérico
setwd("/media/huriel/nebula/C/Geostatistics/R_DATA/BetaAnalitica/intro-r-ba/") #adapte ao seu
                                                                   # diretório de preferência
tab <- read.table("hydranten.csv", sep = ",", header = T)
head(tab)
?read.table()

#write.table(olympics, "olympics.txt", sep = " ")
ol <- read.table("olympics.txt", sep = " ", header = T)
ol

# 2.1 CSV
csv <- read.csv("hydranten.csv", header = T)
head(csv)

csv <- read.table("hydranten.csv", sep = ",", header = T)
head(csv)

# 2.2 Tabela do Excel
install.packages("xlsx") # atenção ao modo via IDE também
library(xlsx) 
excel <- read.xlsx("CPI2015.xlsx", "CPI 2015", header = T, startRow = 2)
head(excel)

# 2.3 Exportando arquivos
write.table(olympics, "olympics.txt", sep = " ", col.names = TRUE)

# EXERCÍCIO 2

# a - Importe a tabela "nypd.csv" de ocorrência de tiros em Nova Iorque
# b - Visualize as primeiras linhas da tabela importada e verifique se ela parece correta.
# c - Exporte a tabela em questão com separação por tabulação 

######## Manipulação de Objetos ######## 

# 3.1 Colchetes[]
set.seed(17)
ex <- runif(30)
ex

ex[3]
ex[15]
ex[1]
ex[30]

# Para Dados bidimensionais
csv[1,] # primeira linha
csv[, ] # primeira coluna
csv[1,] # primeira linha e primeira coluna
csv[23, 4]
csv[1:10, 1:4]                           # 
csv[c(1, 3, 5, 7, 11), ]
csv[1:10, c(1, 3, 5, 7)]

# 3.2 Cifrão $
csv$verlegejahr
csv$ano <- csv$verlegejahr

subset <- csv[which(csv$ano == 2021), ]
head(subset)

# 3.3 Estatística Descritiva 
mean(csv$ano)
mean(csv$ano, na.rm = TRUE)

min(csv$ano, na.rm = T)
max(csv$ano, na.rm = T)

median(csv[, 8], na.rm = T)

summary(csv)
num <- csv[,c(2,5)]
num$oberflur_nummer <- as.numeric(num$oberflur_nummer)
colMeans(num, na.rm = T)
rowMeans(num, na.rm = T)

# EXERCÍCIO 3
# Referente aos dados "nypd.csv" de ocorrência de crimes em Nova Iorque : 
# a - A que tipo de informação a terceira coluna da tabela se refere ?
# b - Crie um novo data frame com apenas as linhas pares da tabela (até a linha 20)
# c - A partir do data frame criado anteriormente (b), crie um novo data frame sub-selecionando as 
# colunas referentes ao horário do crime (OCCUR TIME), a idade da vítima (VIC_AGE_GROUP), o sexo da
# da vítima (VIC_SEX) e o grupo étnico da vítima (VIC_RACE)
# d - Qual a Latitude e Longitude Média dos crimes ocorridos ?
# e - Qual o intervalo temporal dos dados ? 

######## Ordenação, remoção e aleatorização de dados e operações fundamentais

# 4.1 Remoção de dados nulos
is.na(csv[10,])
sum(is.na(csv))
complete <- na.omit(csv)
sum(is.na(complete))
mean(complete$ano)
# * Atenção ao remover NAs !

# 4.2 Listar Objetos
ls()

# 4.3 Remover Objetos
rm(bronze)
ls()

# 4.4 Sequências
seq(from = 0, to = 100, by = 10)
seq(0, 100, 10)
1:10

# 4.4.1 Repetições
rep(27, 13)
rep("R", 19)
rep(c("R", "Python"), times = 3)
rep(c(1,2,3), each=3, times=4)

# 4.5 Gerar Dados Aleatórios
sample(1:10, size = 10) # sem repetição
sample(1:10, size = 10, replace = TRUE) # com repetição

id <- csv$objectid
sample(id, 10)

# 4.6  Ordem
head(csv)
sort(csv$verlegejahr)
sort(csv$verlegejahr, decreasing = T)

order(csv$verlegejahr) # retorna a posição de cada elemento se ordenado
ordered <- csv[sort(csv$verlegejahr),]
head(ordered)

# 4.7 Operações aritméticas
5 + 5
9 - 7
3 * 3
10 / 5
10 %% 3 # modulus
10 %/% 3 # integer division
5 ** 3
10 ** 2 + 5
10 ** (2 + 5)
( (100**2 + 5) * (56*3) ) / (25/9)

csv$delta_year <- csv$verlegejahr - min(csv$verlegejahr, na.rm = T) 
head(csv$delta_year)

# 4.8 Operações lógicas
5 < 3
5 <= 5 
5 > -10
1 >= 0
3 == 3
3 != 3
5 | 3 # OR
3 & 3 # AND
X = TRUE
isTRUE(X)

sum(csv$oberflur_nummer > csv$objectid)

# EXERCÍCIO 4
# a - Remova todas as linhas com dados nulos na tabela nypd.csv
# b - Gere uma sequência de valores entre 0 e 100, em que cada valor da sequência se repita 3 vezes
# (0, 0, 0, 1, 1, 1, 2, 2, 2, ...)
# c - Ordene a sequência de valores criada anteriormente de forma decrescente
# d - Reordene toda a tabela nypd com base no tempo de ocorrência do crime (OCCUR_TIME) 
# e - Calcule a distância entre os pontos mais distantes de occorrências de crimes (Dica : utilize
# as coordenadas projetas - 'X_COORD_ CD' e 'Y_COORD_CD')


######## Criação de gráficos no R ########

# 5.1 Scatterplot
head(swiss)
plot(swiss$Education, swiss$Fertility)

plot(swiss$Education, swiss$Fertility, las = 1)
plot(swiss$Education, swiss$Fertility, las = 1, pch = 19) # pch
plot(swiss$Education, swiss$Fertility, las = 1, pch = 19, col = 'yellow') # colour
plot(swiss$Education, swiss$Fertility, las = 1, pch = 19, col = 'yellow', cex = 2) # size
plot(swiss$Education, swiss$Fertility, las = 1, pch = 19, col = 'yellow', cex = 2, axes = F)

plot(swiss$Education, swiss$Fertility, main = 'Fertility x Education', xlab = 'Education', ylab = 'Fertility')

plot(swiss$Education, swiss$Fertility, xlim = c(0, 30), ylim = c(50, 80))

plot(swiss$Education, swiss$Fertility, xaxt = "n")
axis(1, at = seq(0, 50, 25))

head(iris)
plot(iris[,1:4], col = iris$Species)

# 5.2 Barplot
barplot(iris$Petal.Length)

library(RColorBrewer)
coul <- brewer.pal(5, "Set2")

barplot(olympics$gold, names = olympics$country, col = coul)

# 5.3 Pie (Pizza)
df <- data.frame(title = c("A", "B", "C", "D", "E"), percentage = c(75, 15, 5, 3, 2))
pie(df$percentage, labels = df$title, col = c("green", "blue", "darkgreen", "brown", "khaki"))
pie(df$percentage, labels = df$percentage, col = c("green", "blue", "darkgreen", "brown", "khaki"))

# 5.4 Boxplot
boxplot(swiss)
boxplot(swiss, col = "blue")

brewer.pal.info
pal <- brewer.pal(6, "Set2")
boxplot(swiss, col = pal)
boxplot(swiss, col = pal, range = 1)

# 5.5 Histograma
hist(swiss$Education)
hist(swiss$Education, breaks = 20)

hist(rnorm(1000, 0, 1))

# 5.6 A função "par"
par(col.axis = "brown")
plot(c(5, 3, 5, 6, 0), c(10 ,20, 30, 40, 50))

par(cex = 1.5)
plot(c(5, 3, 5, 6, 0), c(10 ,20, 30, 40, 50))

par(mar = c(2, 2, 2, 1))
plot(c(5, 3, 5, 6, 0), c(10 ,20, 30, 40, 50))

par(mfrow = c(1, 2))
plot(c(5, 3, 5, 6, 0), c(10 ,20, 30, 40, 50))
hist(rnorm(100, 50, 5))

par(mfrow = c(2, 1))
plot(c(5, 3, 5, 6, 0), c(10 ,20, 30, 40, 50))
hist(rnorm(100, 50, 5))

par(mfrow = c(2, 2))
plot(c(5, 3, 5, 6, 0), c(10 ,20, 30, 40, 50))
hist(rnorm(100, 50, 5))
barplot(c(10, 20, 30, 40, 50))
pie(c(10,50,40,30,20,10))

# 5.7 Exportando Figuras
tiff('mygraph.tiff')
hist(swiss$Education)
dev.off()

png('mygraph.png')
hist(swiss$Education)
dev.off()

pdf('mygraph.pdf')
hist(swiss$Education)
dev.off()

