# Prompt da rotina Claude semanal

Este é o texto que o agente agendado (cron cloud) executa. Mantém o site e o artifact
sincronizados com a pesquisa da semana. Não toca em cotação de spot — isso é do GitHub Actions.

---

## Contexto

- Repo: `timmtimm1/opcoes-eleicao-2026-br` (público)
- Site: `site/index.html` + `site/data.json`
- Artifact claude.ai: `https://claude.ai/code/artifact/5d0c89e9-3418-4325-89f3-c38662d7be4a`
- Evento: eleição presidencial BR — 1º turno 04/10/2026, 2º turno 25/10/2026
- Fonte de conhecimento: `skills/pfutzenreuter-opcoes/` (livro de Pfützenreuter)

## Tarefa (executar em ordem)

1. **Clonar / atualizar** o repo:
   `git clone https://github.com/timmtimm1/opcoes-eleicao-2026-br || (cd opcoes-eleicao-2026-br && git pull)`

2. **Pesquisa leve** com `/last30days` (ou web search se indisponível), tópico:
   *"Brazil 2026 election market volatility — Ibovespa implied volatility, Polymarket odds,
   Lula vs opposition polls"*. Extrair:
   - odds atuais do mercado Polymarket "Brazil Presidential Election" (%);
   - leitura de pesquisas (Lula vs adversário, margem);
   - qualquer número público de volatilidade implícita (Ibovespa VIX) — se não houver, manter
     a estimativa anterior e registrar "sem print público".

3. **Atualizar `site/data.json`**, SEM mexer em `tickers.*.spot` (é do Actions):
   - `tickers.*.iv` → ajustar a estimativa de IV anual por ativo, se a pesquisa justificar
     (ex.: vol subindo perto do 1º turno → subir PETR4/BBAS3);
   - adicionar/atualizar um bloco:
     ```json
     "research": {
       "asof": "DD/MM/AAAA",
       "polymarket": "texto curto com as odds",
       "polls": "texto curto",
       "ibov_vix": "nível ou 'sem print público'"
     }
     ```

4. **Atualizar `site/index.html`** — só os trechos de texto que refletem a pesquisa:
   - chips do hero (Polymarket, pesquisa);
   - card "voz do livro" do hero, se a leitura mudou;
   - **não** reescrever a lógica JS, os controles nem o layout.

5. **Commit + push:**
   `git add -A && git commit -m "chore(pesquisa): refresh semanal DD/MM" && git push`
   (o GitHub Actions publica o Pages automaticamente).

6. **Republicar o artifact do claude.ai:**
   - `Artifact` action `read` com `url=` do artifact → pegar a versão atual;
   - aplicar as mesmas mudanças de texto do passo 4 sobre essa versão;
   - `Artifact` publish com `url=` (mesmo link), `label` curto tipo `refresh-DD-MM`.

7. **Relatório curto** (1 parágrafo): o que mudou em odds/pesquisa/IV, e links do commit e da
   nova versão do artifact.

## Regras

- Nunca alterar a fórmula de Black-Scholes, os cálculos de payoff/probabilidade, o cron ou o
  workflow.
- Se a pesquisa não trouxer nada novo relevante, **não** commitar — só reportar "sem mudança".
- Se o passo 6 falhar (sem acesso ao Artifact no ambiente da rotina), concluir mesmo assim: o
  site do Pages é a fonte viva; registrar a falha no relatório.
- Datas relativas → sempre absolutas.
