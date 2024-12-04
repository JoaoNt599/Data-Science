# EXERCÍCIO 1 

# a - Crie um vetor com dados categóricos

categorias <- factor(c("Baixo", "Médio", "Alto", "Médio", "Baixo"))

levels <- c("Baixo", "Médio", "Alto")

print(categorias)

# Verifica se é ordenado
is.ordered(categorias)

levels(categorias)

# Criando um gráfico de barras
barplot(table(categorias), 
        col = c("blue", "yellow", "red"),
        main = "Distribuição de Categorias")



# b - Crie uma matrix 5x5 

matriz1 <- matrix(1:25, nrow = 5, ncol = 5, byrow = TRUE)

print(matriz1)


# c - Crie uma matrix 6x3

matriz2 <- matrix(sample(1:100, 18), nrow = 6, ncol = 3)

print(matriz2)


# d - Crie um data.frame 4x3

dados <- data.frame(
  ID = c(1, 2, 3, 4),
  CATEGORIA = c("A", "B", "C", "D"),
  STATUS = c(TRUE, FALSE, TRUE, FALSE),
  VALOR = c(10.5, 20.3, 15.8, 12.7)
)

print(dados)









