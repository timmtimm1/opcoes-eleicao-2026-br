# A operação e a estratégia escrita

Operação de volatilidade para a janela da eleição, no arcabouço de Pfützenreuter.
Educativo, não recomendação. Números **ilustrativos** — confirme a cadeia real.

---

## 1. Tese

Evento binário com cauda: Lula vs Flávio Bolsonaro, 2º turno dentro da margem de erro.
A transmissão para o preço é a **credibilidade fiscal** (Goldman: câmbio −4% a +3%; SocGen:
quebra do carry). Catalisadores empilhados: **COPOM 16–17/09, 1º turno 04/10, 2º turno 25/10**.
O mercado já começou a reprecificar (Ibovespa −2,5% em 11/08 citando a eleição).
→ Espera-se **movimento forte para qualquer lado** e/ou **alta da volatilidade implícita**.

## 2. Instrumento

Opções sobre **IBOV** (índice, europeias, liquidação financeira) ou **BOVA11** (ETF,
americanas, mais liquidez de varejo). O livro (cap. 6.7) define o instrumento de volatilidade
como **1 call OTM + 1 put OTM** de mesmo vencimento.

**Vencimento: novembro/2026** (3ª sexta, ~20/11). Cobre 1º e 2º turno. **Evitar a série de
outubro** — expira entre os turnos.

## 3. A operação — *strangle* de risco definido (reverse iron condor)

| Perna | Ação | Strike aprox. (spot IBOV ~168k) |
|---|---|---|
| 1 | **Comprar** put OTM | ~158.000 (−6%) |
| 2 | **Comprar** call OTM | ~178.000 (+6%) |
| 3 | **Vender** put mais OTM (trava baixa) | ~146.000 (−13%) |
| 4 | **Vender** call mais OTM (trava alta) | ~190.000 (+13%) |

**Por que não um straddle "a seco":** o livro (cap. 9) diz que **IV alta favorece lançar, não
comprar** — pré-eleição o prêmio do evento já está no preço. O strangle puro tem risco de
perder **100% do prêmio** (anti-pattern da cap. 11) e o **theta** sangra todo dia (cap. 10).
Vender as duas asas: reduz custo, theta e vega líquidos → sobrevive ao *IV crush* pós-evento;
converte "elementar de risco ilimitado de perda" em **composta de risco limitado** (cap. 11.5).
Trade-off: teto no lucro. Se vier um movimento gigante (o "grau de investimento" da cap. 12),
as asas seguram o ganho. Aceita-se.

## 4. Análise (método da cap. 11.17)

1. **Payoff no vencimento** = soma dos valores intrínsecos das 4 pernas.
   - Perda máxima = **prêmio líquido pago** (limitada).
   - Lucro máximo = (largura da asa) − prêmio líquido, se o IBOV fechar ≤146k ou ≥190k.
2. **Pontos de empate** ≈ 158.000 − prêmio líq. (baixa) e 178.000 + prêmio líq. (alta).
3. **Chance de vitória** (fórmula da cap. 6): `P(fora da faixa 158k–178k) = 1 − [N(d2) − N(d1)]`,
   σ = IV da série de novembro, t ≈ 11 semanas. Carregada até o vencimento a chance é **baixa**;
   a operação ganha **no caminho** (vender na alta de vol / no movimento pós-1º turno), não no
   "avestruz" (cap. 12).
4. **Gregas totais:** vega líquida **positiva** (menor que o strangle puro), gama líquido
   positivo perto do spot, **theta líquido negativo** (menor que o straddle), rho pequeno.

## 5. Veículos

| Ativo | Reage à eleição | Motor | Nota |
|---|---|---|---|
| PETR4 | muito | preço de combustível, dividendos, diretoria | a "PETRA50" do livro; put OTM cara pelo sorriso da vol |
| BBAS3 | muito | banco estatal, crédito direcionado, payout | β=0,757 no CAPM do livro (cap. 5) |
| ITUB4 | pouco | juros / ciclo de crédito | catalisador é o COPOM 16–17/09; rho pesa (cap. 10) |
| BBDC4 | médio | juros + reestruturação própria | perna de par para espalhar risco |

**Como escolher:** tese política → PETR4 / BBAS3. Tese de juros → ITUB4 / BBDC4 no vencimento
que pega o COPOM. Cesta IBOV + PETR4 dilui ruído idiossincrático.

## 6. Janela de compra

Faixa de dias, não um "dia mágico": perto o suficiente do evento para a vol já esquentar,
longe o bastante do vencimento para o theta não estar pesado.

- **PETR4 / BBAS3 / IBOV** → janela ancorada no **1º turno (04/10)**.
- **ITUB4 / BBDC4** → janela ancorada no **COPOM (17/09)**.
- Antecedência sugerida: ~15–20 pregões antes do catalisador.
- Dia da semana: **terça a quinta** (evita gap de segunda e ajuste de sexta).
- Horário: **10:30–11:30** ou **13:30–15:00**. Evitar os 15 min de abertura, a última meia
  hora, 10:30 em dia de dado dos EUA, e os minutos ao redor do COPOM / boca de urna.
- **Zona de theta** = últimos ~10 pregões antes do vencimento (~a partir de 06/11): não
  carregar posição comprada até aí.

## 7. Estratégia escrita (cap. 11.21) — antes de montar

- [ ] **Tese escrita:** evento binário + transmissão fiscal → movimento forte em qualquer
      direção ou alta da vol implícita.
- [ ] **Perda máxima ≤ 1–1,5% do patrimônio** da conta. Definida em R$; nunca aumentada.
- [ ] **Lucro máximo** calculado com a cadeia real (largura da asa − débito líquido).
- [ ] **Entrada escalonada:** 1/3 agora · 1/3 ~10 pregões antes do 1º turno · 1/3 só se a IV
      não inflou (senão, calendar: vender outubro, comprar novembro).
- [ ] **Saída no lucro:** realizar 50–75% se o prêmio dobrar, ou no gap de segunda 05/10.
      Não segurar as 4 pernas até o vencimento.
- [ ] **Stop de tempo:** ~10 pregões antes do venc., se perdendo e dentro da faixa, desmontar.
      Tolerância 15–20% do capital da operação (*Axiomas de Zurique*).
- [ ] **Rolagem (cap. 6.7):** se o ativo andar >4–5% antes do evento, reancorar o strangle em
      torno do novo spot.
- [ ] **Lembrete:** é soma zero. Vender as asas = alguém compra cauda de você. Sem borda
      garantida, só risco definido.

### Antes de enviar a ordem

- [ ] Série cobre **1º e 2º turno** (vencimento de novembro, não outubro).
- [ ] **Ibovespa VIX / IV da série** anotada vs. IV histórica → decide strangle comprado vs.
      calendar.
- [ ] **Faixa de empate** recalculada com os prêmios reais.
- [ ] **Perda máxima ≤ o teto de capital** definido.
- [ ] **Corretagem das 4 pernas < 15–20% do prêmio líquido** (cap. 11.20). Se não passar,
      usar strangle de 2 pernas com stop de tempo apertado.
- [ ] **Liquidez conferida:** spread de compra/venda aceitável nas 4 séries.
