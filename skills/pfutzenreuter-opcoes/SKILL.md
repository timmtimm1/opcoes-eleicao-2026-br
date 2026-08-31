---
name: pfutzenreuter-opcoes
description: "Base de conhecimento do livro \"Investindo no Mercado de Opções\" de Elvis Pfützenreuter (Novatec). Use para montar e avaliar estratégias de opções (travas, spreads, boi, vaca, venda coberta, capital protegido), aplicar os frameworks do autor sobre precificação, volatilidade, paridade put-call, Black-Scholes e gregas, ou consultar capítulos e conceitos."
---

<!-- argument-hint: [tópico, nome de operação ou número do capítulo] -->

# Investindo no Mercado de Opções
**Autor**: Elvis Pfützenreuter (Novatec, 1ª ed.) | **Páginas**: ~252 | **Capítulos**: 12 | **Gerado**: 2026-08-31

## How to Use This Skill

- **Sem argumento** — carrega os frameworks centrais para montar operações.
- **Com um tópico** — pergunte sobre `trava de baixa`, `volatilidade implícita`, `theta`, `capital protegido` etc.; eu leio o capítulo relevante antes de responder.
- **Com capítulo** — peça `ch11` (operações), `ch06` (probabilidade de preço futuro), `ch10` (gregas).
- **Navegar** — pergunte "quais capítulos você tem?".

O foco do usuário é **montar operações**. Os capítulos 11 e 12 são o núcleo prático; 3–10 são a base de precificação. Quando o tópico não estiver nos frameworks abaixo, leio o capítulo antes de responder.

⚠️ Conteúdo educativo, não recomendação de investimento. Dados de mercado do livro são de 2008 (BOVESPA/BM&F, SELIC ~12%, tickers antigos como PETRA50, VALEE52). A B3 atual usa outra nomenclatura de séries e as puts têm mais liquidez.

---

## Core Frameworks & Mental Models

### As 3 verdades que valem o livro inteiro (Ch 1, Ch 11)
1. **O mercado tem a última palavra.** Avaliar opção só explica *por que* o preço é aquele; o lucro depende do preço de mercado. Só cabe "dançar ou ficar de fora".
2. **Avaliar opção exige computador** (planilha/calculadora) — não dá para fazer com HP-12C, e é preciso agilidade.
3. **O mercado de opções é soma zero** (levemente negativo pela corretagem). Toda operação só-opções é soma zero. Trate qualquer recomendação — inclusive as do livro — com espírito crítico.

### Prêmio = valor intrínseco + valor extrínseco (Ch 2)
- Intrínseco: `max(S−K,0)` call, `max(K−S,0)` put. Nunca negativo.
- Extrínseco: o preço da incerteza; **∝ √tempo**; 100% do prêmio quando não há intrínseco.
- **Moneyness** decide tudo: OTM (vira pó se nada mudar), ATM (maior extrínseco/prêmio, mais negociada), ITM/DITM (acompanha o spot ~1:1).

### Probabilidade de preço futuro (Ch 6 — o capítulo mais importante)
- Volatilidade = desvio padrão dos rendimentos, % a.a. Anualizar: `σ·√(períodos)` (nunca ×períodos).
- Preço futuro médio: `F = S·e^((r − σ²/2)·t)` — a volatilidade "come" parte do rendimento.
- P(spot < F) = `N(d)`, `d = [ln(F/S) − (r − σ²/2)t]/(σ√t)`. Faixa = N(d₂) − N(d₁).
- **Chance de vitória de uma operação** = probabilidade de o spot terminar na faixa lucrativa.

### Paridade put-call (Ch 7)
`C − P = S − K·e^(−r·t)`. Call comprada + put vendida (mesmo strike) = futuro sintético. Discrepâncias são raras e pequenas (custos comem a arbitragem).

### Black-Scholes e volatilidade implícita (Ch 9)
- `C = S·N(d1) − K·e^(−rt)·N(d2)`; `d1 = [ln(S/K)+(r+σ²/2)t]/(σ√t)`; `d2 = d1 − σ√t`.
- Das 5 entradas, só σ é duvidosa → resolver para ela = **vol implícita** = estimativa de mercado da vol futura.
- Vol implícita **alta** → opção cara, favorece **lançar**. **Baixa** → favorece **comprar**.
- **Sorriso da volatilidade**: ITM/OTM saem caras vs. ATM. Não invalida a paridade.

### Gregas (Ch 10) — sempre cheque a unidade da calculadora
- **Delta** = ∂prêmio/∂spot = N(d1) (≠ chance de exercício, que é N(d2)). Proporção da carteira replicante.
- **Gama** = ∂delta/∂spot. Máximo em ATM; dispara perto do vencimento.
- **Theta** = efeito do tempo. Quase sempre negativo; **a grega decisiva para o pequeno investidor**. Sempre avalie como % do prêmio.
- **Vega** (forma do gama), **Rho** (pouca importância no Brasil).

### Montar qualquer operação (Ch 11.17)
1. Gráfico de lucro no vencimento = soma dos valores intrínsecos das pernas.
2. Pontos de empate.
3. **Chance de vitória** (faixa lucrativa × distribuição log-normal). Passo mais difícil.
4. Gregas totais = soma das pernas (ação: Δ=+100%, resto 0).

### Escolher a operação pela visão de mercado (Ch 11)
Alta explosiva → **Boi** ITM · Alta com teto → **Trava de alta** ITM · Lateral → **Vaca** (com S3) · Queda/mercado esticado → **Trava de baixa** OTM · Renda sobre ação que possuo → **Venda coberta de call** mensal · Não posso perder no curto prazo → **Capital protegido / POP**.
Elementares (comprar/vender a seco) têm risco ilimitado — evitar isoladas; compostas travam o risco no investimento. Ver `patterns.md` e `cheatsheet.md` para parâmetros de cada uma.

