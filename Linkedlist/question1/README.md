# 💎 À procura da Esmeralda Secreta

Em uma terra distante, havia dois irmãos gêmeos exploradores de dados chamados Dwayne Johnson e The Rock, que se aventuravam em uma floresta misteriosa chamada Cinlândia, uma floresta de dados encantados. Eles estavam em busca da lendária "Esmeralda Secreta", uma joia preciosa que detinha todo o conhecimento do universo.

A jornada dos irmãos começou quando eles encontraram um mapa antigo, que indicava a presença de grandes desafios ao longo do caminho. O mapa revelava que para chegar à poderosa Esmeralda, eles teriam que superar obstáculos utilizando seus conhecimentos sobre estruturas de dados.

Ao adentrar a floresta, Dwayne e The Rock depararam-se com um enigma deixado pelos guardiões da floresta, seres sábios que protegiam a preciosa Esmeralda. O enigma consistia em uma série de tarefas relacionadas às estruturas de dados.

The Rock encontrou uma misteriosa espécie de criatura chamada Node que emitia uma luz radiante. Cada Node possuía um número gravado e uma instrução. O desafio era criar um caminho que interligava os Nodes de modo que ao final, depois de seguir todas as instruções, fosse formado um holograma do mapa que o levaria a Esmeralda Secreta.

## Instruções
- `Empurre-me!` - move o Node para uma posição à direita do caminho;

- `Puxe-me!` - move o Node para uma posição à esquerda do caminho;

- `Remova-me!` - remove o Node do caminho;

- `Adicione-me!` - adiciona o Node ao final do caminho;

- `Fim!` - última pedra do caminho.

## Atenção
```
ATENÇÃO!!! Responder usando lista encadeada simples e Está proibido o uso de bibliotecas
```

### Inputs
o Input será um número seguido de dois pontos (:), depois a instrução e sem espaços!!!

Exemplo:

- 1:adicione-me!

- 2:adicione-me!

- 2:remova-me!

- 3:adicione-me!

- 4:adicione-me!

- 1:empurre-me!

- 6:empurre-me!

- 4:empurre-me!

- 3:puxe-me!

- fim!

### Output
A cada instrução realizada, deverá ser printado "Node" + número que foi especificado + instrução realizada
```
"Node {num} [instrução]"
```

Quando o input for "fim!", deverá ser printado "mapa:" + números organizados separados por um hífen (-) e maior que (>), sem espaço.
```
"mapa:1->2->3"
```

Caso um Node seja especificado para realizar alguma instrução e ele não exista, deverá ser printado:
```
"Node {num} não existe"
```

Caso seja pedido para que um Node seja empurrado, mas não tem mais nenhum outro depois dele, isto é, ele é o último do caminho, deverá ser printado:
```
"Não existe Node depois de {num}"
```

Caso seja pedido para que um Node seja puxado, mas não tem mais nenhum outro antes dele, isto é, ele seja o primeiro do caminho, deverá ser printado:
```
"Não existe node antes de {num}"
```

