# Cheatsheet — Montando Estratégias de Opções (Pfützenreuter)

## Regras de decisão fundamentais
- **Toda operação só com opções é soma zero.** Se algo promete lucro consistente, ou é escassez de lançadores (prêmio acima do "valor justo") ou você está presumindo mercado ineficiente. Nunca aposte contra "distorções de mercado" — se avaliação ≠ preço, o erro quase sempre é da avaliação.
- **Se o preço da opção difere de Black-Scholes → a variável errada é a volatilidade.** Resolva para ela = volatilidade implícita.
- **Perder muito capital é desastroso**: ganhar 200% e perder 75% em seguida = 50% mais pobre. Priorize risco limitado sobre retorno alto.
- **Ficar de fora é uma operação válida.**
- **Corretagem fixa mata operação de muitas pernas** (uma vaca = até 6×). Pouco capital → operações que terminam com tudo virando pó (venda coberta, trava de baixa).

## Escolher a operação pela visão de mercado

| Sua visão | Operação recomendada | Por quê |
|---|---|---|
| Alta forte/explosiva, pouco capital | **Boi** (call ratio backspread) ITM | lucro ilimitado, capital = só margem |
| Alta com teto conhecido | **Trava de alta** (call debit spread) ITM | risco = prêmio pago, boas chances |
| Alta moderada / não cai | **Put credit spread** (se houver liquidez) ou vender put coberta | mercado tende a subir (juros) |
| Lateral, entre S1 e S2 | **Vaca** (call ratio spread, com S3) | theta a favor em larga faixa |
| Queda / mercado "esticado" | **Trava de baixa** (call credit spread) OTM | aposta contra novas altas, ROM alto |
| Sou dono da ação, quero renda extra | **Venda coberta de call**, repetida todo mês | theta sempre positivo, BXM: menos vol, mesmo retorno |
| Não posso perder no curto prazo | **Capital protegido** / **POP BOVESPA** | put = seguro; POP é "de graça" |
| Capital grande, bater a renda fixa | **Renda fixa + opções** (operar só os juros em spreads) | principal intocado |

## Moneyness → comportamento (decorar)
| | OTM | ATM | ITM / DITM |
|---|---|---|---|
| Valor extrínseco | pequeno (mas % alto) | **máximo** | pequeno |
| Delta (call) | ~0 | ~+50% | ~+100% |
| Gama | ~0 | **máximo** | ~0 |
| Theta ($) | médio | **mais negativo** | ameno / linear |
| Prêmio acompanha o spot? | pouco | ~metade | quase 1:1 |

- Vol implícita **baixa** → opções baratas, talvez mercado em alta → favorece **comprar** (debit spreads, call DITM, boi).
- Vol implícita **alta** → opções caras, talvez mercado em queda → favorece **lançar** (credit spreads, vendas cobertas).
- Sorriso da volatilidade: ITM e OTM saem caras vs. ATM. Em ratio, montar para que a opção **vendida** seja a "cara".

## Impacto das variáveis no prêmio (Tabela 3.1)
| Sobe → | Call | Put |
|---|---|---|
| Spot | ↑ | ↓ |
| Strike | ↓ | ↑ |
| Prazo | ↑ | ↑ |
| Juros | ↑ | ↓ |
| Volatilidade | ↑ | ↑ |

## Fórmulas de bolso
- Valor intrínseco: call `max(S−K,0)`, put `max(K−S,0)`.
- Valor extrínseco ∝ **√tempo** (opção 12m ≈ 3–4× a de 1m, não 12×).
- Anualizar volatilidade: `σ_anual = σ_período · √(nº de períodos)`.
- Preço futuro médio: `F = S · e^((r − σ²/2)·t)`.
- P(spot < F): `N(d)`, `d = [ln(F/S) − (r − σ²/2)t] / (σ√t)`; faixa [F1,F2] = N(d₂) − N(d₁).
- Paridade: `C − P = S − K·e^(−r·t)`.
- Black-Scholes: `C = S·N(d1) − K·e^(−rt)·N(d2)`; `d1 = [ln(S/K)+(r+σ²/2)t]/(σ√t)`; `d2 = d1 − σ√t`.
- Chance de exercício da call = `N(d2)` (não N(d1) = delta). Put: `N(−d2)`.
- Vol do passo da árvore binomial: `σ · √(Δt)`; descontar `e^(−r·Δt)` a cada recuo.

## Parâmetros das operações (S1 = strike mais baixo; investimento = margem salvo indicado)
| Operação | Montagem | Risco máx | Lucro máx | Spot de empate | Margem |
|---|---|---|---|---|---|
| Comprar call a seco | +1 call | 100% do prêmio | ilimitado | K + prêmio | 0 |
| Comprar put a seco | +1 put | prêmio | K | K − prêmio | 0 |
| Vender call a seco | −1 call | **ILIMITADO** | prêmio | K + prêmio | ~3× prêmio |
| Vender put a seco | −1 put | K | prêmio | K − prêmio | ~3× prêmio |
| Venda coberta de call | +ação −1 call | queda da ação | prêmio + K − custo ação | custo ação − prêmio | 0 (ação) |
| Venda coberta de put | $K −1 put | K | prêmio | K − prêmio | K |
| Capital protegido | +ação +1 put | prêmio da put | ilimitado | spot compra + prêmio | 0 |
| POP BOVESPA | +10 ação +10 put −2/3 call | ~nulo | ilimitado | spot + prêmios pagos − recebidos | 0 |
| Call credit spread (trava baixa) | −call S1 +call S2>S1 | (S2−S1) − prêmio líq | prêmio líq recebido | S1 + prêmio líq | S2−S1 |
| Put credit spread | −put S1 +put S2<S1 | S1−S2 | prêmio líq recebido | S2 − prêmio líq | S1−S2 |
| Call debit spread (trava alta) | +call S1 −call S2>S1 | prêmio líq pago | (S2−S1) − prêmio líq | S2 − prêmio líq | 0 |
| Boi (call ratio backspread) | −X call S1 +Y>X call S2 | (S2−S1)·X | ilimitado | S2 + (S2−S1)·X/Y | (S2−S1)·X |
| Vaca (call ratio spread) | +1 call S1 −X call S2 +(X−1) call S3 | (S3−S2)·(X−1) | S2−S1 | ~S2 + (S3−S2)/X | (S3−S2)·(X−1) |

## Tells & regras de gestão
- **Theta positivo na faixa lucrativa e negativo na faixa de prejuízo** (spreads) → sinal para desmontar assim que o spot entrar na faixa de prejuízo.
- **Boi**: theta negativo em qualquer cenário → sempre com prazo máximo de desfazimento; realizar lucro cedo.
- **Vaca / boi**: nunca abandonar até o vencimento — acompanhar 2×/dia.
- **Compra a seco**: prazo de desfazimento curto (dias); preferir DITM.
- **Venda coberta**: lançar 1 mês antes do vencimento; não desmontar antes da hora (arrependimento garantido); strike próximo ao custo da ação.
- **Fronteira lucro/prejuízo é drástica** no vencimento (VALEE58 = +70%, VALEE60 = pó) → o strike escolhido importa mais que a direção acertada.
- Tolerância a perdas: **15–20%**, sempre com espaço para oscilação normal (senão vira tempestade de stops).
- Erro fatal do iniciante: **realizar lucros pequenos cedo e deixar as perdas crescerem** — garante prejuízo.
- Sempre escreva a estratégia antes: lucro/prejuízo máx, chances, entrada, saída no lucro, plano se o mercado virar.
