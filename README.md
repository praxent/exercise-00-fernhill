# alert-triage

Prototype for Fernhill Bank card fraud operations. Reads TMS alerts, asks Claude for a first-pass analyst summary and a recommended disposition (clear / hold and call / escalate), and writes the results out so they can be pasted into the case system.

Status: pilot. Ran for about a month in the analyst queue. Currently not in use.

## Setup

```
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # add your ANTHROPIC_API_KEY
```

Python 3.10 or newer.

## Run

```
python alert_triage.py --limit 3          # try a few first
python alert_triage.py                    # all 40 sample alerts
python alert_triage.py --alert ALT-2026-0912
```

Results go to `output/results.jsonl`, one line per alert with the disposition and the full model response. Progress and the model's answers print to the console as it runs.

Model defaults to `claude-sonnet-4-5`; override with `TRIAGE_MODEL` in `.env`.

## What's in here

```
alert_triage.py          the script
data/alerts.jsonl        40 sample alerts exported from the TMS (synthetic)
data/labels.csv          dispositions from the senior analysts for the same 40 alerts
docs/fraud_procedures.md the bank's fraud procedures doc (FP-110), used in the prompt
brief/                   client brief
```

## Notes

- The procedures doc is long. Loading it into the prompt is what makes the summaries sound like the bank's own procedures, per the VP's request.
- Some alerts come through without enrichment data (recent_activity / signals are null) when the TMS enrichment service times out. The script handles these the same as any other alert.
- Costs ran higher than expected during the pilot month. Didn't get to the bottom of it.
- TODO: retries on API errors. If the API hiccups mid-run you need to start over.
- TODO: analysts asked for a confidence score. Not implemented.