### Gestão (Ch 11.21)
Escreva a estratégia antes de montar: lucro/prejuízo máx, chances, entrada, saída no lucro, plano se o mercado virar. Tolerância a perdas 15–20%, com espaço para oscilação normal. **Erro fatal do iniciante**: realizar lucros pequenos cedo e deixar as perdas crescerem. Nos spreads, theta vira contra ao entrar na faixa de prejuízo → desmontar.

---

## Chapter Index

| # | Título | Frameworks-chave |
|---|--------|------------------|
| [ch01](chapters/ch01-introducao.md) | Introdução | as 3 verdades, soma zero |
| [ch02](chapters/ch02-o-que-sao-opcoes.md) | O que são opções? | prêmio = intrínseco + extrínseco, moneyness, lançamento, margem, séries BOVESPA |
| [ch03](chapters/ch03-quanto-vale-uma-opcao.md) | Quanto vale uma opção? | média ponderada de cenários, carteira replicante (delta), impacto das variáveis |
| [ch04](chapters/ch04-matematica-financeira.md) | Matemática financeira elementar | valor = renda/juros, valor presente, capitalização contínua |
| [ch05](chapters/ch05-capm.md) | Modelo CAPM | r = i + β·m, risco diversificável vs. sistêmico, prêmio ~6% |
| [ch06](chapters/ch06-volatilidade-e-incerteza.md) | Volatilidade e incerteza | anualização √tempo, preço futuro médio, P(spot<F) = N(d), log-normal |
| [ch07](chapters/ch07-paridade-put-call.md) | Paridade put-call | C − P = S − K·e^(−rt), futuro sintético, arbitragem |
| [ch08](chapters/ch08-arvores-binomiais.md) | Árvores binomiais | construir/recuar a árvore, recombinante, exóticas por poda |
| [ch09](chapters/ch09-black-scholes.md) | Black-Scholes | fórmulas, d1/d2, N(d2) = chance de exercício, vol implícita, sorriso |
| [ch10](chapters/ch10-gregas.md) | Interagindo com as gregas | delta, gama, theta (a mais importante), vega, rho, neo-gregas |
| [ch11](chapters/ch11-operacoes-com-opcoes.md) | Lucratividade das operações | 4 elementares + venda coberta, capital protegido, POP, spreads, boi, vaca; método de análise; estratégia |
| [ch12](chapters/ch12-operacoes-com-cotacoes-de-mercado.md) | Operações com cotações de mercado | simulação real série VALEE (abr–mai 2008), estratégia vs. avestruz |

## Topic Index

- **Anti-pattern do iniciante (realizar lucro cedo)** → ch11
- **Árvore binomial** → ch08
- **Black-Scholes (fórmula, dedução)** → ch09, ch06
- **Boi (call ratio backspread)** → ch11, ch12
- **CAPM / beta / prêmio de risco** → ch05
- **Capital protegido / synthetic long call** → ch11
- **Carteira replicante** → ch03, ch10
- **Chance de vitória de operação** → ch11, ch06
- **Delta / gama / theta / vega / rho** → ch10
- **Estilos de opção (europeu, americano, exótico)** → ch02, ch08
- **Estratégia de operação (como formular)** → ch11
- **Gregas totais de uma operação** → ch11, ch10
- **Juros compostos / valor presente / capitalização contínua** → ch04
- **Margem / chamada de margem** → ch02
- **Moneyness (ITM/ATM/OTM/DITM)** → ch02, ch10
- **Neo-gregas (vanna, volga, charm, fatality)** → ch10
- **Paridade put-call / arbitragem** → ch07
- **POP BOVESPA** → ch11
- **Preço futuro provável / distribuição log-normal** → ch06
- **Prêmio (intrínseco + extrínseco)** → ch02, ch03
- **Put credit spread** → ch11
- **Renda fixa + opções** → ch11
- **Simulação com cotações reais** → ch12
- **Soma zero** → ch01, ch11
- **Sorriso da volatilidade** → ch09, ch12
- **Spreads (debit/credit, bull/bear)** → ch11
- **Trava de alta (call debit spread)** → ch11, ch12
- **Trava de baixa / reversão (call credit spread)** → ch11, ch12
- **Vaca (call ratio spread)** → ch11, ch12
- **Venda coberta (call e put)** → ch11, ch12
- **Volatilidade (histórica vs. implícita)** → ch06, ch09
- **Volatilidade: anualização (√tempo)** → ch06

## Supporting Files

- [glossary.md](glossary.md) — todos os termos do Apêndice A + conceitos-chave, com capítulo de referência.
- [patterns.md](patterns.md) — cada operação e técnica: quando usar, como montar, trade-offs, parâmetros.
- [cheatsheet.md](cheatsheet.md) — tabelas de decisão: operação por visão de mercado, moneyness → gregas, fórmulas de bolso, parâmetros de todas as operações, regras de gestão.

---

## Scope & Limits

Cobre o conteúdo do livro (base matemática + análise de operações). Dados de mercado são de 2008; a mecânica das operações continua válida, mas nomenclatura de séries, liquidez de puts, tributação e a calculadora web do autor (epx.com.br/ctb/bscalc.php) podem estar desatualizados. Para execução na B3 hoje, combine com fontes atuais. O livro é explícito: nenhuma estratégia garante lucro (soma zero) — o objetivo é controle de risco e emocional.
