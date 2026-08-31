# Capítulo 11: Lucratividade das operações com opções

## Core Idea
Junta tudo: analisa cada operação pela lucratividade no vencimento (pior caso), pelas chances de vitória (faixa lucrativa × probabilidade do spot) e pelas gregas totais. Regra de ouro do capítulo: **toda operação só com opções é soma zero** — trate qualquer recomendação com espírito crítico. As 4 operações elementares têm risco ilimitado; as compostas cancelam riscos mutuamente.

## Frameworks Introduced

### Como analisar qualquer operação (11.17)
1. **Gráfico de lucratividade no vencimento** = soma dos valores intrínsecos das pernas (gráficos lineares). Buscar o nome da operação na internet também serve.
2. **Pontos de empate** = spots onde a operação passa de lucro a prejuízo (o gráfico entrega).
3. **Chances de vitória** (passo mais difícil e importante) = probabilidade de o spot terminar na faixa lucrativa (Ch 6 / calculadora / planilha log-normal).
4. Gregas totais (delta/gama/theta) = soma das pernas; úteis para saber o que acontece com o valor da carteira ao longo do tempo, mas não essenciais.

### Gregas de ativos não-opção (11.5)
| Grega | Ação | Dinheiro |
|---|---|---|
| Delta | +100% | 0 |
| Gama / Theta / Vega | 0 | 0 |
| Rho | negativo | 0 |

### Parâmetros das operações-modelo (Tabela 11.1)
Spot na montagem $100; juro 12% ao ano; vol 25% ao ano; 2 meses até o vencimento; S1=$100, S2=$106 ou $94, S3=$112; prêmios por Black-Scholes.

## Operações elementares (11.1–11.4) — todas com risco ilimitado, evitar

| Operação | Risco máx | Lucro máx | Spot de empate | Melhor caso | Delta/Gama/Theta |
|---|---|---|---|---|---|
| **Comprar call a seco** | 100% do prêmio | Ilimitado | strike + prêmio pago | ITM longe do vencimento, realizar cedo | +/+/− |
| **Comprar put a seco** | prêmio pago | valor do strike | strike − prêmio pago | comprar e vender longe do vencimento | −/+/− |
| **Vender call a seco** | **ILIMITADO** | prêmio recebido | strike + prêmio recebido | vender ATM, mercado parado | −/−/+  (margem ≈ 3× prêmio) |
| **Vender put a seco** | valor do strike (≈ ilimitado) | prêmio recebido | strike − prêmio recebido | vender ATM, mercado sobe | +/−/+  (margem ≈ 3× prêmio) |

- Comprar call ATM: ~45% de perder tudo, ~20% de perder boa parte, só ~35% de algum lucro. Perder muito capital é desastroso (ganhar 200% e perder 75% = 50% mais pobre).
- **Compras a seco** só se justificam: (a) garantir preço de compra/recompra futura de ações; (b) "dica quente" (lembrando que insider é ilegal); (c) opções **DITM/LEAPS** ("investir na ação de forma alavancada", theta ameno).
- Vender put a seco tem sentido se o investidor quer adquirir a ação e já tem o dinheiro: lança puts OTM curtas, embolsa prêmios, até ser exercido.

## Operações compostas (todas com risco limitado ao investimento)

### 11.6 Venda coberta de call — possuir 1 ação + vender 1 call
- Risco máx: só a desvalorização da ação. Lucro máx: prêmio + strike − custo da ação. Empate: custo da ação − prêmio recebido. Margem: zero (ação é a garantia).
- **Theta sempre positivo** — o tempo está sempre a favor. Repetir mês após mês (não vale uma vez só). Melhor momento de lançar: exatamente 1 mês antes do vencimento.
- Índice **BXM (BuyWrite)** de Chicago: rendimento médio ~igual à ação pura, mas com menos volatilidade → rendimento efetivo um pouco maior (Ch 6: volatilidade deprime o rendimento).
- Alerta de Fischer Black: só dá lucro consistente em mercados "comportados" (preços numa faixa conhecida).
- Vender OTM (próxima da ATM): menos risco de exercício, aproveita o sorriso da vol, e se exercido recebe mais pela ação. Desvantagens: exige muito capital; paga IR sobre o prêmio.
- Autor: só vende com strike próximo ao custo da ação; evita quando a ação caiu muito e pressente alta.

### 11.7 Venda coberta de put — ter o strike em dinheiro + vender 1 put
- Risco máx: valor do strike (aceitar ação muito depreciada). Lucro máx: prêmio. Só fazer se gostar da ação subjacente. Vender ATM ou próxima OTM.

