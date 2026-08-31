# Capítulo 6: Volatilidade e incerteza

## Core Idea
O capítulo mais importante para o investidor em opções: como estimar a probabilidade de o preço futuro cair dentro de uma faixa. Rendimentos seguem distribuição normal; preços seguem log-normal. Todas as chances de ganhar/perder giram em torno disso.

## Frameworks Introduced
- **Volatilidade = desvio padrão dos rendimentos** (não do valor total do ativo), normalmente em % ao ano.
  - Cálculo: desvios da média → elevar ao quadrado → média → raiz quadrada.
  - **Anualizar volatilidade**: multiplicar pela **raiz quadrada do tempo** (não pelo tempo). Vol mensal 10% → vol anual = 10%·√12 ≈ 34,64%.
  - **Anualizar média** (ajuste pela volatilidade): `μ_anual = μ_mensal·períodos − σ²/2` aproximado; a volatilidade "come" parte do rendimento (−50% seguido de +50% = −25% residual).
- **Preço futuro médio**: `F = S · e^((μ − σ²/2)·t)`
  - `μ` = taxa-base de juros (o livro usa a SELIC pura, como Black-Scholes); `σ` = volatilidade anual; `t` = anos.
  - Ex.: ação $100, σ 30%, μ 12%, t=1 ano → F ≈ $107,79 (não $112: a volatilidade comeu). 50% de chance de ficar acima, 50% abaixo.
- **Probabilidade de o preço futuro ficar abaixo de F**: `p = N(d)` onde
  `d = [ln(F/S) − (μ − σ²/2)·t] / (σ·√t)` — mesma estrutura do d2 de Black-Scholes.
  - `N(x)` = distribuição normal cumulativa = `NORM.DIST(x;0;1;1)` no Excel. Sem fórmula fechada.
  - **Chance de ficar numa faixa [F1, F2]** = P(abaixo de F2) − P(abaixo de F1).

## Key Concepts
- **Distribuição normal**: ±1σ = 68,2% (34,1% de cada lado); ±2σ = 95,4%; ±3σ = 99,7%. Toda normal tem essas mesmas probabilidades.
- **Log-normal**: o logaritmo da grandeza segue a normal; a grandeza se espalha para os valores altos. O preço futuro é log-normal porque é multiplicação em cadeia de rendimentos (que são normais). A volatilidade da log-normal é a mesma calculada para os rendimentos — "pulo do gato".
- **Volatilidade histórica**: calculada sobre o passado (comum: 21 dias úteis = mês; 252 = ano). Serve como estimativa da futura, com cautela.
- **Random walk**: preços completamente imprevisíveis (bêbado andando). Rendimento passado não projeta preço futuro; escolher ações seria bobagem.

## Worked Example
Ação $100, vol 30% ao ano. Chance de o preço passar de $150 em 1 ano?
1. F médio = $100·e^((0,12 − 0,045)·1) = $107,79.
2. `d = [ln(150/100) − (0,12 − 0,045)·1] / (0,30·√1) = [0,4055 − 0,075] / 0,30 ≈ 1,10`.
3. `N(1,10) ≈ 0,864` → 86,4% de chance de ficar **abaixo** de $150.
4. Logo, **13,6% de chance de passar de $150**.

## Anti-patterns
- **Multiplicar a volatilidade pelo tempo para anualizar** (é √tempo).
- **Confiar no rendimento médio passado para projetar preços** — é inútil; use taxa-base + prêmio, ou taxa-base pura.
- **Achar que existe "seguro contra volatilidade" acessível**: só a Bolsa de Chicago tem (VIX). Aproximação grosseira: duas opções OTM iguais (uma call, uma put) — mas deixam de proteger igual quando o mercado se mexe.

## Key Takeaways
1. Volatilidade é a incerteza do futuro traduzida em número; sem ela não há valor extrínseco.
2. Preços médios futuros sempre tendem para cima (a bolsa precisa subir ≥ juro só para empatar com a renda fixa). Topos históricos não surpreendem.
3. Índices como IBOVESPA sobem década após década em parte porque empresas quebradas saem do índice.
4. Use um computador/planilha para calcular N(x).

## Connects To
- **Ch 9**: a fórmula de probabilidade daqui é parte integrante de Black-Scholes (d1, d2).
- **Ch 11**: a "faixa lucrativa" de cada operação × probabilidade do spot = chance de vitória.
