# Agendamento — como mudar, pausar e desligar

Dois mecanismos independentes. Você pode ligar/desligar cada um sem afetar o outro.

---

## 1. GitHub Actions (grátis)

**Onde:** [`.github/workflows/update.yml`](../.github/workflows/update.yml)

**Cron (UTC).** A B3 opera em BRT = UTC−3, sem horário de verão.

| Cron | Horário BRT | Momento |
|---|---|---|
| `15 21 * * 1-5` | 18:15, seg–sex | ~1h após o fechamento do pregão (17:00 + after-market) |
| `45 11 * * 1-5` | 08:45, seg–sex | ~1h antes da abertura (10:00) |

**Mudar horário:** edite as linhas `cron:` (use <https://crontab.guru>, lembrando que é UTC).
Ex.: 19:00 BRT = `00 22 * * 1-5`.

**Rodar agora, à mão:** aba *Actions* → *atualizar-e-publicar* → *Run workflow*. Ou:

```bash
gh workflow run update.yml -R timmtimm1/opcoes-eleicao-2026-br
gh run watch  -R timmtimm1/opcoes-eleicao-2026-br
```

**Pausar:** aba *Actions* → *atualizar-e-publicar* → botão `⋯` → *Disable workflow*.
Reativar no mesmo lugar. Ou apague o arquivo `.github/workflows/update.yml`.

**Token opcional do brapi.dev:** *Settings → Secrets and variables → Actions → New repository
secret* → nome `BRAPI_TOKEN`. Funciona sem, usando o Yahoo Finance.

**Nota:** o GitHub desativa cron de Actions em repositório sem commits há 60 dias. Um commit
qualquer reativa.

---

## 2. Rotina Claude (cobrada por execução)

Um agente Claude Code na nuvem que roda o prompt de [`claude-routine.md`](claude-routine.md)
em cron. Cada execução consome uso do seu plano.

**Sugestão de cron:** semanal, segunda 09:00 BRT (`0 12 * * 1` em UTC).

### Criar

No Claude Code, use a skill `schedule` (ou `/schedule`):

```
/schedule criar rotina semanal, segunda 09:00 America/Sao_Paulo,
que execute o prompt de automation/claude-routine.md do repo timmtimm1/opcoes-eleicao-2026-br
```

Isso registra um cron job. Confirme com:

```
/schedule list
```

### Pausar / remover

```
/schedule list              # ver as rotinas e seus IDs
/schedule remover <id>      # apaga a rotina
```

Ou, direto: `CronList` para ver, `CronDelete` para apagar.

### O que ela faz (resumo — detalhe em claude-routine.md)

1. `git clone` / `pull` do repo.
2. Reexecuta a pesquisa (`/last30days` sobre "Brazil 2026 election market volatility") — leve.
3. Atualiza em `site/data.json`: `tickers.*.iv` (estimativa), `chips`, e um bloco `research`
   com odds do Polymarket, pesquisas e data.
4. Atualiza os trechos de texto correspondentes em `site/index.html` (hero, chips, cards).
5. `git commit` + `git push` (dispara o deploy do Pages pelo Actions).
6. Lê e **republica** o artifact do claude.ai
   (`https://claude.ai/code/artifact/5d0c89e9-3418-4325-89f3-c38662d7be4a`) com `url=`.

### Validação

A **primeira execução é o teste real** — verifique depois dela:

- houve commit novo em `main`? (`git log -1`)
- o Pages redeployou? (aba *Actions*)
- o artifact do claude.ai mudou de versão?

Se o passo 6 (republicar o artifact) falhar no ambiente da rotina, os passos 1–5 ainda
mantêm o **site do GitHub Pages** atualizado — que é a fonte "viva" principal.