### 11.8 Capital protegido — comprar 1 ação + comprar 1 put ATM ou levemente OTM
- Também chamada **synthetic long call**. Risco máx: prêmio da put. Lucro máx: ilimitado. Ação sobe → ganha, put vira pó. Ação cai → exerce a put, recupera ~o capital.
- ATM protege melhor mas é cara; OTM protege fração menor (95% em vez de 100%) mais barato. **Comprar put de prazo mais longo possível** (barateia o seguro por unidade de tempo) — raciocínio inverso da venda coberta. Prazo longo deprime a put (juros) → esperar perto do vencimento para recuperar o capital (daí o resgate de ~30 dias nos fundos de capital protegido).

### 11.9 POP BOVESPA — comprar 10 ações + comprar 10 puts levemente OTM + vender 2–3 calls ATM
- As calls vendidas financiam as puts → proteção "de graça", em troca de abrir mão de parte da alta. Risco máx: praticamente nulo. Proporção 2:10 a 3:10 para proteger ~95% do capital.

### 11.10 Renda fixa + opções — aplicar em RF e operar só os juros
- Risco máx: nulo (nunca arriscar além dos juros; lucro extra volta para o bolo — evita martingale). Exige capital grande; melhor tipo de operação para os juros: alguma variante de spread.

## Spreads (11.11) — explorar a diferença de prêmio entre 2+ opções
- Origem da diferença: **strikes diferentes na mesma série** (a única analisada), calendar spread (vencimentos), sorriso da vol, ativos diferentes.
- **Debit spread**: desembolso líquido na montagem. **Credit spread**: recebimento líquido (mais comum).
- Visão de mercado: **Bull** (lucro máx na alta), **Bear** (lucro máx na queda).
- Atrativo: investimento inicial = só a margem → **retorno sobre capital altíssimo** (ex.: $6 de margem, $1 de prêmio, 1 mês → 16% ao mês).

| Spread | Montagem | Ganha quando | Risco máx | Lucro máx | Empate | Margem |
|---|---|---|---|---|---|---|
| **Call credit spread** (reversão / trava de baixa) | vender call S1, comprar call S2 > S1 | mercado cai / não sobe (ambas viram pó) | (S2−S1) − prêmio líq. | prêmio líq. recebido | S1 + prêmio líq. | S2−S1 |
| **Put credit spread** | vender put S1, comprar put S2 < S1 | mercado sobe (puts ficam OTM) | S1−S2 | prêmio líq. recebido | S2 − prêmio líq. | S1−S2 |
| **Call debit spread** (trava de alta) | comprar call S1, vender call S2 > S1 | mercado sobe (ambas viram ITM) | prêmio líq. pago | (S2−S1) − prêmio líq. pago | S2 − prêmio líq. pago | zero |
| **Call ratio backspread** ("Boi") | vender X calls S1, comprar Y>X calls S2 | mercado **explode** acima de S2 | (S2−S1)·X | ilimitado | S2 + (S2−S1)·X/Y | (S2−S1)·X |
| **Call ratio spread** ("Vaca") | comprar 1 call S1, vender X calls S2, comprar X−1 calls S3 | mercado fica **entre S1 e S2** | (S3−S2)·(X−1) | S2−S1 | ~S2 + (S3−S2)/X | (S3−S2)·(X−1) |

### Notas por spread
- **Trava de baixa**: lucro máx quando ambas viram pó. Pior caso: mercado sobe muito, ambas ITM → prejuízo = S2−S1 (menos o prêmio já recebido). Montar OTM (no máx ATM); evitar com vol implícita muito baixa. Theta a favor na faixa lucrativa, contra na faixa de prejuízo → desmontar cedo ao entrar no prejuízo. Lee Lowell: usar para apostar contra novas altas quando o mercado está "esticado". Reversão ITM só serve para levantar dinheiro rápido (com ações como margem).
- **Put credit spread**: igual à trava de baixa mas ganha na **alta**; chances um pouco maiores (mercado tende a subir). Quase inviável no Brasil (puts sem liquidez). Theta mais negativo na faixa de prejuízo do que positivo na de lucro (efeito juros sobre puts) → montar bem OTM.
- **Trava de alta**: paga prêmio líquido para montar. Melhor chance montando **ITM** quando há razoável certeza de que o mercado não cai até os strikes. Pior caso: mercado abaixo de S1, ambas viram pó, perde tudo. Sem margem (S1 lastreia S2). Boas chances (aposta na alta).
- **Boi (backspread ratio)**: X reversões + (Y−X) compras a seco; ratio típico 3:2, 2:1, 3:1. Monta-se buscando prêmio líquido ~zero → único capital é a margem. Faixa de prejuízo entre S1 e S2 (a mais provável!) → montar **com as duas opções ITM** para jogar a faixa de prejuízo para um patamar improvável, e para que S1 (vendida) seja a opção "cara" do sorriso. Delta positivo e crescente (pode passar de 100%), gama muito positivo, **theta fortemente negativo em qualquer situação** → o tempo está sempre contra; desmontar assim que houver lucro, com prazo máximo definido.
- **Vaca (ratio spread)**: debit spread (S1→S2) financiado por vários credit spreads (S2→S3). Vencedora se o mercado fica **entre S1 e S2**. Preferir a versão **com S3** (risco limitado); sem S3 o risco é ilimitado. Montar zero-a-zero. Sorriso: comprar S1 "barato" (ATM), vender S2 "caro" (OTM). Operação "vendida": delta negativo nos patamares prováveis, **theta positivo em larga faixa**. Faixa de transição estreita, mas delta suave longe do vencimento → dá tempo de desmontar.

