# Questão 1

Essa é a resposta para a primeira questão.

## "A tabela de dados não aparece mais no HTML retornado"

Esse caso parece muito uma questão de: "Os dados estão sendo requisitados do lado do cliente". Isso quer dizer que:

- Antes, provavelmente os dados eram requisitados do lado do servidor e o HTML era enviado direto com a tabela, sem necessidade do `fetch` do lado do cliente (navegador do usuário).
- Agora, parece que o navegador precisa fazer o `fetch` dos dados e após o fetch acontecer (2 segundos de espera), atualizar a tela com os dados da tabela.

O que eu utilizaria para contornar essa situação seria a biblioteca `selenium`, pois esta biblioteca me dá a liberdade de controlar o navegador do usuário com código python. Então o que eu faria seria:

- Instalaria a lib `selenium`
- Entraria no site específico com o navegador de preferência
- Utilizaria função de `wait` que vem do próprio `selenium` para esperar a tabela aparecer na tela
- Quando a tabela aparecesse, eu faria a raspagem dos dados e trataria da forma que for necessária para melhor utilização de acordo com o contexto do domínio

## "Após testar algumas vezes, o site começou a retornar 403"

O status code `403` tem haver com **falta de autorização**.

A primeira coisa que eu faria seria descobrir o motivo pelo qual estou recebendo esse status code, porque existem algumas possibilidades do porque a requisição pode estar falhando. No contexto do erro `403`, duas possibilidades são:

- Token de autorização para acesso ao servidor não é mais válido, seja um Bearer token, session token, entre outros
- Fiz muitas requisições, por isso o IP foi bloqueado temporariamente ou de forma permanente

No caso de ser problema no token de autorização, eu criaria uma função que verificaria o erro `403`, e quando acontecesse, acharia uma forma de fazer o **refresh** desse token, revalidar ele para continuar fazendo requisições.

Caso seja o erro de bloqueio de IP, utilizaria uma estratégia de proxy rotativo, pois mudaria o IP a todo momento e o bloqueio de IP deixaria de ocorrer. Inclusive isso é possível de fazer utilizando `selenium`.

## Conclusão

Dessa forma, eu solucionaria o problema do código trazendo soluções que se adequam ao escopo do problema descrito.
