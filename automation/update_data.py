#!/usr/bin/env python3
"""
update_data.py — atualiza site/data.json com cotações de fechamento / abertura.

Fontes (em ordem): Yahoo Finance (sem token) -> brapi.dev (token opcional em BRAPI_TOKEN).
Regras:
  * nunca sobrescreve o campo "iv" (estimativa mantida manualmente / pela rotina Claude);
  * se uma cotação falhar, mantém o valor anterior do data.json;
  * escreve "updated" (UTC + BRT), "source" e "chips.ibov".
Só usa a biblioteca padrão do Python 3. Rodado pelo GitHub Actions (.github/workflows/update.yml).
"""

import json
import os
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(ROOT, "site", "data.json")

# ticker do data.json -> símbolo Yahoo / símbolo brapi
SYMBOLS = {
    "IBOV":  {"yahoo": "%5EBVSP",  "brapi": "^BVSP"},
    "PETR4": {"yahoo": "PETR4.SA", "brapi": "PETR4"},
    "BBAS3": {"yahoo": "BBAS3.SA", "brapi": "BBAS3"},
    "ITUB4": {"yahoo": "ITUB4.SA", "brapi": "ITUB4"},
    "BBDC4": {"yahoo": "BBDC4.SA", "brapi": "BBDC4"},
}

UA = {"User-Agent": "Mozilla/5.0 (compatible; opcoes-eleicao-2026-br/1.0)"}
BRT = timezone(timedelta(hours=-3))


def _get(url, headers=None, timeout=20):
    req = urllib.request.Request(url, headers=headers or UA)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def yahoo_price(sym):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}?range=1d&interval=1d"
    data = _get(url)
    meta = data["chart"]["result"][0]["meta"]
    price = meta.get("regularMarketPrice") or meta.get("chartPreviousClose")
    if price is None:
        raise ValueError("sem preço no payload Yahoo")
    return float(price)


def brapi_price(sym, token):
    q = f"https://brapi.dev/api/quote/{sym}"
    if token:
        q += f"?token={token}"
    data = _get(q)
    results = data.get("results") or []
    if not results:
        raise ValueError("sem results no payload brapi")
    price = results[0].get("regularMarketPrice") or results[0].get("regularMarketPreviousClose")
    if price is None:
        raise ValueError("sem preço no payload brapi")
    return float(price)


def fetch_price(ticker):
    y = SYMBOLS[ticker]["yahoo"]
    b = SYMBOLS[ticker]["brapi"]
    token = os.environ.get("BRAPI_TOKEN", "").strip()
    errors = []
    for attempt in range(2):
        try:
            return yahoo_price(y), "yahoo"
        except Exception as e:  # noqa: BLE001
            errors.append(f"yahoo:{e}")
            time.sleep(1.5)
    try:
        return brapi_price(b, token), "brapi"
    except Exception as e:  # noqa: BLE001
        errors.append(f"brapi:{e}")
    raise RuntimeError("; ".join(errors))


def fmt_ibov(price):
    return "~" + f"{round(price):,}".replace(",", ".")


def main():
    with open(DATA_PATH, "r", encoding="utf-8") as fh:
        data = json.load(fh)

    tickers = data.setdefault("tickers", {})
    got, kept = [], []
    src_used = set()

    for tk in SYMBOLS:
        slot = tickers.setdefault(tk, {})
        try:
            price, src = fetch_price(tk)
            price = round(price, 0) if tk == "IBOV" else round(price, 2)
            slot["spot"] = price
            src_used.add(src)
            got.append(f"{tk}={price}")
        except Exception as e:  # noqa: BLE001
            kept.append(f"{tk}({e.__class__.__name__})")
        # "iv" nunca é tocado aqui
        slot.setdefault("iv", None)

    if "IBOV" in tickers and tickers["IBOV"].get("spot"):
        data.setdefault("chips", {})["ibov"] = fmt_ibov(tickers["IBOV"]["spot"])

    now_utc = datetime.now(timezone.utc)
    data["updated"] = (
        now_utc.astimezone(BRT).strftime("%d/%m/%Y %H:%M BRT")
        + f"  ({now_utc.strftime('%Y-%m-%dT%H:%MZ')})"
    )
    data["source"] = "Yahoo Finance / brapi.dev via GitHub Actions"
    if src_used:
        data["source"] += " [" + ",".join(sorted(src_used)) + "]"

    with open(DATA_PATH, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    print("atualizados:", ", ".join(got) or "(nenhum)")
    if kept:
        print("mantidos (falha na fonte):", ", ".join(kept))
    # sai 0 mesmo com falhas parciais — o commit só ocorre se houve mudança
    return 0


if __name__ == "__main__":
    sys.exit(main())