## Worked Example
**Trava de baixa ATM** (S1=$100, S2=$106), spot $100, 2 meses. Recebe ~$1 de prêmio líquido; margem $6.
- Lucro máx = $1 (ambas viram pó, spot ≤ $100 no vencimento). ROM = $1/$6 ≈ **16% ao mês**.
- Empate = $100 + $1 = $101.
- Pior caso = spot ≥ $106: exerce S2, é exercido em S1, prejuízo = $6 − $1 = **−$5** (perde ~83% da margem).
- Chance de sucesso "média" por ser ATM; montar mais OTM eleva as chances.
- Gestão: theta a favor enquanto spot < $101; ao aproximar-se de $101–$106, o theta vira contra e o custo de recompra sobe → desmontar. A área de transição entre lucro e prejuízo dá tempo para decidir — vantagem da operação.

## Anti-patterns
- **Realizar lucros pequenos cedo e deixar as perdas crescerem** (11.21): "estratégia" que garante prejuízo — fica só com a "banda podre" dos rendimentos. O erro clássico do iniciante.
- **Cortar perdas cedo demais** sem espaço para oscilação normal: todas as operações "morrem no prejuízo"; tempestade de stops. *Os Axiomas de Zurique*: tolerância de 15–20%.
- **Vaca abandonada até o vencimento**: muitas terminariam no prejuízo; exige acompanhamento (Bastter: ver o "rebanho" 2×/dia).
- **Deixar de considerar corretagem** (11.20): corretagem fixa de R$20 → uma vaca custa até R$120. Exercício custa igual ou mais. Pouco capital → operações simples que terminam com tudo virando pó (venda coberta, trava de baixa).
- **Achar que operação "vendida" bate a soma zero**: pode ser só escassez de lançadores mantendo o prêmio acima do "valor justo" (hipótese do 11.19) — não nega a soma zero.

## Key Takeaways
1. Toda operação só-opções é soma zero; operações com ação/dinheiro rendem, no longo prazo, o que o ativo convencional renderia sozinho.
2. Analise: lucro/prejuízo no vencimento → pontos de empate → **chance de vitória** → gregas totais.
3. Elementares têm risco ilimitado; compostas travam o risco no investimento.
4. Venda coberta e trava de baixa: theta a favor, boas chances (mercado tende a subir), baratas em corretagem — as favoritas para pouco capital.
5. Capital protegido / POP: seguro para quem não pode perder no curto prazo.
6. Ratio (boi/vaca): o sorriso da vol importa mais; risco de perder 100% da margem.
7. **Elabore sua própria estratégia** (11.21) antes de montar: lucro/prejuízo máximos, chances de vitória, ponto de entrada, ponto de saída no lucro, o que fazer se o mercado virar. Objetivo: controle emocional, não 100% de acerto (impossível — é soma zero).
8. Operações recomendadas: **Bastter** (tropicalizado p/ BOVESPA) — venda coberta de call, reversões cobertas, vacas cobertas. **Lee Lowell** — vendas cobertas (call e put), reversões, compra de call DITM, vacas. Ambos: operações "vendidas" e de risco limitado.

## Connects To
- **Ch 6**: probabilidade do spot final define a chance de vitória.
- **Ch 9**: vol implícita alta favorece operações vendidas; sorriso da vol encarece ITM/OTM.
- **Ch 10**: gregas totais = soma das pernas; theta positivo = tempo a favor.
- **Ch 12**: as mesmas operações simuladas com cotações reais da BOVESPA (série VALEE, abr–mai 2008).
