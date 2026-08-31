# Capítulo 5: Modelo CAPM — Capital Asset Pricing Model

## Core Idea
Ativos mais arriscados devem ser avaliados com taxa de juros maior (para valerem menos). O CAPM estabelece a relação matemática entre risco e retorno, mas só remunera o risco **não-diversificável** (sistêmico), medido pelo beta.

## Frameworks Introduced
- **Fórmula CAPM**: `r = i + β · m`
  - `r` = taxa de retorno esperada; `i` = taxa-base de juros (SELIC); `β` = beta do ativo; `m` = prêmio de risco do mercado (carteira padrão / índice, β=1).
  - Ex.: BBAS3 com β=0,757, IBOVESPA 18%, SELIC 12% → prêmio 6% → retorno esperado = 12% + 0,757·6% ≈ 16,5%.
- **Beta (co-variância)**: correlação da variância do ativo com o mercado (IBOVESPA). β=0,5 → absorve 50% das oscilações do mercado. β<1 = mais seguro que a média; β=1,8 = amplifica os solavancos, muito arriscado.
- **Prêmio de risco ≈ 6% ao ano** acima da renda fixa — empiricamente observado em vários mercados do mundo. Boa estimativa inicial.

## Key Concepts
- **Risco = variância do retorno**. Títulos do governo têm variância zero → nenhum ativo pode render menos que a SELIC.
- **Risco diversificável ("ruído")**: específico de cada ativo, cancelável combinando ativos numa carteira. O CAPM **não** remunera. Emprestar para o cunhado é risco diversificável — não merece retorno.
- **Risco não-diversificável (sistêmico)**: afeta o mercado todo, não some com diversificação.

## Worked Example
Ativo XYZ tem grande variação nos ganhos (parece arriscado a olho nu) mas correlação de apenas 0,5 com o mercado. Pelo CAPM, é considerado "seguro" (beta baixo, provável pagador de dividendos), porque metade da oscilação dele é ruído diversificável. Para essa promessa se cumprir na prática, a carteira precisa estar de fato diversificada.

## Anti-patterns
- **"Risco alto = retorno alto automático"**: inversão do raciocínio, derivada da má compreensão do CAPM. Investidores ousados falidos não são recompensados por "correr risco".
- **"Investimento arriscado é automaticamente ruim"**: também falso.
- **"Carteira TEM de ser diversificada"**: crença enviesada; diversificação custa corretagem e não elimina risco sistêmico.
- **Confiar no CAPM para prever o futuro**: ele não prevê. BBAS3 e IBOVESPA não vão seguir a previsão teórica.

## Key Takeaways
1. CAPM = ferramenta para achar a taxa de juros adequada à avaliação de um ativo.
2. Só o risco sistêmico (beta) é remunerado.
3. A relação risco/retorno do CAPM só se concretiza com carteira diversificada.
4. Betas de ações BOVESPA estão disponíveis em vários sites; o prêmio de risco use ~6%.

## Connects To
- **Ch 4**: a taxa de retorno alimenta a fórmula valor = renda / taxa.
- **Ch 6**: variância do retorno = volatilidade, o outro pilar da precificação.
