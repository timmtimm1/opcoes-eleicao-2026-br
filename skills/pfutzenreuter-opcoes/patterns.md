# Patterns — Operações e Técnicas

Todas as operações-modelo do livro usam: spot $100, juro 12% a.a., vol 25% a.a., 2 meses, S1=$100, S2=$106 (ou $94), S3=$112.
Convenção: S1 é sempre a opção de strike mais baixo; "vendido"/"comprado" descreve o caráter líquido da operação.

## Método universal de avaliação de operação (Ch 11.17)
**Quando usar**: qualquer operação, mesmo não listada no livro.
**Como**:
1. Gráfico de lucro no vencimento = soma dos valores intrínsecos das pernas (linhas).
2. Achar os pontos de empate (spots de lucro→prejuízo).
3. Calcular a chance de o spot terminar na faixa lucrativa (distribuição log-normal — Ch 6, calculadora ou planilha). **Passo mais importante.**
4. Gregas totais = soma das pernas (ação: Δ=+100%, resto 0; dinheiro: tudo 0).
**Trade-offs**: passos 1–2 são triviais; o passo 3 exige "sentir" como taxa de juros + volatilidade definem o preço futuro.

## Carteira replicante / hedge de delta (Ch 3.4, 10.4)
**Quando usar**: entender de onde vem o valor da opção; delta-hedge teórico.
**Como**: tomar dinheiro emprestado + comprar uma fração `delta` de ação + aplicar o resto em renda fixa. Reajustar o delta diariamente conforme o mercado se move.
**Trade-offs**: puramente teórica — o reajuste diário gera custos de corretagem proibitivos.

## Volatilidade implícita por tentativa-e-erro (Ch 9.3)
**Quando usar**: descobrir a estimativa de mercado da volatilidade futura; saber se a opção está cara/barata.
**Como**: variar σ em Black-Scholes até o prêmio teórico igualar o de mercado (interpolação linear ou método de Newton num computador).
**Trade-offs**: sem fórmula fechada; precisa de ferramenta. É a métrica que os profissionais usam no lugar do prêmio absoluto.

## Anualização de volatilidade (Ch 6.1)
**Quando usar**: converter volatilidade de um período para outro.
**Como**: multiplicar pela **raiz quadrada** do fator de tempo (`σ_anual = σ_mensal · √12`). Nunca pelo fator direto.

---

## Operações elementares (risco ilimitado — evitar isoladas)

### Comprar call a seco (Ch 11.1)
**Quando**: garantir preço de compra futura de ações; "dica quente" legal; ou opção **DITM/LEAPS** como alavancagem "séria".
**Como**: comprar 1 call. Risco = 100% do prêmio; lucro ilimitado; empate = strike + prêmio.
**Trade-offs**: call ATM tem ~45% de perder tudo. Theta corrói rápido; encerrar cedo. Preferir ITM longe do vencimento.

### Comprar put a seco (Ch 11.2)
**Quando**: perna de seguro numa operação de capital protegido; raramente isolada.
**Como**: comprar 1 put. Risco = prêmio; lucro máx = strike; empate = strike − prêmio.
**Trade-offs**: mau investimento isolado; sorriso encarece puts OTM.

### Vender call a seco (Ch 11.3)
**Quando**: quase nunca para o pequeno investidor (risco ILIMITADO).
**Como**: lançar 1 call, depositar margem ≈ 3× o prêmio. Lucro máx = prêmio; empate = strike + prêmio.
**Trade-offs**: se a ação dispara, a obrigação supera muito o prêmio. Theta a favor.

### Vender put a seco (Ch 11.4)
**Quando**: investidor quer adquirir a ação e já tem o dinheiro — lança puts OTM curtas até ser exercido.
**Como**: lançar 1 put, margem ≈ 3× o prêmio. Risco = strike; lucro máx = prêmio; empate = strike − prêmio.
**Trade-offs**: chances um pouco melhores que vender call (mercado tende a subir).

---

## Operações compostas (risco limitado ao investimento)

### Venda coberta de call (Ch 11.6)
**Quando**: investidor de longo prazo em ações querendo remuneração adicional, em mercado "comportado". Repetir todo mês, lançando 1 mês antes do vencimento.
**Como**: possuir 1 ação + lançar 1 call (ATM, ou OTM próxima da ATM). Margem zero (a ação garante). Lucro máx = prêmio + strike − custo da ação.
**Trade-offs**: **theta sempre positivo**. Lucro limitado; exige muito capital; paga IR sobre o prêmio. Vender OTM reduz risco de exercício e ganha mais se exercido. Não desmontar antes da hora.

### Venda coberta de put (Ch 11.7)
**Quando**: só se você gosta da ação e não se incomoda de comprá-la acima do preço.
**Como**: ter o strike em dinheiro + lançar 1 put (ATM ou OTM próxima). Risco máx = strike.
**Trade-offs**: semelhante à venda coberta de call; exige capital = strike.

