# Challenge Suzano
[![Build Status](https://travis-ci.org/lserra/challenge_boa.svg?branch=source)](https://travis-ci.org/lserra/challenge_boa)

Challenge for a Vacancy at Suzano

#### Problema

Atualmente um dos nossos desafios é criar serviços de dados escaláveis, otimizados
para o armazenamento e para o acesso aos dados.

Nossos Analistas examinaram os dados de fluxo de pessoas e concluíram que a melhor
forma de apresentar essa informação seria segmentando o fluxo por dias da semana e
períodos do dia (manhã, tarde e noite), ou seja, os clientes precisam saber quantas
pessoas em média frequentam seus concorrentes em cada dia da semana e em cada período
do dia.

Para encontrar fluxo médio de pessoas é preciso considerar os eventos dos mesmos dias
da semana e dos mesmos períodos do dia.

A densidade demográfica de um bairro é uma informação muito importante para nossos
clientes e é uma informação que precisa ser calculada. A densidade demográfica de
um bairro é o resultado da  divisão da população do bairro pela área do bairro.

#### Objetivo

Com o conhecimento sobre os dados que você irá trabalhar e regras mencionadas,
agora você precisa construir uma aplicação que calcule e apresente as informações
dos concorrentes como código, nome, endereço, preço praticado, fluxo médio de
pessoas por dia da semana e por período do dia, bairro e a população e a
densidade demográfica do bairro.

## Conhecendo os Dados (Exploratory Data Analysis)

Análise exploratória dos dados usando o `Python/Pandas`.

O script usado para gerar os relatórios, pode ser encontrado na pasta: `/src/analysis/eda.py`.

Para gerar os relatórios, basta executar os comandos abaixo:

```shell script
$ cd challenge_suzano
$ bash eda.sh
```

E os relatórios em formato HTML, podem ser encontrados na pasta: `/output/analysis`.

## Modelagem dos Dados

Esta informação está disponível no arquivo compartilhado [aqui](https://docs.google.com/presentation/d/1Ue3UEnxKsFxKq2cuXtrF95LHJCnZdjg7XbyTOcf79Lc/edit?usp=sharing).

Na pasta `/db` está disponível o banco de dados SQLite com as tabelas criadas a
partir dos arquivos CSV/JSON fornecidos.

## Como Executar e Monitorar o Processo

- Para executar a aplicação é necessário ter instalado na máquina o Python (3.7)
  ou mais recente. Execute o comando abaixo para verificar a versão do python instalado
  na sua máquina:

```shell script
$ python --version
```

Além disso, será necessário instalar algumas bibliotecas.
Para instalar todas as bibliotecas necessárias, basta executar os comandos abaixo:  

```shell script
$ cd challenge_suzano
$ pip3 install -r requirements.txt
```

Para executar a aplicação, basta executar os comandos abaixo.

```shell script
$ cd challenge_suzano
$ bash start.sh
```

Para executar a aplicação usando o Docker, é necessário que você tenha
  o Docker instalado na sua máquina.
  Para verificar se você possui o Docker instalado, basta digitar o seguinte comando:

```shell script
$ docker --version
```

Em seguida, você deve executar o comando abaixo no mesmo diretório em que se encontra o Dockerfile.

```shell script
$ cd challenge_suzano
$ docker build -t lserra/de_suzano:latest . 
```

## Relatórios EDA

- [Bairros](output/analysis/bairros.html)
- [Concorrentes](output/analysis/concorrentes.html)

## Estutura de Pastas e Arquivos do Projeto

    challenge_suzano
        |__ /db             => banco de dados SQLite 
        |__ /input          => dados de origem
        |__ /output
        |______ /analysis   => resultado da análise exploratória dos dados
        |______ /json       => resultado da consulta (JSON)
        |__ /sql            => scripts SQL
        |__ /src            => scripts Python
        |__ README.md       => documentação do projeto
        |__ eda.sh          => shell script dos relatórios de exploração
        |__ start.sh        => shell script de execução deste projeto

## Agradecimentos

Agradeço a oportunidade de poder participar deste processo.

Segue abaixo outras referências do meu trabalho e coloco-me a disposição de todos
para os esclarecimentos que forem necessários.

GitHub:

- [My Personal Blog](https://lserra.github.io/)
- [B2W](https://github.com/lserra/challenge_b2w)
- [ContaAzul](https://github.com/lserra/challenge_ca)
- [AWS EMR](https://github.com/lserra/BrodAI)
- [Diversos](https://github.com/lserra/blog_da/tree/master/notebooks)

THANK YOU !!! 🍺🍺
