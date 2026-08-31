# Como isto foi construído

Registro do processo, ferramenta por ferramenta, para reproduzir ou auditar.

---

## 1. PDF → skill (`book-to-skill`)

Entrada: PDF *Investindo no Mercado de Opções* (Elvis Pfützenreuter, Novatec, 1ª ed., ~252 p.).

Fluxo `book-to-skill`:

1. **Extração** — modo *technical* (Docling), preservando tabelas e fórmulas como markdown.
   Saída: `full_text.txt` (~43.600 palavras, ~58k tokens, 12 capítulos).
2. **Análise de estrutura** — título, autor, mapa de capítulos, temas.
3. **Geração** — `DEPTH=study`, `BOOK_TYPE=technical`:
   - `SKILL.md` (frameworks centrais + índice de capítulos e de tópicos);
   - `chapters/ch01…ch12.md` — resumo estruturado por capítulo (Core Idea, Frameworks,
     Key Concepts, Worked Example, Anti-patterns, Key Takeaways, Connects To);
     cap. 11 (operações) e 12 (simulação com cotações reais) em maior profundidade;
   - `glossary.md`, `patterns.md`, `cheatsheet.md`.
4. **Scan de segurança** do skill gerado — sem padrões de injeção.

Resultado em [`../skills/pfutzenreuter-opcoes/`](../skills/pfutzenreuter-opcoes/).

---

## 2. Pesquisa de mercado (`/last30days`)

Run de **31/08/2026**, tópico *"Brazil 2026 election market volatility"*, plano de 3 subqueries
(primária + polls/cenários + implied vol), fontes: Reddit, X, YouTube, Hacker News, Polymarket,
web. Reddit veio parcial (HTTP 429).

**Achados usados na ferramenta:**

- 1º turno **04/10/2026**, 2º turno **25/10/2026** (AS/COA, Rio Times).
- Corrida empatada: Lula ~3–6 pts à frente de Flávio Bolsonaro; cenários de 2º turno dentro da
  margem de erro (@awsan).
- Transmissão via **credibilidade fiscal**: Goldman fala em "asymmetric real trade", câmbio
  −4% a +3%; SocGen, quebra do carry; Commerzbank, USD/BRL 5,20 só se o risco político ceder.
- Evento **já no preço**: Ibovespa −2,5% em 11/08 citando a eleição (Rio Times).
- COPOM 16–17/09 (mercado espera corte; Fed pode subir nos mesmos dias) — @jeffnab3.
- **Ibovespa VIX** existe (S&P/B3, metodologia Cboe, desde 2024) mas **sem print público** —
  ponto cego assumido na ferramenta.
- Polymarket: mercado "Brazil Presidential Election" ~US$23M de volume.

Saída bruta + fontes em [`RESEARCH-2026-08-31.md`](RESEARCH-2026-08-31.md).

---

## 3. Estratégia (skill `pfutzenreuter-opcoes`)

Cruzando a pesquisa com o livro:

- **Instrumento** (cap. 6.7): o par call OTM + put OTM = *strangle*, o "instrumento de
  volatilidade" do livro.
- **Correção** (cap. 9 + 11.5): a IV pré-eleição já embute o prêmio do evento → o livro diz
  *lançar*, não comprar. Solução: vender duas asas mais OTM → *strangle* de **risco definido**
  (reverse iron condor). Menos theta, menos vega, perda travada; teto no lucro.
- **Análise** (cap. 11.17): payoff no vencimento = soma dos intrínsecos; pontos de empate;
  chance de vitória via log-normal (cap. 6); gregas totais = soma das pernas.
- **Timing** (cap. 10 + 11.6): theta acelera nas últimas ~2 semanas → não carregar até o
  vencimento; entrar com antecedência, sair no evento.
- **Veículos**: PETR4 e BBAS3 = maior beta eleitoral (a "PETRA50" do livro; BBAS3 com β=0,757
  no exemplo do CAPM, cap. 5). ITUB4/BBDC4 = dirigidos por juros/COPOM (rho, cap. 10).
- **Gestão** (cap. 11.21): estratégia escrita antes de montar — ver [`STRATEGY.md`](STRATEGY.md).

---

## 4. Ferramenta (`artifact-design` + `Artifact`)

Página HTML única, sem framework. Tudo é calculado no navegador:

- `normCdf` (Abramowitz-Stegun 26.2.17), `bsCall`/`bsPut` → prêmios e gregas (vega/theta por
  diferença finita);
- payoff do reverse iron condor / strangle, pontos de empate por varredura de sinal;
- estimador log-normal `P(spot<F) = N(d)` da cap. 6;
- "janela ideal de compra": matemática de dias úteis a partir do catalisador de cada ativo;
- checklist com `localStorage`, tema claro/escuro/auto, legenda filtrável.

Tipografia: Libre Franklin (títulos), Newsreader (corpo), IBM Plex Mono (dados). Dois temas
via tokens CSS.

Publicado como artifact em `https://claude.ai/code/artifact/5d0c89e9-3418-4325-89f3-c38662d7be4a`
e como site em `https://timmtimm1.github.io/opcoes-eleicao-2026-br/`.

---

## 5. Automação (GitHub Actions + rotina Claude)

- **`automation/update_data.py`** — stdlib do Python 3.12; Yahoo Finance (sem token) → brapi.dev
  (token opcional). Reescreve `site/data.json` mantendo `iv` e valores que falharam.
- **`.github/workflows/update.yml`** — cron dias úteis 18:15 e 08:45 BRT + manual + push; job
  `atualizar` (commit `[skip ci]` se mudou) e job `publicar` (GitHub Pages).
- **`site/index.html`** faz `fetch('data.json')` no boot e re-renderiza; no claude.ai o sandbox
  bloqueia — usa os valores embutidos.
- **Rotina Claude semanal** — refresh de IV/odds/pesquisa e republicação do artifact; ver
  [`../automation/claude-routine.md`](../automation/claude-routine.md) e
  [`../automation/SCHEDULE.md`](../automation/SCHEDULE.md).
