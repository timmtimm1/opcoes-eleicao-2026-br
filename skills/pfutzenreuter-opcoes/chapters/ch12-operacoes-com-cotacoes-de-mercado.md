# Capítulo 12: Operações com cotações de mercado

## Core Idea
Simula todas as operações do Ch 11 com cotações reais da série VALEE (call sobre VALE5, vencimento 19/maio/2008), montadas em 7 de abril. Cada operação recebe uma estratégia formulada (não é sugestão) e é comparada com a "estratégia avestruz" (esperar até o vencimento). Só calls, porque a BOVESPA só tem liquidez em calls.

## Reference Tables

Cotações de 7/abr/2008 (VALE5 = $52,35), série E (venc. 19/maio):

| Código | Cotação | Situação | Vol implícita | Delta% | Gama% | Theta $/dia |
|---|---|---|---|---|---|---|
| VALEE42 | 11,35 | DITM | 55,75% | 90,8 | 1,7 | −0,03 |
| VALEE46 | 7,46 | ITM | 40,60% | 86,5 | 3,0 | −0,03 |
| VALEE48 | 5,51 | ITM | 32,50% | 83,1 | 4,4 | −0,03 |
| VALEE50 | 4,20 | ITM | 35,00% | 71,1 | 5,5 | −0,04 |
| VALEE52 | 2,89 | ATM | 33,50% | 59,1 | 6,5 | −0,04 |
| VALEE54 | 1,91 | OTM | 33,00% | 45,8 | 6,8 | −0,03 |
| VALEE56 | 1,16 | OTM | 32,00% | 32,7 | 6,4 | −0,03 |
| VALEE58 | 0,65 | OTM | 31,25% | 21,4 | 5,3 | −0,02 |
| VALEE60 | 0,47 | OTM | 34,00% | 15,6 | 4,0 | −0,02 |

- Sorriso da vol com mínimo entre strikes 48 e 58 → o mercado estimava $48–$58 como faixa mais provável para VALE5 em 19/maio.
- Vol implícita **baixa** para o padrão brasileiro → opções algo baratas → operações "compradas" poderiam sair lucrativas.
- 11/abr: Vale distribuiu $0,40 de dividendo → todos os strikes caíram $0,40 (VALEE50 virou strike $49,60).
- **30/abr: Brasil recebeu grau de investimento da S&P** → forte subida do mercado. Fator "atípico" que dominou todos os resultados.
- 19/maio ao meio-dia: VALE5 = $58,71.

## Worked Example — resultados por operação

| Operação (estratégia) | Seguindo a estratégia | Avestruz (até o vencimento) |
|---|---|---|
| **Compra a seco** (segurar até 25/abr; realizar se lucro > $1) | Todas no prejuízo (prazo curto evitou perda de 100% nas OTM) | ITM/ATM lucraram 51–168%; OTM (≥ VALEE60) viraram pó, −100% |
| **Venda coberta de call** (vender ATM/OTM que remunere ≥ 2%; até o vencimento) | Todas exercidas; lucro de 2,8% a 8,4% sobre o capital em ações. VALEE54/56 (OTM) exercidas acima do custo → melhor lucratividade | idem |
| **Call credit spread / trava de baixa** (não fazer se pagar < 25% do risco; realizar prejuízo a partir de 6/mai se entrar na faixa de prejuízo total) | Quase todas no prejuízo; o grau de investimento "entornou o caldo". Estratégia evitou prejuízos maiores mas não salvou VALEE56/58 | Todas ITM → todas custam $2 na liquidação; prejuízo de 3% a 292% do prêmio líquido |
| **Call debit spread / trava de alta** (não pagar > 66% do risco; realizar se lucro ≥ 50%; realizar prejuízo a partir de 6/mai) | Enxurrada encerrada em 5–6/mai; lucros de ~11–52% nas bem posicionadas, prejuízos nas muito OTM | Lucros de 53% a **511%** nas ITM/ATM; VALEE60/62 e acima, −100% |
| **Backspread ratio / boi** (montar gastando o mínimo; até 25/abr; realizar antes se lucro > 15% ROM) | Maioria no prejuízo; o melhor (14,25%) tinha as **duas opções ITM**; bois com opção ATM deram o maior prejuízo | Bois ATM/ITM lucrariam 37–138% ROM |
| **Call ratio spread / vaca** (montar mínimo; gestão diária de lucro/prejuízo até o vencimento) | Quase todas no lucro; único prejuízo pequeno. Estratégia foi decisiva para gerenciar | Muitas terminariam **no prejuízo** se abandonadas |

## Key Concepts
- **A fronteira entre lucro e prejuízo é drástica**: VALEE58 até o vencimento = +70%; VALEE60 = pó. VALEE58/60 (debit spread) = +511%; VALEE60/62 = −100%.
- Operações "compradas" (compra a seco, debit spread, boi) que apostaram na alta e perseveraram até perto do vencimento tiveram um ótimo mês — contrariando o prognóstico geral. Stops de tempo curtos fizeram perder os frutos da subida final.
- Opções **profundamente ITM** foram as melhores para apostar na alta — corrobora a recomendação de comprar call DITM.
- Reversões (credit spreads, prediletas de Lee Lowell) sofreram muito — e Lowell costuma fazê-las com puts (apostando na alta), inviável no Brasil.
- Vendas cobertas: pequeno e honesto lucro, como esperado.
- Vacas: grande manejabilidade sob gestão ativa; catastróficas se abandonadas.

## Anti-patterns
- **Stop de tempo curto demais** numa aposta comprada correta: perdeu-se a subida forte às vésperas do vencimento.
- **Abandonar vaca/boi até o vencimento**: exigem acompanhamento contínuo (Bastter: 2×/dia).
- **Adotar as estratégias do capítulo cegamente**: são ilustrativas, não recomendações.

## Key Takeaways
1. Não existe "mercado típico"; cada período tem sua particularidade (aqui, o grau de investimento).
2. Definir prazo de desfazimento curto protege contra perda total nas compras a seco OTM — mas pode cortar o lucro cedo.
3. Venda coberta OTM brilha quando a expectativa de mercado é boa (exercido acima do custo).
4. Ratio spreads (boi/vaca) são operações de gestão ativa, não de "sentar e esperar".
5. Vol implícita baixa na montagem realmente sinalizou vantagem para operações compradas.

## Connects To
- **Ch 11**: cada operação aqui é a versão "ao vivo" da teoria.
- **Ch 9**: o sorriso da vol e o nível da vol implícita orientaram as escolhas.
- **Ch 1 / Ch 11.21**: "toda operação deve ter uma estratégia" — e ainda assim a taxa de acerto fica longe de 100%.
