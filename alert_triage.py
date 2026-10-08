"""
alert_triage.py - Fernhill Bank card fraud alert triage prototype

Reads alerts from data/alerts.jsonl, asks Claude for an analyst summary and a
recommended disposition, writes results to output/results.jsonl.

Usage:
    python alert_triage.py                 # all alerts
    python alert_triage.py --limit 5       # first 5
    python alert_triage.py --alert ALT-2026-0912

Built by: contractor (see README)
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

MODEL = os.environ.get("TRIAGE_MODEL", "claude-sonnet-4-5")
DATA_FILE = "data/alerts.jsonl"
OUTPUT_FILE = "output/results.jsonl"
PROCEDURES_FILE = "docs/fraud_procedures.md"

client = Anthropic()


def load_procedures():
    with open(PROCEDURES_FILE) as f:
        return f.read()


def load_alerts():
    alerts = []
    with open(DATA_FILE) as f:
        for line in f:
            if line.strip():
                alerts.append(json.loads(line))
    return alerts


def build_prompt(alert, procedures):
    system = (
        "You are a senior fraud analyst at Fernhill Bank. Use the bank's procedures below "
        "to review the alert and recommend a disposition.\n\n"
        "=== FERNHILL BANK FRAUD PROCEDURES ===\n"
        + procedures
        + "\n=== END PROCEDURES ==="
    )
    user = (
        "Review this alert and write a short analyst summary followed by your recommended "
        "disposition (Clear, Hold and Call, or Escalate) and the reason.\n\n"
        "Cardholder: " + alert["cardholder"]["name"]
        + "\nDate of birth: " + alert["cardholder"]["date_of_birth"]
        + "\nCard number: " + alert["cardholder"]["card_number"]
        + "\nHome: " + alert["cardholder"]["home_city"] + ", " + alert["cardholder"]["home_state"]
        + "\nAccount age (days): " + str(alert["cardholder"]["account_age_days"])
        + "\n\nRule fired: " + alert["rule_fired"]
        + "\n\nTransaction:\n" + json.dumps(alert["transaction"], indent=2)
        + "\n\nRecent activity:\n" + json.dumps(alert.get("recent_activity"), indent=2)
        + "\n\nSignals:\n" + json.dumps(alert.get("signals"), indent=2)
        + "\n\nCustomer contact:\n" + json.dumps(alert.get("customer_contact"), indent=2)
    )
    return system, user


def parse_disposition(text):
    # the model usually says "Recommended disposition: Clear" or similar
    m = re.search(r"[Dd]isposition[:\s]+\**(Clear|Hold and Call|Escalate)", text)
    if m:
        return m.group(1).lower().replace(" ", "_")
    m = re.search(r"\b(CLEAR|HOLD AND CALL|ESCALATE)\b", text)
    if m:
        return m.group(1).lower().replace(" ", "_")
    return "clear"  # default if we can't find it


def triage(alert, procedures):
    system, user = build_prompt(alert, procedures)
    print(f"[{datetime.now().isoformat()}] sending {alert['alert_id']} for {alert['cardholder']['name']} "
          f"card {alert['cardholder']['card_number']} ...")
    resp = client.messages.create(
        model=MODEL,
        max_tokens=800,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    text = resp.content[0].text
    disposition = parse_disposition(text)
    print(f"  -> {disposition}")
    print(f"  prompt: {user}")
    print(f"  response: {text}")
    return {
        "alert_id": alert["alert_id"],
        "disposition": disposition,
        "summary": text,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--alert", type=str, default=None)
    args = parser.parse_args()

    procedures = load_procedures()
    alerts = load_alerts()
    if args.alert:
        alerts = [a for a in alerts if a["alert_id"] == args.alert]
    if args.limit:
        alerts = alerts[: args.limit]

    os.makedirs("output", exist_ok=True)
    results = []
    for alert in alerts:
        result = triage(alert, procedures)
        results.append(result)

    with open(OUTPUT_FILE, "w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")

    counts = {}
    for r in results:
        counts[r["disposition"]] = counts.get(r["disposition"], 0) + 1
    print(f"\ndone. {len(results)} alerts. {counts}")
    print(f"results written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
