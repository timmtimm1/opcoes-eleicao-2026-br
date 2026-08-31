# Capítulo 2: O que são opções?

## Core Idea
Opção é como uma apólice de seguro ou um sinal: dá o **direito** (nunca o dever) de comprar (*call*) ou vender (*put*) um ativo a preço determinado (*strike*) até o vencimento. Diferente do contrato de futuro, que obriga ambas as partes.

## Frameworks Introduced
- **Prêmio = valor intrínseco + valor extrínseco**
  - Valor intrínseco: quanto a opção vale se exercida hoje. Call: `max(spot − strike, 0)`. Put: `max(strike − spot, 0)`. Nunca negativo.
  - Valor extrínseco: prêmio menos valor intrínseco. É o "preço da incerteza" — proporcional à probabilidade de a opção valer algo no vencimento.
- **Moneyness** — decidir o comportamento da opção:
  - **ITM** (in the money): tem valor intrínseco positivo. Acompanha de perto o spot; valor extrínseco cada vez menor.
  - **ATM** (at the money): spot ≈ strike. Maior valor extrínseco da série, prêmio mais "caro", opção mais negociada.
  - **OTM** (out of the money): valor intrínseco zero, spot longe do strike. Vira pó se nada mudar. Quanto mais OTM, menos o prêmio acompanha o spot.
  - **DITM** (deep ITM): valor intrínseco especialmente grande.
- **Valor extrínseco ∝ √tempo**: opção ATM de 12 meses não vale 12× a de 1 mês, vale ~3–4×.

## Key Concepts
- **Lançar (vender) opção** = emitir título novo no mercado; sinônimo de "vender". Risco **ilimitado** (call) ou limitado ao strike (put).
- **Margem**: garantia do lançador. Em dinheiro ≈ 3× o prêmio corrente, recalculada diariamente (chamada de margem). Em ações subjacentes ≈ 25× o prêmio, mas sem chamada de margem.
- **Comprar volatilidade** = comprar opção (lucra se oscilação aumentar). **Vender volatilidade** = lançar opção.
- **Estilos**: europeu (exerce só no vencimento), americano (qualquer dia), bermudas, asiática (preço médio), knock-out/barreira.

## Reference Tables

Séries BOVESPA (vencimento na 3ª segunda-feira do mês):

| Vencimento | Call | Put |  | Vencimento | Call | Put |
|---|---|---|---|---|---|---|
| Janeiro | A | M |  | Julho | G | S |
| Fevereiro | B | N |  | Agosto | H | T |
| Março | C | O |  | Setembro | I | U |
| Abril | D | P |  | Outubro | J | V |
| Maio | E | Q |  | Novembro | K | W |
| Junho | F | R |  | Dezembro | L | X |

Parâmetros que definem o prêmio: spot, strike, data de vencimento, estilo, direito garantido (call/put), taxa-base de juros (SELIC), volatilidade.

## Worked Example
Você tem PETR4 a $105 e teme queda. Compra uma **put** strike $100, vencimento dezembro, pagando o prêmio. Se PETR4 cair a $70, você exerce e vende a $100 (protegeu o capital). Se subir a $120, deixa a put virar pó e perde só o prêmio. É "seguro do carro" aplicado à ação.

Caso Barings (1995): Nick Leeson lançou muitas calls e puts apostando em bolsa parada. Terremoto de Kobe → bolsa caiu → puts chamaram margem que o banco não cobriu → insolvência. Ironia: se tivesse coberto as margens, teria lucrado no vencimento.

## Anti-patterns
- **Investir todas as economias em opção "a seco"**: pode perder tudo — a opção vira pó no vencimento. "Comprar call é como comprar caixa de tomates esperando o preço subir: em uma semana estão podres."
- **Avaliar opção com ferramentas de outros ativos** (análise técnica/fundamentalista): opção tem prazo de validade; se o mercado confirmar sua análise um dia após o vencimento, "perdeu".

## Key Takeaways
1. Opção = direito, não obrigação. Futuro = obrigação bilateral.
2. O que importa no prêmio: quantos dias faltam e o moneyness.
3. O tempo é a nêmesis da opção (valor extrínseco decai).
4. Lançar é como venda a descoberto, mas cria título novo e exige margem.
5. Na BOVESPA: puts têm liquidez quase zero; calls concentram-se em poucas blue chips, ATM e curto prazo. Opções protegidas de dividendos (strike cai junto).

## Connects To
- **Ch 3**: por que o valor extrínseco existe (opção como bilhete de loteria).
- **Ch 10**: as gregas explicam quantitativamente o comportamento por moneyness.
- **Ch 11**: moneyness na montagem decide as chances de cada operação.
