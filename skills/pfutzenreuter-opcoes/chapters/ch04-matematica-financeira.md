# Capítulo 4: Matemática financeira elementar

## Core Idea
Avaliar opção exige antes saber avaliar ativos simples: um ativo vale a renda que gera dividida pela taxa de juros, e $1 no futuro vale menos que $1 hoje (desconto ao valor presente). Opções usam capitalização contínua (e^juro).

## Frameworks Introduced
- **Valor do ativo = renda / taxa de retorno**. Ativo que rende $1.200/ano a 12% vale $10.000. Se o preço difere muito, ou o mercado está maluco ou a renda futura esperada vai mudar.
  - P/L (preço/lucro) = inverso da taxa de retorno. P/L 8 ≈ 12,5% ao ano.
- **Desconto ao valor presente**: `VP = VF · e^(−r·t)` (expoente negativo). $100 em 2 anos a 12% valem menos hoje.
- **Capitalização contínua**: aumentar o nº de capitalizações eleva a taxa efetiva, mas com teto = `e^(taxa nominal)`. 12% ao ano contínuo = 12,7497%. Usada em finanças porque e^x é fácil de integrar (necessário na avaliação de opções) e modela bem carteira diversificada (cada empresa paga em dia diferente).
- **Taxa nominal vs. efetiva**: "12% ao ano capitalizado mensalmente" = 1% ao mês = 12,68% ao ano efetivo. "10% ao mês" anunciado como "120% ao ano" = 313% efetivo.

## Key Concepts
- **Ativos que não respeitam a regra renda/juros** têm características de opção: ações com yield abaixo da SELIC, obras de arte (sem renda, valor pela escassez), terrenos baldios (valor = expectativa futura), jazidas com prazo longo. O valor de revenda = expectativa de evento futuro positivo descontado.
- **SELIC**: taxa que o governo paga; a mais baixa da economia. Quando muda, todos os ativos são reavaliados (daí a bolsa subir quando o juro cai).
- **Juro composto** trata principal e juros como uma coisa só (exponencial); juro simples "carimba" separado e favorece o mau devedor.

## Worked Example
Empresa que paga $100/ano em dividendos, SELIC 12%, prêmio de risco 6% → ação vale ~$555,55 (18% de 555,55 = 100). Título de renda fixa pagando $100/ano vale $833,33 (sem risco, 12%). Se a SELIC cai para 8%: a ação passa a $714,28 ($100/0,14) e o título a $1.250 ($100/0,08). Por isso a bolsa sobe quando o juro cai.

## Anti-patterns
- **Confundir taxa nominal com efetiva**: fonte comum de enganação comercial.
- **Achar que capitalizar em períodos menores é "fonte de dinheiro"**: converge para o limite e^juro.

## Key Takeaways
1. Avaliar ativo = estimar rendimentos e dividir pela taxa de juros. Todo o resto gira em torno disso.
2. Opção garante preço fixo futuro (strike) → o desconto ao valor presente é central para opções europeias.
3. Opção americana tem o strike sempre no valor presente (exercível hoje).
4. Prefira capitalização contínua nas fórmulas de opções.

## Connects To
- **Ch 5**: CAPM ajusta a taxa de juros pelo risco do ativo.
- **Ch 7**: o desconto do strike explica a paridade put-call.
- **Ch 9**: e^(−rt) aparece dentro de Black-Scholes.
