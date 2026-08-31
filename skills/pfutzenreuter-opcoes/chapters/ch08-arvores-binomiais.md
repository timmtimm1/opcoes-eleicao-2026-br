# Capítulo 8: Avaliando opções usando árvores binomiais

## Core Idea
A árvore binomial estima a evolução do preço da ação em passos discretos, calcula o valor da opção em cada nó final e "recua" tirando médias e descontando juros até o presente. É mais fácil de entender que Black-Scholes e serve para opções americanas e exóticas.

## Frameworks Introduced
- **Construir a árvore** (por passo):
  1. Preço médio do próximo passo = preço atual valorizado pela taxa de juros (`S·e^(r·Δt)`). **Não** aplica o efeito depressivo da volatilidade — a árvore faz isso sozinha.
  2. Converter volatilidade anual em volatilidade do passo: `σ_passo = σ_anual·√(Δt)`. Ex.: 25% ao ano → 25%·√(1/12) ≈ 7,2% ao mês.
  3. Dois preços possíveis = preço médio ± volatilidade do passo.
  4. Repetir a partir de cada nó.
- **Árvore recombinante**: subir-depois-descer dá o mesmo preço que descer-depois-subir (mesmo % de movimento), então nós se fundem e a árvore simplifica.
- **Avaliar a opção (recuar da direita para a esquerda)**:
  1. No vencimento, valor da opção em cada nó = valor intrínseco.
  2. Em cada nó anterior, valor = média dos dois nós seguintes (50/50).
  3. **Descontar um passo de juros a cada recuo** (multiplicar por e^(−r·Δt), ~0,99 ao mês no exemplo).
  4. O valor no nó inicial (mês 00) é o preço da opção hoje.

## Key Concepts
- Black-Scholes é o **caso-limite** da árvore binomial com nº de passos arbitrariamente grande. Mas a árvore foi inventada **depois** (Cox, Ross e Rubinstein), como método didático.
- **Método numérico**: muitas operações simples em vez de uma fórmula fechada. Impraticável à mão; perfeito para computador. Recomendado: ≥ 40 passos.
- **Opções exóticas/barreira**: basta "podar" os galhos onde a opção deixa de valer e atribuir zero no ponto de poda. Black-Scholes seria inútil aqui.

## Worked Example
Opção-cobaia: spot $100, strike $100, call europeia, vol 25% ao ano, juro 12% ao ano, 2 meses, 2 passos.
- σ mensal = 25%·√(1/12) ≈ 7,2%.
- Mês 01: preço médio = 100·e^(0,12/12) ≈ 101,0 → ramos em ~108,29 e ~93,72.
- Mês 02 (a partir de $108,29): ramos ~$117,28 e ~$101,49 → valores da call $17,28 e $1,49.
- Nó $108,29 no mês 01: média (17,28 + 1,49)/2 = $9,39.
- Nó $93,72: média ($1,49 + $0)/2 = $0,75.
- Mês 00: média ($9,39 + $0,75)/2 = $5,07 → descontando os juros a cada passo (×0,99), **$4,97**.
- Black-Scholes dá $5,10 — a árvore de 2 passos chegou perto apesar da baixa precisão.

## Anti-patterns
- **Esquecer de descontar os juros a cada passo**: erro cometido no próprio exemplo do livro; "$1 hoje vale mais que $1 amanhã".
- **Usar poucos passos e confiar na precisão**: 2 passos são didáticos, não operacionais.

## Key Takeaways
1. A árvore captura a essência dos movimentos supondo distribuição log-normal.
2. O preço final mais provável é levemente acima do spot inicial (juros apontam a árvore para cima).
3. Delta, gama e theta saem da própria árvore; vega e rho exigem recalcular a árvore com parâmetros diferentes.
4. Use a árvore quando precisar avaliar opção americana/exótica; senão, Black-Scholes.

## Connects To
- **Ch 3**: é o refinamento do método de cenários ponderados.
- **Ch 9**: Black-Scholes como caso-limite.
- **Ch 10.12**: gregas calculadas a partir da árvore.
