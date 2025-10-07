# install.packages("GA")
library(GA)

# fitness function
f <- function(x) {
  resultado = 2 * x + 5
  return(-abs(resultado - 20))  # GA maximizes. Use negative value
}

# genetic algorithm
resultado = ga(
  type = "real-valued",
  fitness = f,
  lower = -100,
  upper = 100,
  popSize = 10,
  maxiter = 10,
  monitor = TRUE
)

# results
summary(resultado)
summary(resultado)$solution
plot(resultado)

