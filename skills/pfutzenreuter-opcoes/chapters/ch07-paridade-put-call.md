# Capítulo 7: Paridade entre opções de compra e de venda

## Core Idea
Call e put de mesmo strike e vencimento têm prêmios matematicamente e rigidamente relacionados. Comprar uma call + lançar uma put de mesmo strike "sintetiza" um contrato de futuro. Se a relação se quebra, há arbitragem (dinheiro fácil sem risco).

## Frameworks Introduced
- **Equação de paridade**: `C − P = S − K·e^(−r·t)`
  - `C` = prêmio da call; `P` = prêmio da put; `S` = spot; `K` = strike; `r` = juro; `t` = tempo.
  - Se assumimos K já no valor presente: `C − P = S − K`.
  - Rearranjo útil: se você sabe C e o valor do futuro, `P = C − (S − K·e^(−rt))`.
- **Sintetizar o futuro com opções**: comprar call strike K + lançar put strike K → paga o mesmo que o contrato de futuro. Se o futuro vale −$3 (você recebe ao montar), a montagem call+put deve render +$3.
- **Prova por arbitragem**: qualquer discrepância entre (call − put) e (S − K descontado) pode ser explorada montando call comprada + put vendida + venda a descoberto da ação (ou o oposto), travando o lucro da diferença em todos os desfechos do vencimento.

## Key Concepts
- **Contrato de futuro**: valor = `S − K·e^(−rt)`. O desconto do strike pela taxa de juros aumenta o valor presente pago pelo comprador. Linha "grossa" no gráfico = valor intrínseco; linha "fina" = valor real com juros (é o preço de mercado).
- **Put europeia ITM pode ter prêmio < valor intrínseco**: aparente aberração, causada só pelos juros correndo até o vencimento. Some conforme o vencimento se aproxima.
- **Reduzir o strike** aumenta a call e diminui a put.
- **Faixa de tolerância**: custos de corretagem e aluguel de venda a descoberto impedem a maioria de arbitrar, então a paridade pode ser "desrespeitada" dentro de uma margem.

## Worked Example
VALE5 a $50 hoje. VALEA55 (call jan, strike $55) cotada a $0,50. VALEM55 (put mesmo strike) a $6,00. Desconsiderando juros, a paridade prevê `C − P = S − K = 50 − 55 = −5`, mas o mercado dá `0,50 − 6,00 = −5,50`. Discrepância de $0,50. Para explorar:
1. Comprar VALEA55 a $0,50;
2. Vender VALEM55 a $6,00;
3. Vender VALE5 a descoberto a $50.
Caixa: $55,50. Em qualquer desfecho no vencimento (VALE5 a $70, $55 ou $40), você fecha as posições e sobra exatamente $0,50 de lucro — arbitragem sem risco.

## Anti-patterns
- **Ignorar a taxa de juros ao avaliar contrato de futuro/paridade**: o adiantamento recebido rende na renda fixa; o mercado esvazia essa "injustiça".
- **Contar com arbitragem fácil**: custos reais (corretagem, aluguel) comem discrepâncias pequenas.

## Key Takeaways
1. Sabendo o prêmio da call, calcula-se o da put (mesmos parâmetros).
2. Call comprada + put vendida (mesmo strike) = futuro sintético.
3. Discrepâncias na paridade são raras e pequenas na prática.
4. O sorriso da volatilidade **não** invalida a paridade: call e put de mesmo strike têm a mesma volatilidade implícita.

## Connects To
- **Ch 4**: desconto do strike ao valor presente.
- **Ch 9**: a put de Black-Scholes é deduzida da call via paridade.
- **Ch 11**: futuros sintéticos aparecem embutidos em ratio spreads.
