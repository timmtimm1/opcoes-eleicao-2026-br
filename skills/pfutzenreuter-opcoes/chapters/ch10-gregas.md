# Capítulo 10: Interagindo com as gregas

## Core Idea
As gregas são derivadas parciais do prêmio de Black-Scholes em relação a cada variável de mercado. Elas **sugerem** o que acontece com o prêmio quando algo muda. Para o pequeno investidor, **theta** é a mais importante (faz a opção virar pó). Toda grega tem unidade — saiba a da sua calculadora.

## Frameworks Introduced
- **Delta (Δ)** = `N(d1)` (call) ou `N(d1) − 1` (put). Quanto o prêmio sobe se o spot subir $1.
  - Call: 0 a +100%. Put: 0 a −100%. Ação = +100%; venda a descoberto = −100%; dinheiro = 0.
  - OTM → ~0; ATM → ~±50%; ITM/DITM → ~±100%. Vol baixa empurra delta aos extremos.
  - É a proporção de ações da carteira replicante. Jargão: delta-neutra (não oscila nem lucra, alvo do market maker), delta-positiva, delta-negativa, comprar/vender delta.
- **Gama (Γ)** = derivada segunda; mudança esperada no delta quando o spot sobe $1.
  - Sempre positivo para opção comprada (negativo só em operações vendidas). Máximo perto de ATM, ~0 para ITM/OTM extremos. Área sob a curva = 100%.
  - Vol alta → gama ATM menor (delta muda mais suave). Perto do vencimento → gama ATM dispara.
  - Concavidade da carteira. Comprar/vender gama = comprar/vender opção.
- **Theta (Θ)** = efeito da passagem do tempo. Duas parcelas: decaimento temporal (sempre negativa, mais influente) + efeito da taxa de juros (positiva para put, negativa para call).
  - Quase sempre negativo. Mais negativo perto de ATM (maior valor extrínseco) e conforme o vencimento se aproxima. DITM: theta ~constante, prêmio decai linearmente.
  - **Confronte sempre theta com o prêmio**: theta $0,01/dia num prêmio de $0,04 = −25% ao dia.
- **Vega (ν)** = `S·√t·N'(d1)`. Efeito de +1 ponto percentual de volatilidade. Mesma forma da curva de gama. Igual para call e put de mesmos parâmetros. Pequena importância para o investidor casual, mas grande efeito relativo em OTM.
- **Rho (ρ)** = efeito de +1 ponto na taxa de juros. Positivo para call, negativo para put. Menos importante (juros não mudam da noite pro dia; opções curtas no Brasil).

## Reference Tables

Gregas da opção-cobaia (spot $100, strike $100, call, vol 25% ao ano, juro 12%, 2 meses):

| Grega | Valor | Interpretação |
|---|---|---|
| Delta | 59,8% | ação sobe $1 → opção sobe $0,598 |
| Gama | 3,8% | ação sobe $1 → delta vai a 63,6% |
| Theta | −$0,05 | cada dia → opção perde $0,05 |
| Vega | 15,82 | vol +1% → opção +$0,1582 |
| Rho | 9,14 | juro +1% → opção +$0,0914 |

Neo-gregas (fora do Black-Scholes original, usadas em exóticas e no sorriso da vol): **speed** (∂gama/∂spot), **charm/delta decay** (∂delta/∂tempo), **color** (∂charm/∂spot), **vanna** (∂delta/∂vol), **volga/vega gamma** (∂vega/∂vol), **lambda** (delta como % do prêmio). Sugestões do autor/Bastter: **delta quality** (delta/gama), **fatality** (theta como % do prêmio).

## Worked Example
Opção OTM com prêmio $0,04 e theta $0,01/dia: em termos absolutos parece inofensivo, mas é **−25% ao dia** sobre o investimento. Por isso o autor sugere a grega *fatality* (theta como % do prêmio) para investimentos "a seco". Como o mercado brasileiro só tem liquidez em calls de vencimento próximo, quase sempre lidamos com thetas muito negativos — bom para quem lança, ruim para quem compra; operações compradas devem ser encerradas cedo.

## Anti-patterns
- **Não checar a unidade da calculadora** (theta em $/dia vs. $/ano vs. % do prêmio) → interpretação totalmente errada. Theta é a pior nesse aspecto.
- **Achar que delta = chance de exercício** (é N(d2), não N(d1)).
- **Analisar operação só pelo delta** ignorando que o delta muda (para isso existe o gama).

## Key Takeaways
1. Theta é a grega decisiva para o pequeno investidor; sempre como % do prêmio.
2. Delta e gama são ditados pelo moneyness; vega tem a forma do gama.
3. Opção ITM/DITM/LEAPS: menor theta, menos corroída pelo tempo — mas sem liquidez no Brasil.
4. Gregas sugerem; o mercado faz o que quer. Ainda assim, é o que existe.

## Connects To
- **Ch 3**: delta como proporção da carteira replicante.
- **Ch 9**: as gregas exigem a vol implícita calculada primeiro.
- **Ch 11**: as gregas totais de uma operação = soma das gregas das pernas (ação: Δ+100%, resto 0).
