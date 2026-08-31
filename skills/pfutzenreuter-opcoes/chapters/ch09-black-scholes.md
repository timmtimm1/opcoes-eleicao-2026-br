# Capítulo 9: Avaliando opções com o modelo de Black e Scholes

## Core Idea
Black-Scholes (1973) é um "pacote": fórmulas fechadas + premissas irreais (sem corretagem, volatilidade fixa, retorno = SELIC). Dá o "valor justo" da opção europeia. Como o mercado é soberano, quando o preço difere da avaliação, a variável duvidosa é a **volatilidade** — e resolver para ela dá a **volatilidade implícita**.

## Frameworks Introduced
- **Fórmulas (call e put europeias, sem dividendos)**:
  - `C = S·N(d1) − K·e^(−r·t)·N(d2)`
  - `P = K·e^(−r·t)·N(−d2) − S·N(−d1)` (deduzida via paridade)
  - `d1 = [ln(S/K) + (r + σ²/2)·t] / (σ·√t)`
  - `d2 = d1 − σ·√t`
  - `N(x)` = normal acumulada = `NORM.DIST(x;0;1;1)`.
- **Interpretação das partes**:
  - `N(d2)` = probabilidade de a call ser exercida (vencer ITM). Da put: `N(−d2)` = `1 − N(d2)`.
  - `N(d1)` = delta da call (**não** é a chance de exercício; comum confundir, mas os valores costumam estar próximos).
- **Volatilidade implícita**: tentativa-e-erro (interpolação linear ou Newton) até o prêmio teórico bater com o de mercado. Não tem fórmula fechada.
  - **É a volatilidade futura que o mercado estima** e deve ser levada a sério. Profissionais cotam opção pela vol implícita, não pelo prêmio absoluto.
- **Sorriso da volatilidade**: plotar a vol implícita de toda a série (mesmo vencimento, strikes diferentes) forma uma curva em U. Opções perto de ATM são as "mais baratas" em custo/benefício; ITM e OTM saem "caras". Aparece em quase todo mercado; hoje é tratado como ingrediente legítimo, não distorção. Mais pronunciado após crashes.

## Key Concepts
- O prêmio de Black-Scholes é o "preço de custo" / "valor justo" — não dá vantagem a comprador nem vendedor. O mercado desvia disso por oferta/demanda.
- **Vol implícita alta** (vs. histórica) → opção cara, talvez mercado em queda (vol sobe quando mercado cai) → favorece operações **vendidas** (lançar).
- **Vol implícita baixa** → opção barata, talvez mercado em alta → favorece operações **compradas**.
- BOVESPA: avaliar as opções como europeias (protegidas de dividendos).

## Worked Example
VALED54 (call VALE série D, strike $54), fechamento 03/abr. Spot VALE5 = $51,30; vol histórica trimestral = 51,33%; juro = 11,25% ao ano.
- Black-Scholes com vol histórica → "valor justo" $1,44.
- Mas VALED54 fechou a **$0,50** no mercado.
- Testando volatilidades, **28,75%** faz o modelo dar $0,50.
- Leitura: o mercado estima a volatilidade **futura** da Vale em ~29%, bem abaixo da histórica de 51% → com menos volatilidade, a opção vale menos. A vol implícita é o "preço real".

## Anti-patterns
- **Achar que N(d1) é a chance de exercício** — é N(d2).
- **Comparar prêmios absolutos de opções para decidir se está "cara"** — inútil; use a volatilidade implícita.
- **Ignorar o sorriso**: uma série que não "sorri" é que está distorcida.

## Key Takeaways
1. Black-Scholes só tem fórmula fechada para estilo europeu.
2. Das 5 entradas (S, K, r, t, σ), quatro são certas; a σ é a incógnita real → vol implícita.
3. Vol implícita = estimativa de mercado da volatilidade futura; norteia se convém comprar ou lançar.
4. O sorriso encarece ITM/OTM em relação a ATM — considere isso na montagem.

## Connects To
- **Ch 6**: d2 vem da fórmula de probabilidade de preço futuro.
- **Ch 7**: a put sai da paridade.
- **Ch 10**: as gregas são derivadas parciais dessas fórmulas — exigem a vol implícita primeiro.
