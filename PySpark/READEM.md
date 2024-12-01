#  Apache Spark e PySpark


## O Apache Spark é uma ferramenta poderosa para processamento distribuído de dados, enquanto o PySpark é a integração do Spark com Python, facilitando seu uso para cientistas de dados e desenvolvedores Python.

### Principais características do Apache Spark:

1. Velocidade: Processa dados em memória, reduzindo a latência.
2. Escalabilidade: Pode ser executado em pequenos clusters locais ou em grandes clusters em nuvem.
3. Versatilidade: Suporta diversas APIs para diferentes linguagens (Java, Scala, Python, R) e bibliotecas como Spark SQL, MLlib, GraphX e Spark Streaming.


### Com PySpark, é possível:

1. Manipular e transformar grandes volumes de dados usando DataFrames e RDDs.
2. Realizar consultas SQL com o Spark SQL.
3. Criar modelos de aprendizado de máquina com MLlib.
4. Processar fluxos de dados em tempo real com Spark Streaming.



## Componentes


## Spark Application = Contrução da aplicação via Spark

### Spark Driver

1. Inicializa o Spark Session
2. Utiliza recursos como: CPU, Memória
3. Gera um ambiente para executar o processos do Spark

### Spark Session

1. É uma entrada uificada para os recursos do Spark
2. Parametrização de JVM
3. Realiza criação de Dataframes
4. Leitura de fonte dados


## Dataframe

### É uma estrutura de dados tabular amplamente usada em bibliotecas de ciência de dados, como Pandas e PySpark. Ele organiza os dados em formato de tabela, com linhas e colunas, semelhante a uma planilha ou tabela em um banco de dados.

### Características principais de um DataFrame:

1. Estruturado: Cada coluna possui um nome e um tipo de dado, como int, string, etc.
2. Imutável: No caso de bibliotecas como PySpark, as alterações geram novos DataFrames em vez de modificar o original.
3. Distribuído: Em PySpark, os DataFrames são processados em cluster, permitindo lidar com grandes volumes de dados.
4. Rico em Operações: Suporta filtros, agrupamentos, agregações, junções e outras transformações complexas.


## Cluster Manager


### Gerenciamento de alocação de recursos para o cluster

1. Cluster manager standalone
2. Apache Hadoop YARN
3. Apache Mesos
4. Kubernetes


### Spark Executor

1. Realizar execução das tasks
2. Pode possuir vários cores de processamento 


### Spark Jobs

1. Cada ação possui um Job
2. Ação é um processamento que retorna resultados
3. Job pode possuir um ou mais Stages


### Spark Stages

1. Um Job é dividido por conjuntos menores de tasks, ou por Stages


### Spark Task

1. Um processo de execução unitário que pode variar dependendo dos executores disponíveis 