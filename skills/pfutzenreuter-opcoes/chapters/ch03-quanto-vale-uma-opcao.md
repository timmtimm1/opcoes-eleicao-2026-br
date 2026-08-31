# Capítulo 3: O preço de casar com Raquel — quanto vale uma opção?

## Core Idea
Toda avaliação de opção se apoia na mesma ideia: simular cenários para o ativo subjacente, calcular a probabilidade de cada um, calcular o lucro da opção em cada cenário e tirar a **média ponderada pelas probabilidades**. Esse é o "valor justo".

## Frameworks Introduced
- **Método da média ponderada (bilhete de loteria)**:
  1. Simular cenários para o spot no vencimento.
  2. Probabilidade de cada cenário.
  3. Lucro da opção em cada cenário (valor intrínseco).
  4. Média ponderada = valor justo.
  - Ex.: PETR $50, call strike $50, 2 meses. Sobe 10% → intrínseco $5; cai 10% → $0. Chances iguais → opção vale $2,50.
- **Carteira replicante (delta)**: montar com ativos simples (empréstimo + ação) algo que pague o mesmo que a opção.
  - Call ITM strike $100, spot $102: tomar $100 emprestado + $2 do bolso, comprar $102 em ações. **Delta = proporção de ações comprada vs. montante emprestado.** Delta 100% = cada $1 de spot move $1 na carteira; delta 50% = move $0,50.
  - Carteira replicante é teórica: precisa reajuste diário, custos de corretagem enormes.
- **Impacto das variáveis no prêmio** (Tabela 3.1):

| Variável sobe | Call | Put |
|---|---|---|
| Spot | ↑ | ↓ |
| Strike | ↓ | ↑ |
| Prazo até vencimento | ↑ | ↑ |
| Taxa de juros | ↑ | ↓ |
| Volatilidade | ↑ | ↑ |
| Dividendos pagos | ↓ | ↑ (mas BOVESPA é protegida) |

## Key Concepts
- **Preço de mercado é soberano**: se avaliação ≠ mercado, é muito mais provável erro de avaliação do que distorção de mercado. Perigoso especular contra "distorções".
- **Opções reais**: avaliar ativos com cara de opção (empresa falimentar com patrimônio negativo, terreno baldio, jazida com prazo longo) como se fossem opções — valor = expectativa de evento futuro positivo descontada.

## Worked Example
Impacto da taxa de juros na call: você tem call PETRA50, planeja gastar $50 em janeiro (já tem o dinheiro). Se o juro sobe, você aplica os $50 na renda fixa e no vencimento tem $50 + juro extra → a call deu mais lucro que o esperado → **juro maior aumenta a call**. Já na put PETRM50 você tem garantia de receber $50 em janeiro; juro maior derruba o valor presente desses $50 → **juro maior diminui a put**.

## Anti-patterns
- **Usar análise técnica/fundamentalista para decidir a opção**: mesmo que Petrobrás esteja "barata", o mercado precisa concordar E os preços subirem ANTES do vencimento. Não dá para esperar *ad infinitum*.
- **Candlestick na própria opção**: o máximo que descobre é que a opção desvaloriza perto do vencimento.

## Key Takeaways
1. Valor justo = média dos desfechos ponderada por probabilidade.
2. O delta nasce aqui: proporção da carteira replicante.
3. Assuma que o mercado é eficiente e o preço é "correto" — pelo menos para opções.
4. Ficar de fora também é uma opção válida de investimento.

## Connects To
- **Ch 6**: como calcular as probabilidades dos cenários de preço futuro.
- **Ch 8**: a árvore binomial refina esse método de cenários.
- **Ch 10**: delta formalizado como grega.
