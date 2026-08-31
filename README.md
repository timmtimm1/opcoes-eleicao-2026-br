# Opções · Eleição 2026 (Brasil)

Workbench interativo para montar **operações de volatilidade em opções** (IBOV, PETR4, bancos)
na janela da eleição presidencial de **4 de outubro de 2026**, construído sobre o livro
*Investindo no Mercado de Opções* (Elvis Pfützenreuter, Novatec).

O repositório reúne **a ferramenta**, **a skill de conhecimento extraída do livro**, **a
estratégia escrita** e a **automação** que mantém as cotações atualizadas todo dia útil.

> ⚠️ **Conteúdo educativo, não recomendação de investimento.** O mercado de opções é soma zero
> e nenhuma estratégia garante lucro. Preços, volatilidade implícita e prêmios exibidos são
> ilustrativos — confirme a cadeia real na corretora, além de tributação e custos, antes de operar.

---

## Links

| O quê | Onde |
|---|---|
| Site (auto-atualizado, GitHub Pages) | `https://timmtimm1.github.io/opcoes-eleicao-2026-br/` |
| Artifact original (claude.ai) | `https://claude.ai/code/artifact/5d0c89e9-3418-4325-89f3-c38662d7be4a` |
| Estratégia escrita | [`docs/STRATEGY.md`](docs/STRATEGY.md) |
| Como tudo foi construído | [`docs/PROCESS.md`](docs/PROCESS.md) |
| Skill do livro | [`skills/pfutzenreuter-opcoes/`](skills/pfutzenreuter-opcoes/) |

---

## O que a ferramenta faz

- **Workbench de payoff** — escolhe o ativo (IBOV / PETR4 / BBAS3 / ITUB4 / BBDC4), ajusta
  spot, IV, prazo, juro e a distância dos strikes; desenha o diagrama de payoff no vencimento
  com pontos de empate, perda/ganho máximo e o sinal das gregas. Prêmios por Black-Scholes ou
  digitados do mercado. Alterna *strangle* simples (2 pernas) ↔ risco definido (4 pernas).
- **Chance de terminar fora da faixa** — estimador log-normal (cap. 6 do livro): P(dentro) /
  P(fora) da faixa dos strikes comprados, e o movimento de 1 desvio padrão.
- **Janela ideal de compra** — por ativo, calcula a faixa de datas para comprar, o dia da
  semana sugerido, o horário do pregão e o status ao vivo ("JANELA ABERTA", "ainda cedo",
  "tarde — theta pesado", "pós-evento"). O ponto "hoje" anda sozinho pelo calendário real.
- **Sensibilidade eleitoral** de PETR4 e dos bancos, e uma **legenda filtrável** com todos os
  termos técnicos em português claro.
- **Estratégia escrita (cap. 11.21)** — checklist com barra de progresso, salvo no navegador.

### O que se atualiza sozinho

| Parte | Atualiza | Como |
|---|---|---|
| Contagem regressiva, "janela ideal", status, ponto "hoje" | **a cada abertura da página** + de hora em hora | JavaScript no navegador, relógio real |
| Cotações (spot) de PETR4/IBOV/BBAS3/ITUB4/BBDC4 | **dias úteis, ~18:15 e ~08:45 BRT** | GitHub Actions → `site/data.json` → `fetch()` no site |
| Nível do Ibovespa no topo | idem | idem |
| Volatilidade implícita (IV), odds do Polymarket, pesquisas, texto da pesquisa | **semanal** (se a rotina Claude estiver ligada) ou manual | ver [`automation/SCHEDULE.md`](automation/SCHEDULE.md) |

O `fetch('data.json')` só funciona no GitHub Pages. No artifact do claude.ai o sandbox bloqueia
rede — lá a página usa os valores embutidos e continua 100% funcional, só sem dados do dia.

---

## Estrutura do repositório

```
opcoes-eleicao-2026-br/
├── site/
│   ├── index.html            # a ferramenta (entrypoint do GitHub Pages)
│   └── data.json             # snapshot de cotações — escrito pelo GitHub Actions
├── skills/
│   └── pfutzenreuter-opcoes/  # skill extraída do livro (SKILL.md, chapters/, glossary, patterns, cheatsheet)
├── automation/
│   ├── update_data.py        # busca cotações (Yahoo Finance / brapi.dev), reescreve data.json
│   ├── claude-routine.md     # prompt que a rotina Claude semanal executa
│   └── SCHEDULE.md           # cron do Actions + rotina Claude: como mudar / pausar / desligar
├── docs/
│   ├── PROCESS.md            # last30days + book-to-skill + artifact-design, passo a passo
│   ├── STRATEGY.md           # a operação e a estratégia escrita (cap. 11.21)
│   └── RESEARCH-2026-08-31.md# saída bruta da pesquisa /last30days + fontes web
├── .github/workflows/update.yml
├── LICENSE
└── README.md
```

---

## Automação

### 1. GitHub Actions (grátis, sempre ligado)

`.github/workflows/update.yml` roda:

- **cron** `15 21 * * 1-5` (18:15 BRT) e `45 11 * * 1-5` (08:45 BRT), dias úteis;
- **manual** pela aba *Actions → atualizar-e-publicar → Run workflow*;
- **a cada push** na `main`.

O job `atualizar` executa `automation/update_data.py`, que busca o fechamento/último negócio de
cada ativo no **Yahoo Finance** (sem token) e, como reserva, no **brapi.dev** (token opcional em
`Settings → Secrets → BRAPI_TOKEN`). Se uma fonte falhar, o valor anterior é mantido. **O campo
`iv` nunca é sobrescrito** pelo Actions. Se `site/data.json` mudar, faz commit `[skip ci]` e o
job `publicar` sobe o `site/` para o GitHub Pages.

Rodar o script localmente:

```bash
python3 automation/update_data.py   # só biblioteca padrão do Python 3.12
```

### 2. Rotina Claude (semanal, cobrada por execução)

Refresh mais "inteligente": reexecuta a pesquisa `/last30days`, atualiza IV estimada, odds do
Polymarket, números de pesquisa e os trechos de texto, faz commit e **republica o artifact do
claude.ai**. O prompt está em [`automation/claude-routine.md`](automation/claude-routine.md);
a configuração do cron e como pausar/remover em [`automation/SCHEDULE.md`](automation/SCHEDULE.md).

---

## A skill do livro

[`skills/pfutzenreuter-opcoes/`](skills/pfutzenreuter-opcoes/) é uma *agent skill* gerada a
partir do PDF com o fluxo `book-to-skill`. Contém:

- `SKILL.md` — frameworks centrais + índice de capítulos e de tópicos;
- `chapters/ch01…ch12.md` — um resumo estruturado por capítulo (cap. 11 e 12, as operações, em
  maior profundidade);
- `glossary.md` — o Apêndice A do livro + conceitos, com referência de capítulo;
- `patterns.md` — cada operação: quando usar, como montar, trade-offs, parâmetros;
- `cheatsheet.md` — tabelas de decisão (operação por visão de mercado, moneyness → gregas,
  fórmulas de bolso, parâmetros de todas as operações).

Para usar no Claude Code, copie a pasta para `~/.claude/skills/` e chame `pfutzenreuter-opcoes`.

---

## Licença

[MIT](LICENSE). O conteúdo do livro pertence ao autor e à editora; a skill é uma síntese
estrutural para estudo, não uma cópia do texto.
