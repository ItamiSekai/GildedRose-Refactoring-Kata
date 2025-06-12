# Mini Relatório - Gilded Rose - Refatoração
### Nome: Gabriel Gomes Nogueira (GU3055361)    Nome: Samuel Vitalino Leite (GU3056457)
### Disciplina: Engenharia de Software

## Descrição da atividade

Este projeto consiste em realizar a refatoração do código original do sistema Gilded Rose, que gerencia o estoque de uma loja com diversos tipos de itens. O código original apresentava uma função update_quality com diversas condições aninhadas e de difícil manutenção. O objetivo foi tornar o código mais claro, modularizado e fácil de entender, além de implementar a regra adicional para os itens Conjured.

## Processo de refatoração
As principais mudanças realizadas foram:

- Separação do comportamento por tipo de item dentro do método update_item_quality, alterando o item conforme o necessário, retirando todos aqueles "if" desnecessários. Deixando mais simples e legível, dividindo em pequenos métodos. Como estes abaixo.

Criação de métodos auxiliares para cada comportamento específico:

- update_aged_brie

- update_backstage_pass

- update_conjured_item

- update_normal_item

Criação dos métodos utilitários:

- increase_quality

- decrease_quality

Implementação da regra para Conjured:

- Itens cujo nome começa com "Conjured" passam a perder qualidade duas vezes mais rápido que os itens normais. Assim como havia sido descrito na atividade.

Preservação das regras gerais do sistema:

- Qualidade mínima = 0

- Qualidade máxima = 50 (exceto Sulfuras, que é fixo)


## Dificuldades encontradas

- Manter o código organizado e fácil de entender, mesmo com a necessidade de múltiplas regras. O que gerou uma certa confusão no começo, por ter que dividir em algumas funções, mas que de forma geral fica mais intuitiva e mais fácil de entender.

- Ler o código e entender antes de refatorar. Todos aqueles "if" acabaram confundindo bastante no geral, principalmente para entender a lógica geral. No fim acabou sendo mais simples apagar tudo e fazer novamente.

## Lições aprendidas
- A importância de separar claramente as responsabilidades no código, facilitando manutenção futura. Deixando que cada método tenha uma função principal, sem que faça várias coisas ao mesmo tempo e deixe o código ainda maior.

- Métodos auxiliares. Eles ajudam a manter o código mais simples e legível, sem falar coma sua reutilização. Ao invés de refazer sempre a mesma parte de código é apenas chamar a função, como increase_quality, é fácil entender o que vai acontencer após eu usar ele. E caso precise usar mais de uma vez é apenas usar a função novamente.

- A importância de garantir que todos os casos sejam bem tratados. Respeitando todas as regras implementadas, fazerem funcionar da maneira correta.
