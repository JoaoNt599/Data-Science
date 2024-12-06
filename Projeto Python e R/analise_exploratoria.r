# 1. Configuração Inicial

install.packages("ggplot2")
install.packages("dplyr")
install.packages("forecast")

library(ggplot2)
library(dplyr)
library(forecast)

dados <- read.csv("C:/Users/joaon/Desktop/Python/DS Github/Projeto Python e R/data/resultados_d20.csv")


# 2. Análise Estatística

# Amostragem - Pegando uma amostra de 10 rolagens
amostra <- sample(dados$Resultado, size = 10, replace = FALSE, prob = NULL)
print(paste("Amostra:", amostra))


# Probabilidade - Probabilidade de cada valor aparecer
probabilidades <- table(dados$Resultado) / nrow(dados)
print(paste("Probabilidades:", probabilidades))


# Media
media <- mean(dados$Resultado, na.rm=FALSE)
print(paste("Media:", media))

# Mdiana 
mediana <- median(dados$Resultado)
print(paste("Mediana:", mediana))

# Moda
moda <- as.numeric(names(sort(table(dados$Resultado), decreasing = TRUE)[1]))
print(paste("Moda:", moda))


# Média Ponderada
pesos <- rep(1, length(dados$Resultado)) # pesos iguais
media_ponderada <- sum(dados$Resultado * pesos) / sum(pesos)
print(paste("Media Ponderada:", media_ponderada))


# Outliers - Usando IQR
iqr <- IQR(dados$Resultado)
limite_inferior <- quantile(dados$Resultado, 0.25) - 1.5 * iqr 
limite_superior <- quantile(dados$Resultado, 0.75) + 1.5 * iqr

outliers <- dados$Resultado[dados$Resultado < limite_inferior | dados$Resultado > limite_superior]
print(paste("Outliers:", outliers))


# 3. Visualizações

# Histograma
ggplot(dados, aes(x = Resultado)) +
  geom_histogram(binwidth = 1, fill = "blue", color = "black") +
  labs(title = "Distribuição dos Resultados", x = "Resultado", y = "Frquência")

# Histograma personalizado

# Definir as cores personalizadas 
cores <- c(
  "1" = "red", "2" = "blue", "3" = "green", "4" = "purple", "5" = "orange",
  "6" = "pink", "7" = "yellow", "8" = "cyan", "9" = "brown", "10" = "lightgreen",
  "11" = "gray", "12" = "magenta", "13" = "lightblue", "14" = "violet", 
  "15" = "indianred", "16" = "gold", "17" = "turquoise", "18" = "salmon", 
  "19" = "peachpuff", "20" = "plum"
)

# Criar o histograma para os valores rolados
ggplot(dados, aes(x = Resultado, fill = as.factor(Resultado))) +
  geom_histogram(
    binwidth = 1,  # Define o intervalo de cada barra (1, os valores vão de 1 a 20)
    color = "black",
    boundary = 0.5  # Ajusta o limite da barra 
  ) +
  scale_fill_manual(values = cores) +  
  labs(
    title = "Histograma dos Valores Rolados",
    x = "Valor Rolado",
    y = "Frequência"
  ) +
  theme_minimal()


# Boxplot
ggplot(dados, aes(y = Resultado)) +
  geom_histogram(fill = "orange") +
  labs(title = "Boxplot dos Resultados", y = "Resultados")


# Pizza
frequencias <- table(dados$Resultado)

# Cria um gráfico de pizza
pie(
  frequencias,
  labels = paste(names(frequencias), "(", frequencias, ")", sep = ""),
  main = "Frequência dos Valores Rolados (1 a 20)",
  col = rainbow(length(frequencias)) 
)


# Preparar os dados para o gráfico
frequencias <- as.data.frame(table(dados$Resultado))
colnames(frequencias) <- c("Valor", "Frequencia")

# Adicionar porcentagens ao dataset
frequencias$Porcentagem <- round((frequencias$Frequencia / sum(frequencias$Frequencia)) * 100, 1)

# Gráfico de pizza personalizado
ggplot(frequencias, aes(x = "", y = Frequencia, fill = as.factor(Valor))) +
  geom_bar(stat = "identity", width = 1) +
  coord_polar(theta = "y") +
  labs(
    title = "Frequência dos Valores Rolados (1 a 20)",
    fill = "Valor"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_blank(), axis.ticks = element_blank(), panel.grid = element_blank()) +
  geom_text(aes(label = paste0(Porcentagem, "%")), position = position_stack(vjust = 0.5))



# Gráfico de Rosca personalizado

# Preparar os dados para o gráfico
frequencias <- as.data.frame(table(dados$Resultado))
colnames(frequencias) <- c("Valor", "Frequencia")

# Adicionar porcentagens ao dataset
frequencias$Porcentagem <- round((frequencias$Frequencia / sum(frequencias$Frequencia)) * 100, 1)

# Criar o gráfico de rosca
ggplot(frequencias, aes(x = 2, y = Frequencia, fill = as.factor(Valor))) +
  geom_bar(stat = "identity", width = 1) +
  coord_polar(theta = "y") +
  xlim(1, 2.5) +  # Ajustar o tamanho do "buraco"
  labs(
    title = "Frequência dos Valores Rolados",
    fill = "Valor"
  ) +
  theme_void() +  # Remove os eixos
  theme(legend.position = "right") +
  geom_text(aes(label = paste0(Porcentagem, "%")), position = position_stack(vjust = 0.5))



# 4. Predição das próximas 10 rolagens
modelo <- auto.arima(dados$Resultado)

# Prevendo as proximas 10 rolagens
previsoes <- forecast(modelo, h = 10)
print(paste("Previsões:", previsoes))

# Plotando as previsões
autoplot(previsoes) +
  labs(title = "Predição das Próximas 10 Rolagens", x = "Rolagens Futuras", y = "Resultado")
