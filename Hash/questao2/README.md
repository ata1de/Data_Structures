# 👨‍💻Equipes do CIN
Marcelo J, líder dos 22 centros da Associação Contabilística Anti-Roubo das Águas do Sertão, está insatisfeito com a sua atual equipe de TI e decidiu investir nos alunos do Cin para aprimorar sua análise de dados. Marcelo deseja fazer uma competição disponível para todos os alunos, alunos esses que podem formar grupos de 1 pessoa à 10 pessoas para participar do projeto dessa competição. Entendendo que muitas pessoas no Cin não possuem amigos, Marcelo convocou você para formar grupos a partir de uma lista de pessoas e suas respectivas preferências de tamanho de grupo.

## Input

Você vai receber uma quantidade indeterminada de linhas no input seguindo esse modelo:
```
<nome_pessoa><tamanho_da_equipe>
```

### Exemplo:
```
Anaju 2

Geydson 2

Gabriel 1

```

No caso do exemplo acima, 'Anaju' deseja participar de um grupo com 2 pessoas, 'Geydson' num grupo de também duas pessoas e Gabriel em um grupo de apenas uma pessoa (ele mesmo).

### OBS
A quantidade de interessados em um determinado tamanho de grupo é sempre divisível pelo tamanho do grupo, ou seja, o número N de pessoas interessadas pelo tamanho de grupo 3 é sempre algum múltiplo de 3, portanto N pode ser 3 pessoas interessadas, 6, 9 e assim por diante.

## Output
O output será uma lista com os grupos formados em ordem crescente pelo tamanho dos grupos e nomes das pessoas de acordo com a ordem alfabética (A é menor que D), Exemplo:

### Input:

Vina 1

Ana 1

Geydson 2

Gabriel 2

Bruno 2

Marcelo 2

### Output:
 [['Ana'], ['Vina'], ['Bruno', 'Gabriel'], ['Geydson', 'Marcelo']]

**IMPORTANTE: UTILIZAR HASH TABLE COM LISTA ENCADEADA PARA TRATAR AS REPETIÇÕES** 

### OBS
Não pode utilizar dicionário