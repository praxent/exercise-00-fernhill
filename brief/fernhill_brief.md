# Client brief: Fernhill Bank, card fraud alert triage

*Fernhill Bank is fictional. Every name, number and record in this packet is invented.*

## The client

Fernhill Bank is a community bank in Oregon with about four billion dollars in assets. Its Card Fraud Operations team has twelve analysts, three of them senior. The team's transaction monitoring system raises about 1,800 card-fraud alerts a day, rising to 3,000 in peak season. An analyst works each alert in roughly six minutes. About seventy percent of alerts close as false positives. The backlog is growing.

## What exists

Six months ago a contractor built a prototype called **alert-triage**. It is a Python script that reads an alert (the transaction, the cardholder's recent history, device and merchant signals), calls Claude, and writes a first-pass analyst summary with a recommended disposition: clear, hold the card and call the customer, or escalate for suspicious-activity review. The code, the sample alerts it was tested on, and the bank's fraud procedures document are in this repository.

The prototype ran in the analyst queue for about a month. The analysts stopped using it.

## What the bank wants

A version of alert-triage that the analysts trust, running in the analyst queue, within six weeks. The VP of Fraud Operations owns the project. The bank's Model Risk Management function has to approve any decision aid before it returns to the queue.

## Your pre-read

Read this brief. Look through the repository and run the script on a few alerts so you know what it does today. Do not start changing it. The specific request comes from the client during the session, and you will get time with the VP before you touch anything.

## Logistics

The repository runs with Python 3.10 or newer and an Anthropic API key, which we provide for the exercise. Keep the files local and do not share them. Bring the coding agent and tools you use day to day.