### Capital protegido / synthetic long call (Ch 11.8)
**Quando**: quem não pode perder dinheiro no curto prazo.
**Como**: comprar 1 ação + comprar 1 put (ATM ou levemente OTM), **de prazo mais longo possível**. Risco máx = prêmio da put; lucro ilimitado.
**Trade-offs**: ATM protege 100% mas é cara; OTM protege ~95% barato. Prazo longo deprime a put (juros) → só recupera o capital perto do vencimento (resgate ~30 dias).

### POP BOVESPA (Ch 11.9)
**Quando**: capital protegido "de graça", abrindo mão de parte da alta.
**Como**: comprar 10 ações + comprar 10 puts levemente OTM + vender 2–3 calls ATM (proporção ~2:10 a 3:10 para proteger ~95%). Risco máx ~nulo; lucro ilimitado; margem zero.

### Renda fixa + opções (Ch 11.10)
**Quando**: capital grande, quer bater a renda fixa sem arriscar o principal.
**Como**: aplicar em RF, operar **só os juros** (de preferência em spreads). Lucro extra volta para o bolo (evita martingale). Risco máx = nulo.

---

## Spreads (Ch 11.11–11.16) — retorno sobre capital altíssimo (investimento = só a margem)

### Call credit spread / reversão / trava de baixa (Ch 11.12)
**Quando**: apostar que o mercado cai ou não sobe; mercado "esticado" (Lee Lowell). Montar OTM, no máx ATM.
**Como**: vender call S1 + comprar call S2 > S1. Recebe prêmio líquido = lucro máx. Risco máx = (S2−S1) − prêmio líq. Empate = S1 + prêmio líq. Margem = S2−S1.
**Trade-offs**: ROM enorme (ex.: $6 margem, $1 prêmio, 1 mês → 16% a.m.). Pior caso (ambas ITM): perde quase toda a margem. Theta a favor na faixa lucrativa, contra na de prejuízo → desmontar ao entrar no prejuízo. Não paga IR se terminar perdedora. Baixa corretagem (tudo vira pó).

### Put credit spread (Ch 11.13)
**Quando**: apostar na alta; chances um pouco melhores que a trava de baixa.
**Como**: vender put S1 + comprar put S2 < S1. Risco máx = S1−S2; lucro máx = prêmio líq.; empate = S2 − prêmio líq.; margem = S1−S2.
**Trade-offs**: quase inviável no Brasil (puts sem liquidez). Theta mais negativo na faixa de prejuízo → montar bem OTM.

### Call debit spread / trava de alta (Ch 11.14)
**Quando**: apostar na alta com razoável certeza de que o mercado não cai até os strikes. Montar **ITM**.
**Como**: comprar call S1 + vender call S2 > S1. Paga prêmio líquido. Risco máx = prêmio líq. pago; lucro máx = (S2−S1) − prêmio líq.; empate = S2 − prêmio líq.; margem zero.
**Trade-offs**: pior caso (ambas viram pó abaixo de S1): perde tudo. Theta mais negativo na faixa de prejuízo. Boas chances (aposta na alta).

### Call ratio backspread / "Boi" (Ch 11.15)
**Quando**: apostar numa alta **explosiva** com pouco capital.
**Como**: vender X calls S1 + comprar Y>X calls S2 (ratio 3:2, 2:1, 3:1), buscando prêmio líquido ~zero → capital = só a margem = (S2−S1)·X. Risco máx = (S2−S1)·X; lucro ilimitado; empate = S2 + (S2−S1)·X/Y.
**Trade-offs**: faixa de prejuízo entre S1 e S2 (a mais provável) → **montar com as duas opções ITM**. Theta fortemente negativo sempre → desmontar assim que houver lucro, com prazo máximo. Pode perder 100% da margem.

### Call ratio spread / "Vaca" (Ch 11.16)
**Quando**: apostar que o mercado fica entre S1 e S2; gestão ativa.
**Como**: comprar 1 call S1 + vender X calls S2 + comprar X−1 calls S3 (preferir versão **com S3**, risco limitado). Montar zero-a-zero. Risco máx = (S3−S2)·(X−1); lucro máx = S2−S1; empate ≈ S2 + (S3−S2)/X; margem = (S3−S2)·(X−1).
**Trade-offs**: operação "vendida", theta positivo em larga faixa. Faixa de transição estreita mas delta suave longe do vencimento. **Nunca abandonar até o vencimento** (Bastter: ver o "rebanho" 2×/dia).

---

## Técnica de gestão: elabore uma estratégia antes de montar (Ch 11.21)
**Quando**: toda operação.
**Como**: definir por escrito — lucro/prejuízo máximos, chances de vitória, ponto de entrada, ponto de saída se der certo, o que fazer se o mercado virar. Tolerância a perdas de 15–20% (*Axiomas de Zurique*), sempre com espaço para oscilação normal.
**Trade-offs**: não aumenta a taxa de acerto acima do que a soma zero permite; serve para controle emocional e justificar a operação para si mesmo. Erro fatal do iniciante: realizar lucros pequenos cedo e deixar as perdas crescerem.
