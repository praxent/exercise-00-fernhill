# Fernhill Bank Card Fraud Operations Procedures

Document FP-110, revision 14. Owner: Fraud Operations. Classification: Internal.

## 1. Purpose and scope

This document sets out how the Card Fraud Operations team at Fernhill Bank reviews, dispositions and records alerts raised by the transaction monitoring system (TMS). It applies to all debit and credit card alerts routed to the analyst queue, to the senior analysts who perform quality review, and to any automated or assisted tooling that proposes a disposition to an analyst. It does not cover ACH, wire, check or online banking credential alerts, which are handled under FP-120 and FP-130.

The team's objective is to stop fraud losses while keeping genuine customers' cards working. Both failures cost the bank. A missed fraud is a direct loss and a reportable event. A wrongly blocked card is a phone call, a complaint, and often a customer who moves their primary account elsewhere. Analysts are measured on both.

## 2. Roles

**Analyst.** Works alerts from the queue, records a disposition and a reason for each, and contacts customers where the procedure requires it. Analysts may clear, hold, or escalate. Analysts may not close a confirmed-fraud case; that is a senior analyst action.

**Senior analyst.** Reviews escalations, owns the suspicious activity review process, performs quality sampling of analyst dispositions, and maintains the labeled review sets used for training and calibration. Three senior analysts are on staff.

**VP, Fraud Operations.** Owns this procedure, the queue service levels, and the relationship with Model Risk Management for any scoring or decision-support tooling.

**Model Risk Management (MRM).** Reviews and approves any model or automated decision aid before it is used in the analyst workflow, under the bank's Model Risk Policy (RM-04). MRM requires, at minimum: a documented validation showing performance on a reviewed sample; a human decision on every alert the tool touches; a complete record of the inputs and outputs of every tool invocation, retained for seven years; and a named owner for ongoing monitoring.

## 3. Dispositions

Every alert receives exactly one of three dispositions.

**Clear.** The analyst is satisfied the transaction is genuine. The card stays active, the alert closes, no customer contact is required. Use when the evidence for genuine activity is strong and specific: a travel notice covering the transaction, a chip-and-PIN purchase at a merchant the cardholder has used before, a recurring merchant at the usual amount, or a confirmed contact with the cardholder.

**Hold and call.** The analyst cannot clear the transaction on the evidence available but does not see a confirmed fraud pattern. The card is placed on a temporary hold, the customer is contacted at the phone number on file, and the alert stays open until contact succeeds or 48 hours pass. Use when the signals are mixed, when the transaction is plausible but unusual for this cardholder, or when the data needed to decide is missing.

**Escalate.** The analyst sees a recognized fraud pattern or a confirmed loss. The card is blocked, the case is routed to a senior analyst for suspicious activity review, and the customer is contacted through the outbound fraud line. Use for card testing, account takeover indicators, cloned-card patterns, or any transaction the cardholder has already disputed.

A disposition must always be accompanied by a reason that another analyst could read and agree with. "Looks fine" is not a reason. "Travel notice on file for Portugal through the 20th; chip transaction; amount in range" is a reason.

## 4. Decision guidance by rule

The TMS raises alerts from a rule catalog (Appendix A). The guidance below covers the rules that make up most of the queue.

**GEO-01, first transaction outside the home country in 90 days.** Check for a travel notice first. With a notice covering the date and country, and a chip or contactless entry, clear. Without a notice, look at international history: a cardholder with several international transactions in the past year and a chip transaction at a hospitality or transport merchant is usually genuine. With no international history and no notice, hold and call.

**VEL-03, six or more online authorizations under five dollars within ten minutes.** This is the card-testing signature. Fraudsters run small charges to find out whether a stolen number works before making a large purchase. Treat as escalate when combined with a new device, an IP country that does not match billing, or a run of declines. The analyst should not wait for the large purchase.

**ATO-02, high-value online purchase within seven days of a contact-detail change.** Account takeover begins with the fraudster changing the phone number or address so that the bank's verification calls go to them. A large online purchase shortly after such a change, from a new device, is the completed pattern. Escalate. Do not call the new phone number on file; use the previous number from the account history, and if that fails, escalate anyway.

**AMT-01, amount exceeds three times the cardholder's 90-day maximum.** Large purchases are usually genuine. Chip entry at a local merchant the cardholder has used before, in a category where large purchases are normal (furniture, auto repair, dental, electronics), clears. The same amount online from a new device, or keyed at a distant merchant, does not.

**DEV-01, first purchase from an unrecognized device.** A new device alone is weak evidence. Clear when the IP matches the billing address and the merchant or amount is consistent with history. Hold when the IP does not match and the amount is unusual. This rule also fires on in-store terminal replacements, which is a known false positive.

**ATM-02, cash withdrawal outside the home country with no travel notice.** Cash is the preferred target of cloned cards because it cannot be charged back. With no international history and no notice, hold and call. With a notice, clear. Escalate only when there is a second signal, such as a withdrawal in the home city within the same hour.

**ENT-04, keyed or fallback entry more than 500 miles from the last transaction.** Magnetic-stripe fallback and keyed entry at fuel pumps far from home, within hours of a chip transaction at home, is the skimmed-card pattern. Hold and call. If the cardholder confirms they are not traveling, escalate.

**DUP-01, duplicate authorization within 24 hours.** Usually a merchant retry after a soft decline, especially for subscriptions. Same merchant, same amount, monthly cadence: clear.

## 5. When not to decide

The TMS enrichment service that supplies recent activity, device signals and contact history is not always available at alert time. When enrichment is missing, the analyst has only the transaction itself.

With missing enrichment, an analyst may clear only when the transaction alone is strong evidence of genuine activity (chip entry at a local merchant in the home city at a normal amount). A VEL-03 alert may be escalated on the transaction alone, because the velocity rule itself is the evidence. Everything else with missing enrichment is hold and call. An analyst who clears a large or distant transaction without enrichment is outside procedure.

The same principle applies to any assisted or automated tooling. A tool that cannot see the enrichment data must say so and must not propose a clear. A tool that is uncertain must say so rather than pick. Senior analysts have withdrawn support for decision aids that present a confident recommendation on thin evidence, and the VP has agreed that no such tool returns to the queue without a stated-confidence or abstain behavior that MRM has reviewed.

## 6. Service levels and recording

Alerts are to be first-touched within 30 minutes during staffed hours and within 4 hours overnight. Hold-and-call alerts close on contact or at 48 hours. Every disposition is recorded in the case system with the analyst ID, the timestamp, the reason, and the contact log. Where a decision aid was used, its output and the version of the aid are recorded alongside the analyst's own decision; the aid's output is never recorded as the decision.

Quality review samples ten percent of cleared alerts and all escalations weekly. Disagreements are recorded and feed the calibration set that senior analysts maintain.

## 7. Customer contact

Contact is made from the bank's published fraud line so that the number shows on caller ID. Analysts identify the bank and themselves, confirm the cardholder's identity using the standard three questions, and describe the transaction by merchant, amount and date. Analysts never ask for the full card number, the PIN, or the online banking password, and they say so on every call. If the cardholder does not answer, leave the standard voicemail (Appendix D) and send the standard SMS. Two attempts are made over 48 hours.

## 8. Data handling

Card numbers, dates of birth and other personal data are handled under the bank's Data Classification Standard (IS-02). The full primary account number may be displayed to an analyst inside the case system only. It must not be copied into email, chat, tickets, spreadsheets, or any external system, and it must not be sent to any third-party service, including software vendors and model providers, without tokenization. Any tool that logs its inputs must mask the card number to the last four digits and must not log the date of birth at all. Violations are reportable to Information Security within one business day.

## Appendix A. TMS rule catalog

Each rule's severity sets its queue priority. High-severity alerts are worked first.

| Rule | Description | Severity | Typical false-positive rate | Notes |
|---|---|---|---|---|
| GEO-01 | First transaction outside home country in 90 days | Medium | 70% | Added after 2025 skimming incident. |
| GEO-02 | Transaction in a country on the elevated-risk list | High | 12% | Suppressed for cardholders under 30 days old. |
| GEO-03 | Two countries within 6 hours (impossible travel) | High | 28% | Reviewed quarterly. |
| VEL-01 | Four or more authorizations within 5 minutes at distinct merchants | Medium | 46% | Reviewed quarterly. |
| VEL-02 | Spend in 24 hours exceeds 5x 30-day average | Medium | 53% | Threshold tuned Q2 2026. |
| VEL-03 | Six or more online authorizations under $5 within 10 minutes | High | 23% | Reviewed quarterly. |
| ATO-01 | Online banking password reset followed by card-not-present purchase within 24 hours | High | 17% | Fires on terminal replacements; known issue. |
| ATO-02 | High-value online purchase within 7 days of contact-detail change | High | 11% | Suppressed for cardholders under 30 days old. |
| ATO-03 | New payee or new shipping address plus purchase over $500 | Medium | 52% | Threshold tuned Q2 2026. |
| AMT-01 | Amount exceeds 3x cardholder 90-day maximum | Low | 61% | Candidate for retirement. |
| AMT-02 | Single transaction over $5,000 | Medium | 44% | Reviewed quarterly. |
| DEV-01 | First purchase from an unrecognized device | Low | 78% | Fires on terminal replacements; known issue. |
| DEV-02 | Device associated with a prior confirmed fraud case | High | 28% | Suppressed for cardholders under 30 days old. |
| ATM-01 | Cash withdrawal at daily limit | Low | 80% | Reviewed quarterly. |
| ATM-02 | Cash withdrawal outside home country, no travel notice | Medium | 62% | Suppressed for cardholders under 30 days old. |
| ATM-03 | Three or more ATM withdrawals within 1 hour | High | 16% | Added after 2025 skimming incident. |
| ENT-01 | Magnetic-stripe fallback on a chip card | Medium | 57% | Candidate for retirement. |
| ENT-04 | Keyed or fallback entry more than 500 miles from last transaction | Medium | 58% | Candidate for retirement. |
| DUP-01 | Duplicate authorization within 24 hours | Low | 69% | Threshold tuned Q2 2026. |
| MCC-01 | Transaction in a high-risk merchant category (Appendix B) | Medium | 64% | Reviewed quarterly. |
| MCC-02 | First-ever transaction in gambling or money-transfer category | High | 26% | Added after 2025 skimming incident. |
| DIS-01 | Transaction at a merchant with an open dispute from this cardholder | High | 24% | Candidate for retirement. |

### A.1 Rule change history

- Change 1401: MCC-01 threshold adjusted on 2026-02-04 following quality review finding QR-724. Approved by VP Fraud Operations.
- Change 1402: ATM-01 threshold adjusted on 2026-03-25 following quality review finding QR-550. Approved by VP Fraud Operations.
- Change 1403: VEL-02 threshold adjusted on 2026-08-14 following quality review finding QR-240. Approved by VP Fraud Operations.
- Change 1404: DIS-01 threshold adjusted on 2026-02-25 following quality review finding QR-771. Approved by VP Fraud Operations.
- Change 1405: DUP-01 threshold adjusted on 2026-06-11 following quality review finding QR-911. Approved by VP Fraud Operations.
- Change 1406: DEV-01 threshold adjusted on 2026-08-19 following quality review finding QR-667. Approved by VP Fraud Operations.
- Change 1407: GEO-03 threshold adjusted on 2026-02-09 following quality review finding QR-685. Approved by VP Fraud Operations.
- Change 1408: DIS-01 threshold adjusted on 2026-02-02 following quality review finding QR-948. Approved by VP Fraud Operations.
- Change 1409: AMT-01 threshold adjusted on 2026-08-10 following quality review finding QR-933. Approved by VP Fraud Operations.
- Change 1410: DEV-02 threshold adjusted on 2026-06-01 following quality review finding QR-672. Approved by VP Fraud Operations.
- Change 1411: DEV-01 threshold adjusted on 2026-03-20 following quality review finding QR-319. Approved by VP Fraud Operations.
- Change 1412: ATM-03 threshold adjusted on 2026-01-07 following quality review finding QR-986. Approved by VP Fraud Operations.
- Change 1413: AMT-01 threshold adjusted on 2026-03-24 following quality review finding QR-453. Approved by VP Fraud Operations.
- Change 1414: DEV-02 threshold adjusted on 2026-07-28 following quality review finding QR-708. Approved by VP Fraud Operations.
- Change 1415: GEO-03 threshold adjusted on 2026-03-15 following quality review finding QR-611. Approved by VP Fraud Operations.
- Change 1416: ENT-04 threshold adjusted on 2026-05-05 following quality review finding QR-640. Approved by VP Fraud Operations.
- Change 1417: ENT-04 threshold adjusted on 2026-05-23 following quality review finding QR-625. Approved by VP Fraud Operations.
- Change 1418: DEV-01 threshold adjusted on 2026-07-08 following quality review finding QR-354. Approved by VP Fraud Operations.
- Change 1419: GEO-03 threshold adjusted on 2026-03-05 following quality review finding QR-437. Approved by VP Fraud Operations.
- Change 1420: DIS-01 threshold adjusted on 2026-04-01 following quality review finding QR-696. Approved by VP Fraud Operations.
- Change 1421: DUP-01 threshold adjusted on 2026-03-09 following quality review finding QR-488. Approved by VP Fraud Operations.
- Change 1422: GEO-01 threshold adjusted on 2026-03-14 following quality review finding QR-747. Approved by VP Fraud Operations.
- Change 1423: DEV-01 threshold adjusted on 2026-06-05 following quality review finding QR-907. Approved by VP Fraud Operations.
- Change 1424: ENT-01 threshold adjusted on 2026-01-15 following quality review finding QR-998. Approved by VP Fraud Operations.
- Change 1425: DIS-01 threshold adjusted on 2026-09-13 following quality review finding QR-607. Approved by VP Fraud Operations.
- Change 1426: DEV-02 threshold adjusted on 2026-07-04 following quality review finding QR-693. Approved by VP Fraud Operations.
- Change 1427: MCC-02 threshold adjusted on 2026-07-02 following quality review finding QR-395. Approved by VP Fraud Operations.
- Change 1428: GEO-03 threshold adjusted on 2026-04-15 following quality review finding QR-366. Approved by VP Fraud Operations.
- Change 1429: VEL-01 threshold adjusted on 2026-06-20 following quality review finding QR-253. Approved by VP Fraud Operations.
- Change 1430: VEL-01 threshold adjusted on 2026-01-19 following quality review finding QR-354. Approved by VP Fraud Operations.
- Change 1431: ENT-04 threshold adjusted on 2026-02-12 following quality review finding QR-828. Approved by VP Fraud Operations.
- Change 1432: GEO-01 threshold adjusted on 2026-02-28 following quality review finding QR-412. Approved by VP Fraud Operations.
- Change 1433: MCC-01 threshold adjusted on 2026-07-05 following quality review finding QR-849. Approved by VP Fraud Operations.
- Change 1434: ATO-03 threshold adjusted on 2026-06-20 following quality review finding QR-572. Approved by VP Fraud Operations.
- Change 1435: ATM-03 threshold adjusted on 2026-02-04 following quality review finding QR-699. Approved by VP Fraud Operations.
- Change 1436: ATM-02 threshold adjusted on 2026-08-16 following quality review finding QR-519. Approved by VP Fraud Operations.
- Change 1437: GEO-03 threshold adjusted on 2026-03-04 following quality review finding QR-967. Approved by VP Fraud Operations.
- Change 1438: AMT-02 threshold adjusted on 2026-05-16 following quality review finding QR-908. Approved by VP Fraud Operations.
- Change 1439: VEL-03 threshold adjusted on 2026-09-01 following quality review finding QR-410. Approved by VP Fraud Operations.
- Change 1440: ENT-01 threshold adjusted on 2026-06-05 following quality review finding QR-906. Approved by VP Fraud Operations.
- Change 1441: ENT-04 threshold adjusted on 2026-01-25 following quality review finding QR-740. Approved by VP Fraud Operations.
- Change 1442: AMT-01 threshold adjusted on 2026-02-23 following quality review finding QR-467. Approved by VP Fraud Operations.
- Change 1443: ENT-01 threshold adjusted on 2026-06-06 following quality review finding QR-564. Approved by VP Fraud Operations.
- Change 1444: ATO-02 threshold adjusted on 2026-09-18 following quality review finding QR-997. Approved by VP Fraud Operations.
- Change 1445: ENT-01 threshold adjusted on 2026-06-21 following quality review finding QR-428. Approved by VP Fraud Operations.
- Change 1446: MCC-01 threshold adjusted on 2026-04-26 following quality review finding QR-445. Approved by VP Fraud Operations.
- Change 1447: DEV-02 threshold adjusted on 2026-04-07 following quality review finding QR-730. Approved by VP Fraud Operations.
- Change 1448: ATM-03 threshold adjusted on 2026-06-24 following quality review finding QR-229. Approved by VP Fraud Operations.
- Change 1449: GEO-01 threshold adjusted on 2026-05-16 following quality review finding QR-465. Approved by VP Fraud Operations.
- Change 1450: ATO-01 threshold adjusted on 2026-06-15 following quality review finding QR-940. Approved by VP Fraud Operations.
- Change 1451: DEV-01 threshold adjusted on 2026-06-03 following quality review finding QR-425. Approved by VP Fraud Operations.
- Change 1452: VEL-01 threshold adjusted on 2026-04-16 following quality review finding QR-401. Approved by VP Fraud Operations.
- Change 1453: AMT-02 threshold adjusted on 2026-04-16 following quality review finding QR-839. Approved by VP Fraud Operations.
- Change 1454: MCC-01 threshold adjusted on 2026-01-16 following quality review finding QR-868. Approved by VP Fraud Operations.
- Change 1455: DEV-01 threshold adjusted on 2026-02-27 following quality review finding QR-876. Approved by VP Fraud Operations.
- Change 1456: VEL-01 threshold adjusted on 2026-07-26 following quality review finding QR-928. Approved by VP Fraud Operations.
- Change 1457: ATO-01 threshold adjusted on 2026-08-06 following quality review finding QR-644. Approved by VP Fraud Operations.
- Change 1458: MCC-02 threshold adjusted on 2026-06-03 following quality review finding QR-939. Approved by VP Fraud Operations.
- Change 1459: DEV-02 threshold adjusted on 2026-08-13 following quality review finding QR-961. Approved by VP Fraud Operations.
- Change 1460: GEO-03 threshold adjusted on 2026-03-06 following quality review finding QR-330. Approved by VP Fraud Operations.
- Change 1461: GEO-01 threshold adjusted on 2026-03-19 following quality review finding QR-676. Approved by VP Fraud Operations.
- Change 1462: MCC-02 threshold adjusted on 2026-03-20 following quality review finding QR-810. Approved by VP Fraud Operations.
- Change 1463: ATM-03 threshold adjusted on 2026-06-05 following quality review finding QR-761. Approved by VP Fraud Operations.
- Change 1464: ENT-04 threshold adjusted on 2026-03-01 following quality review finding QR-214. Approved by VP Fraud Operations.
- Change 1465: MCC-02 threshold adjusted on 2026-02-17 following quality review finding QR-967. Approved by VP Fraud Operations.
- Change 1466: VEL-02 threshold adjusted on 2026-07-28 following quality review finding QR-399. Approved by VP Fraud Operations.
- Change 1467: ATO-01 threshold adjusted on 2026-01-09 following quality review finding QR-417. Approved by VP Fraud Operations.
- Change 1468: AMT-01 threshold adjusted on 2026-09-08 following quality review finding QR-982. Approved by VP Fraud Operations.
- Change 1469: DUP-01 threshold adjusted on 2026-06-09 following quality review finding QR-757. Approved by VP Fraud Operations.
- Change 1470: ATM-01 threshold adjusted on 2026-03-02 following quality review finding QR-957. Approved by VP Fraud Operations.
- Change 1471: DEV-01 threshold adjusted on 2026-08-22 following quality review finding QR-797. Approved by VP Fraud Operations.
- Change 1472: ENT-01 threshold adjusted on 2026-07-27 following quality review finding QR-713. Approved by VP Fraud Operations.
- Change 1473: VEL-02 threshold adjusted on 2026-09-05 following quality review finding QR-736. Approved by VP Fraud Operations.
- Change 1474: ENT-01 threshold adjusted on 2026-01-28 following quality review finding QR-650. Approved by VP Fraud Operations.
- Change 1475: VEL-03 threshold adjusted on 2026-01-25 following quality review finding QR-353. Approved by VP Fraud Operations.
- Change 1476: VEL-03 threshold adjusted on 2026-03-16 following quality review finding QR-833. Approved by VP Fraud Operations.
- Change 1477: VEL-01 threshold adjusted on 2026-09-02 following quality review finding QR-533. Approved by VP Fraud Operations.
- Change 1478: DIS-01 threshold adjusted on 2026-09-17 following quality review finding QR-768. Approved by VP Fraud Operations.
- Change 1479: ATM-03 threshold adjusted on 2026-02-18 following quality review finding QR-258. Approved by VP Fraud Operations.
- Change 1480: ATO-02 threshold adjusted on 2026-04-09 following quality review finding QR-243. Approved by VP Fraud Operations.
- Change 1481: VEL-01 threshold adjusted on 2026-09-15 following quality review finding QR-775. Approved by VP Fraud Operations.
- Change 1482: GEO-01 threshold adjusted on 2026-02-15 following quality review finding QR-533. Approved by VP Fraud Operations.
- Change 1483: MCC-01 threshold adjusted on 2026-09-20 following quality review finding QR-724. Approved by VP Fraud Operations.
- Change 1484: ATO-01 threshold adjusted on 2026-05-15 following quality review finding QR-720. Approved by VP Fraud Operations.
- Change 1485: ENT-04 threshold adjusted on 2026-08-17 following quality review finding QR-453. Approved by VP Fraud Operations.
- Change 1486: ENT-01 threshold adjusted on 2026-05-18 following quality review finding QR-407. Approved by VP Fraud Operations.
- Change 1487: ATM-02 threshold adjusted on 2026-03-14 following quality review finding QR-324. Approved by VP Fraud Operations.
- Change 1488: DEV-02 threshold adjusted on 2026-08-11 following quality review finding QR-274. Approved by VP Fraud Operations.
- Change 1489: DIS-01 threshold adjusted on 2026-04-14 following quality review finding QR-274. Approved by VP Fraud Operations.
- Change 1490: ATO-01 threshold adjusted on 2026-05-26 following quality review finding QR-325. Approved by VP Fraud Operations.
- Change 1491: VEL-02 threshold adjusted on 2026-06-05 following quality review finding QR-459. Approved by VP Fraud Operations.
- Change 1492: VEL-02 threshold adjusted on 2026-08-08 following quality review finding QR-964. Approved by VP Fraud Operations.
- Change 1493: VEL-01 threshold adjusted on 2026-07-16 following quality review finding QR-366. Approved by VP Fraud Operations.
- Change 1494: DIS-01 threshold adjusted on 2026-04-06 following quality review finding QR-923. Approved by VP Fraud Operations.
- Change 1495: ATM-01 threshold adjusted on 2026-09-13 following quality review finding QR-547. Approved by VP Fraud Operations.
- Change 1496: ATM-01 threshold adjusted on 2026-04-12 following quality review finding QR-526. Approved by VP Fraud Operations.
- Change 1497: GEO-03 threshold adjusted on 2026-06-01 following quality review finding QR-546. Approved by VP Fraud Operations.
- Change 1498: ENT-04 threshold adjusted on 2026-08-15 following quality review finding QR-920. Approved by VP Fraud Operations.
- Change 1499: GEO-01 threshold adjusted on 2026-07-11 following quality review finding QR-729. Approved by VP Fraud Operations.
- Change 1500: MCC-01 threshold adjusted on 2026-05-17 following quality review finding QR-265. Approved by VP Fraud Operations.
- Change 1501: VEL-01 threshold adjusted on 2026-04-04 following quality review finding QR-286. Approved by VP Fraud Operations.
- Change 1502: ATO-03 threshold adjusted on 2026-05-02 following quality review finding QR-997. Approved by VP Fraud Operations.
- Change 1503: VEL-03 threshold adjusted on 2026-05-25 following quality review finding QR-332. Approved by VP Fraud Operations.
- Change 1504: ATM-01 threshold adjusted on 2026-05-13 following quality review finding QR-352. Approved by VP Fraud Operations.
- Change 1505: ENT-04 threshold adjusted on 2026-09-19 following quality review finding QR-706. Approved by VP Fraud Operations.
- Change 1506: AMT-02 threshold adjusted on 2026-02-09 following quality review finding QR-258. Approved by VP Fraud Operations.
- Change 1507: VEL-03 threshold adjusted on 2026-07-03 following quality review finding QR-475. Approved by VP Fraud Operations.
- Change 1508: GEO-01 threshold adjusted on 2026-02-26 following quality review finding QR-466. Approved by VP Fraud Operations.
- Change 1509: GEO-03 threshold adjusted on 2026-04-03 following quality review finding QR-470. Approved by VP Fraud Operations.
- Change 1510: VEL-01 threshold adjusted on 2026-08-01 following quality review finding QR-547. Approved by VP Fraud Operations.
- Change 1511: ENT-04 threshold adjusted on 2026-07-09 following quality review finding QR-836. Approved by VP Fraud Operations.
- Change 1512: VEL-02 threshold adjusted on 2026-01-17 following quality review finding QR-926. Approved by VP Fraud Operations.
- Change 1513: ATO-02 threshold adjusted on 2026-02-06 following quality review finding QR-468. Approved by VP Fraud Operations.
- Change 1514: GEO-02 threshold adjusted on 2026-03-07 following quality review finding QR-519. Approved by VP Fraud Operations.
- Change 1515: MCC-02 threshold adjusted on 2026-05-17 following quality review finding QR-977. Approved by VP Fraud Operations.
- Change 1516: ATO-01 threshold adjusted on 2026-05-15 following quality review finding QR-712. Approved by VP Fraud Operations.
- Change 1517: DIS-01 threshold adjusted on 2026-03-09 following quality review finding QR-555. Approved by VP Fraud Operations.
- Change 1518: GEO-01 threshold adjusted on 2026-05-02 following quality review finding QR-215. Approved by VP Fraud Operations.
- Change 1519: GEO-01 threshold adjusted on 2026-09-18 following quality review finding QR-394. Approved by VP Fraud Operations.
- Change 1520: ENT-01 threshold adjusted on 2026-08-08 following quality review finding QR-657. Approved by VP Fraud Operations.

## Appendix B. Merchant category risk table

Risk tier drives the MCC-01 rule and informs analyst judgment on unfamiliar merchants.

| MCC | Description | Risk tier | Guidance |
|---|---|---|---|
| 0742 | Veterinary services | Low | Clear on consistent history. |
| 4112 | Passenger railways | Low | Clear on consistent history. |
| 4722 | Travel agencies | Medium | Weigh with device and geography signals. |
| 4816 | Computer network services | Low | Clear on consistent history. |
| 4829 | Money transfer | High | Hold unless history at this merchant or confirmed contact. |
| 4899 | Cable and streaming services | Low | Clear on consistent history. |
| 5045 | Computers and peripherals | Medium | Weigh with device and geography signals. |
| 5251 | Hardware stores | Low | Clear on consistent history. |
| 5261 | Nurseries and garden supply | Low | Clear on consistent history. |
| 5311 | Department stores | Low | Clear on consistent history. |
| 5399 | Miscellaneous general merchandise | Medium | Weigh with device and geography signals. |
| 5411 | Grocery stores | Low | Clear on consistent history. |
| 5499 | Miscellaneous food stores | Low | Clear on consistent history. |
| 5541 | Service stations | Medium | Weigh with device and geography signals. |
| 5542 | Automated fuel dispensers | High | Hold unless history at this merchant or confirmed contact. |
| 5712 | Furniture stores | Low | Clear on consistent history. |
| 5732 | Electronics stores | Medium | Weigh with device and geography signals. |
| 5812 | Restaurants | Low | Clear on consistent history. |
| 5815 | Digital goods: media | Medium | Weigh with device and geography signals. |
| 5816 | Digital goods: games | High | Hold unless history at this merchant or confirmed contact. |
| 5912 | Drug stores | Low | Clear on consistent history. |
| 5941 | Sporting goods | Low | Clear on consistent history. |
| 5944 | Jewelry stores | High | Hold unless history at this merchant or confirmed contact. |
| 5967 | Direct marketing, inbound | High | Hold unless history at this merchant or confirmed contact. |
| 6010 | Financial institutions, manual cash | High | Hold unless history at this merchant or confirmed contact. |
| 6011 | ATM cash | Medium | Weigh with device and geography signals. |
| 6051 | Quasi-cash, crypto on-ramps | High | Hold unless history at this merchant or confirmed contact. |
| 7011 | Hotels | Low | Clear on consistent history. |
| 7538 | Auto service shops | Low | Clear on consistent history. |
| 7801 | Online gambling | High | Hold unless history at this merchant or confirmed contact. |
| 7995 | Betting | High | Hold unless history at this merchant or confirmed contact. |
| 7997 | Membership clubs | Low | Clear on consistent history. |
| 8021 | Dentists | Low | Clear on consistent history. |

### B.1 Merchant-level overrides

- Override 001: QuickCart Retail, acquirer ID 790298: no override, monitor (review QR-455).
- Override 002: Meadow Meal Kits, acquirer ID 975156: no override, monitor (review QR-519).
- Override 003: Orbit Travel Booking, acquirer ID 821149: treat as Medium (review QR-348).
- Override 004: Brightwave Digital Goods, acquirer ID 308272: treat as Medium (review QR-455).
- Override 005: Brightwave Digital Goods, acquirer ID 157030: treat as Medium (review QR-311).
- Override 006: QuickCart Retail, acquirer ID 755830: treat as High (review QR-455).
- Override 007: Pixelhaus Electronics, acquirer ID 158092: treat as Low (review QR-455).
- Override 008: Meadow Meal Kits, acquirer ID 803115: treat as High (review QR-519).
- Override 009: Nimbus Game Store, acquirer ID 826333: treat as High (review QR-311).
- Override 010: Streamflix Subscription, acquirer ID 294355: treat as Medium (review QR-402).
- Override 011: Streamflix Subscription, acquirer ID 103798: treat as High (review QR-402).
- Override 012: Brightwave Digital Goods, acquirer ID 673648: treat as High (review QR-348).
- Override 013: Everline Marketplace, acquirer ID 424584: treat as Medium (review QR-402).
- Override 014: Pixelhaus Electronics, acquirer ID 101120: treat as High (review QR-455).
- Override 015: QuickCart Retail, acquirer ID 597699: treat as High (review QR-519).
- Override 016: Nimbus Game Store, acquirer ID 360234: treat as Low (review QR-311).
- Override 017: Orbit Travel Booking, acquirer ID 956733: treat as Low (review QR-348).
- Override 018: Cloudbox Storage, acquirer ID 715305: treat as Low (review QR-455).
- Override 019: Everline Marketplace, acquirer ID 414201: treat as High (review QR-348).
- Override 020: QuickCart Retail, acquirer ID 714028: treat as Medium (review QR-519).
- Override 021: Cloudbox Storage, acquirer ID 901438: treat as High (review QR-455).
- Override 022: Pixelhaus Electronics, acquirer ID 397980: treat as Medium (review QR-311).
- Override 023: Meadow Meal Kits, acquirer ID 757805: no override, monitor (review QR-519).
- Override 024: Pixelhaus Electronics, acquirer ID 649199: treat as Low (review QR-519).
- Override 025: Nimbus Game Store, acquirer ID 189225: treat as Low (review QR-311).
- Override 026: Pixelhaus Electronics, acquirer ID 768068: treat as High (review QR-311).
- Override 027: Cloudbox Storage, acquirer ID 976422: no override, monitor (review QR-519).
- Override 028: Everline Marketplace, acquirer ID 758261: treat as Low (review QR-519).
- Override 029: Nimbus Game Store, acquirer ID 613062: treat as High (review QR-311).
- Override 030: Streamflix Subscription, acquirer ID 936446: treat as Low (review QR-519).
- Override 031: Meadow Meal Kits, acquirer ID 196408: treat as Low (review QR-455).
- Override 032: Orbit Travel Booking, acquirer ID 948527: treat as Low (review QR-402).
- Override 033: Nimbus Game Store, acquirer ID 864763: treat as Medium (review QR-348).
- Override 034: Streamflix Subscription, acquirer ID 617942: no override, monitor (review QR-311).
- Override 035: Streamflix Subscription, acquirer ID 816907: treat as High (review QR-311).
- Override 036: Juniper Fitness App, acquirer ID 763531: treat as Medium (review QR-311).
- Override 037: Juniper Fitness App, acquirer ID 254586: treat as High (review QR-402).
- Override 038: Orbit Travel Booking, acquirer ID 751323: treat as Medium (review QR-311).
- Override 039: Streamflix Subscription, acquirer ID 163607: no override, monitor (review QR-402).
- Override 040: QuickCart Retail, acquirer ID 825808: treat as Medium (review QR-455).
- Override 041: Orbit Travel Booking, acquirer ID 843305: treat as High (review QR-455).
- Override 042: Streamflix Subscription, acquirer ID 588992: treat as Low (review QR-519).
- Override 043: Nimbus Game Store, acquirer ID 426814: treat as Low (review QR-455).
- Override 044: Everline Marketplace, acquirer ID 403655: no override, monitor (review QR-311).
- Override 045: Meadow Meal Kits, acquirer ID 571283: treat as High (review QR-455).
- Override 046: Nimbus Game Store, acquirer ID 320944: treat as Low (review QR-519).
- Override 047: QuickCart Retail, acquirer ID 248625: treat as High (review QR-402).
- Override 048: Pixelhaus Electronics, acquirer ID 732674: treat as High (review QR-311).
- Override 049: Brightwave Digital Goods, acquirer ID 342623: no override, monitor (review QR-455).
- Override 050: Cloudbox Storage, acquirer ID 126040: treat as Medium (review QR-311).
- Override 051: Streamflix Subscription, acquirer ID 814696: no override, monitor (review QR-455).
- Override 052: Orbit Travel Booking, acquirer ID 862506: treat as Medium (review QR-455).
- Override 053: Brightwave Digital Goods, acquirer ID 494375: treat as High (review QR-311).
- Override 054: Brightwave Digital Goods, acquirer ID 101825: treat as High (review QR-402).
- Override 055: Cloudbox Storage, acquirer ID 225872: treat as Medium (review QR-311).
- Override 056: Orbit Travel Booking, acquirer ID 365512: treat as High (review QR-311).
- Override 057: Cloudbox Storage, acquirer ID 509113: treat as Low (review QR-402).
- Override 058: Cloudbox Storage, acquirer ID 892363: treat as High (review QR-311).
- Override 059: Orbit Travel Booking, acquirer ID 206650: treat as Low (review QR-402).
- Override 060: Pixelhaus Electronics, acquirer ID 361435: treat as High (review QR-455).
- Override 061: Meadow Meal Kits, acquirer ID 430932: treat as Medium (review QR-402).
- Override 062: Cloudbox Storage, acquirer ID 130420: no override, monitor (review QR-519).
- Override 063: Meadow Meal Kits, acquirer ID 313317: treat as Low (review QR-311).
- Override 064: Cloudbox Storage, acquirer ID 572761: treat as Medium (review QR-402).
- Override 065: Streamflix Subscription, acquirer ID 151356: treat as Medium (review QR-348).
- Override 066: Streamflix Subscription, acquirer ID 535019: treat as High (review QR-402).
- Override 067: Orbit Travel Booking, acquirer ID 368165: treat as High (review QR-455).
- Override 068: Nimbus Game Store, acquirer ID 415449: no override, monitor (review QR-519).
- Override 069: Cloudbox Storage, acquirer ID 225559: treat as Medium (review QR-348).
- Override 070: QuickCart Retail, acquirer ID 317970: no override, monitor (review QR-519).
- Override 071: Nimbus Game Store, acquirer ID 574990: treat as High (review QR-455).
- Override 072: Cloudbox Storage, acquirer ID 246377: treat as Medium (review QR-348).
- Override 073: QuickCart Retail, acquirer ID 283181: treat as High (review QR-519).
- Override 074: QuickCart Retail, acquirer ID 434797: treat as Medium (review QR-402).
- Override 075: Orbit Travel Booking, acquirer ID 948673: treat as Medium (review QR-311).
- Override 076: Cloudbox Storage, acquirer ID 501434: no override, monitor (review QR-519).
- Override 077: Nimbus Game Store, acquirer ID 495172: treat as High (review QR-402).
- Override 078: Everline Marketplace, acquirer ID 622343: treat as High (review QR-519).
- Override 079: Brightwave Digital Goods, acquirer ID 231988: treat as Medium (review QR-311).
- Override 080: Orbit Travel Booking, acquirer ID 360522: no override, monitor (review QR-455).
- Override 081: Streamflix Subscription, acquirer ID 552813: treat as High (review QR-311).
- Override 082: Pixelhaus Electronics, acquirer ID 133809: no override, monitor (review QR-455).
- Override 083: Juniper Fitness App, acquirer ID 613618: treat as Low (review QR-311).
- Override 084: Cloudbox Storage, acquirer ID 965693: no override, monitor (review QR-455).
- Override 085: Nimbus Game Store, acquirer ID 921147: treat as Low (review QR-348).
- Override 086: Pixelhaus Electronics, acquirer ID 259455: treat as Low (review QR-455).
- Override 087: QuickCart Retail, acquirer ID 678290: treat as Low (review QR-311).
- Override 088: Pixelhaus Electronics, acquirer ID 343874: treat as Low (review QR-402).
- Override 089: Pixelhaus Electronics, acquirer ID 756904: treat as High (review QR-519).
- Override 090: Cloudbox Storage, acquirer ID 832516: treat as Low (review QR-311).
- Override 091: QuickCart Retail, acquirer ID 414939: treat as Medium (review QR-455).
- Override 092: Orbit Travel Booking, acquirer ID 334443: treat as Low (review QR-311).
- Override 093: Meadow Meal Kits, acquirer ID 416167: no override, monitor (review QR-402).
- Override 094: Brightwave Digital Goods, acquirer ID 775886: treat as Medium (review QR-455).
- Override 095: Meadow Meal Kits, acquirer ID 346172: treat as Medium (review QR-311).
- Override 096: Cloudbox Storage, acquirer ID 838882: treat as High (review QR-311).
- Override 097: Everline Marketplace, acquirer ID 303544: no override, monitor (review QR-455).
- Override 098: QuickCart Retail, acquirer ID 369752: treat as Medium (review QR-455).
- Override 099: Brightwave Digital Goods, acquirer ID 337802: no override, monitor (review QR-311).
- Override 100: Brightwave Digital Goods, acquirer ID 853225: no override, monitor (review QR-402).
- Override 101: Cloudbox Storage, acquirer ID 307701: treat as Low (review QR-402).
- Override 102: Meadow Meal Kits, acquirer ID 170708: treat as Medium (review QR-455).
- Override 103: Nimbus Game Store, acquirer ID 426857: treat as Medium (review QR-348).
- Override 104: Streamflix Subscription, acquirer ID 332199: treat as High (review QR-402).
- Override 105: QuickCart Retail, acquirer ID 753888: no override, monitor (review QR-519).
- Override 106: Pixelhaus Electronics, acquirer ID 334172: no override, monitor (review QR-455).
- Override 107: Everline Marketplace, acquirer ID 723695: treat as Medium (review QR-455).
- Override 108: Everline Marketplace, acquirer ID 323293: treat as Low (review QR-519).
- Override 109: Pixelhaus Electronics, acquirer ID 535562: treat as Low (review QR-311).
- Override 110: Pixelhaus Electronics, acquirer ID 512427: no override, monitor (review QR-402).
- Override 111: QuickCart Retail, acquirer ID 183216: treat as Medium (review QR-402).
- Override 112: Nimbus Game Store, acquirer ID 294523: no override, monitor (review QR-311).
- Override 113: Orbit Travel Booking, acquirer ID 796705: no override, monitor (review QR-402).
- Override 114: Brightwave Digital Goods, acquirer ID 563926: treat as Medium (review QR-311).
- Override 115: Everline Marketplace, acquirer ID 182042: treat as High (review QR-311).
- Override 116: Brightwave Digital Goods, acquirer ID 540593: treat as Low (review QR-519).
- Override 117: Nimbus Game Store, acquirer ID 498594: treat as High (review QR-402).
- Override 118: Cloudbox Storage, acquirer ID 192023: treat as Low (review QR-455).
- Override 119: Nimbus Game Store, acquirer ID 490819: no override, monitor (review QR-348).
- Override 120: Brightwave Digital Goods, acquirer ID 481942: no override, monitor (review QR-311).
- Override 121: Cloudbox Storage, acquirer ID 360060: no override, monitor (review QR-311).
- Override 122: Cloudbox Storage, acquirer ID 136547: no override, monitor (review QR-311).
- Override 123: Everline Marketplace, acquirer ID 369500: treat as Medium (review QR-311).
- Override 124: Juniper Fitness App, acquirer ID 455540: treat as High (review QR-402).
- Override 125: Brightwave Digital Goods, acquirer ID 746948: treat as Low (review QR-402).
- Override 126: Brightwave Digital Goods, acquirer ID 389019: treat as High (review QR-311).
- Override 127: Juniper Fitness App, acquirer ID 944794: treat as Low (review QR-311).
- Override 128: Nimbus Game Store, acquirer ID 212471: no override, monitor (review QR-455).
- Override 129: Cloudbox Storage, acquirer ID 928164: treat as High (review QR-455).
- Override 130: Streamflix Subscription, acquirer ID 239153: no override, monitor (review QR-348).
- Override 131: Everline Marketplace, acquirer ID 941553: treat as High (review QR-348).
- Override 132: Juniper Fitness App, acquirer ID 347613: treat as High (review QR-402).
- Override 133: Streamflix Subscription, acquirer ID 479436: treat as Low (review QR-519).
- Override 134: Nimbus Game Store, acquirer ID 510711: treat as Medium (review QR-348).
- Override 135: Cloudbox Storage, acquirer ID 167877: treat as Low (review QR-455).
- Override 136: Meadow Meal Kits, acquirer ID 671071: treat as High (review QR-348).
- Override 137: Cloudbox Storage, acquirer ID 210332: treat as Low (review QR-402).
- Override 138: Juniper Fitness App, acquirer ID 188166: treat as Medium (review QR-311).
- Override 139: Cloudbox Storage, acquirer ID 622689: no override, monitor (review QR-348).
- Override 140: Nimbus Game Store, acquirer ID 239388: no override, monitor (review QR-455).
- Override 141: Juniper Fitness App, acquirer ID 806854: treat as Medium (review QR-519).
- Override 142: QuickCart Retail, acquirer ID 917627: treat as High (review QR-402).
- Override 143: Orbit Travel Booking, acquirer ID 694421: treat as High (review QR-402).
- Override 144: Orbit Travel Booking, acquirer ID 873919: treat as High (review QR-348).
- Override 145: Streamflix Subscription, acquirer ID 359448: treat as Medium (review QR-348).
- Override 146: Nimbus Game Store, acquirer ID 260769: treat as High (review QR-519).
- Override 147: Nimbus Game Store, acquirer ID 442190: treat as Low (review QR-455).
- Override 148: Orbit Travel Booking, acquirer ID 357896: treat as Medium (review QR-311).
- Override 149: Streamflix Subscription, acquirer ID 138821: treat as Low (review QR-311).
- Override 150: Streamflix Subscription, acquirer ID 958891: treat as Medium (review QR-455).
- Override 151: Brightwave Digital Goods, acquirer ID 142322: treat as High (review QR-348).
- Override 152: QuickCart Retail, acquirer ID 152838: treat as Medium (review QR-519).
- Override 153: Juniper Fitness App, acquirer ID 303593: treat as Low (review QR-402).
- Override 154: Meadow Meal Kits, acquirer ID 286393: no override, monitor (review QR-519).
- Override 155: Orbit Travel Booking, acquirer ID 912644: treat as Low (review QR-311).
- Override 156: Juniper Fitness App, acquirer ID 844180: treat as High (review QR-348).
- Override 157: Everline Marketplace, acquirer ID 486618: treat as High (review QR-348).
- Override 158: Everline Marketplace, acquirer ID 313884: treat as High (review QR-311).
- Override 159: Juniper Fitness App, acquirer ID 867797: treat as Medium (review QR-311).
- Override 160: Brightwave Digital Goods, acquirer ID 528862: treat as High (review QR-348).

## Appendix C. Country risk list

| Code | Country | Tier | Cash guidance | Card-present guidance |
|---|---|---|---|---|
| CA | Canada | Standard | Clear with notice; hold without. | Clear on chip with history or notice. |
| MX | Mexico | Standard | Clear with notice; hold without. | Clear on chip with history or notice. |
| GB | United Kingdom | Standard | Clear with notice; hold without. | Clear on chip with history or notice. |
| PT | Portugal | Standard | Clear with notice; hold without. | Clear on chip with history or notice. |
| ES | Spain | Standard | Clear with notice; hold without. | Clear on chip with history or notice. |
| IE | Ireland | Standard | Clear with notice; hold without. | Clear on chip with history or notice. |
| JP | Japan | Standard | Clear with notice; hold without. | Clear on chip with history or notice. |
| TH | Thailand | Elevated | Hold without notice. | Hold without history. |
| TR | Turkey | Elevated | Hold without notice. | Hold without history. |
| NG | Nigeria | Elevated | Hold without notice. | Hold without history. |
| RO | Romania | Elevated | Hold without notice. | Hold without history. |
| PH | Philippines | Elevated | Hold without notice. | Hold without history. |
| VN | Vietnam | Elevated | Hold without notice. | Hold without history. |
| BR | Brazil | Elevated | Hold without notice. | Hold without history. |
| ID | Indonesia | Elevated | Hold without notice. | Hold without history. |
| GH | Ghana | Elevated | Hold without notice. | Hold without history. |
| UA | Ukraine | Elevated | Hold without notice. | Hold without history. |
| PK | Pakistan | Elevated | Hold without notice. | Hold without history. |

### C.1 Seasonal adjustments

- Nigeria: notice volume rises 29% in March; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Mexico: notice volume rises 83% in August; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Ghana: notice volume rises 28% in July; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Portugal: notice volume rises 70% in October; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Pakistan: notice volume rises 39% in October; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Pakistan: notice volume rises 31% in October; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Ireland: notice volume rises 70% in October; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Turkey: notice volume rises 72% in June; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Nigeria: notice volume rises 73% in December; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Nigeria: notice volume rises 65% in July; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Brazil: notice volume rises 22% in June; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Japan: notice volume rises 70% in October; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Vietnam: notice volume rises 46% in December; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Brazil: notice volume rises 40% in July; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Portugal: notice volume rises 31% in July; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Philippines: notice volume rises 78% in March; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Spain: notice volume rises 21% in December; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Pakistan: notice volume rises 38% in October; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Vietnam: notice volume rises 31% in August; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Philippines: notice volume rises 84% in March; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Spain: notice volume rises 64% in June; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Ireland: notice volume rises 86% in March; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- United Kingdom: notice volume rises 33% in July; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Ghana: notice volume rises 45% in June; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Spain: notice volume rises 25% in July; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Romania: notice volume rises 26% in August; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Vietnam: notice volume rises 31% in October; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Ireland: notice volume rises 48% in August; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Vietnam: notice volume rises 45% in July; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Ireland: notice volume rises 47% in December; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Vietnam: notice volume rises 86% in March; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Vietnam: notice volume rises 65% in December; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Spain: notice volume rises 51% in October; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Japan: notice volume rises 25% in August; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Mexico: notice volume rises 61% in December; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Vietnam: notice volume rises 78% in August; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Nigeria: notice volume rises 73% in June; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Thailand: notice volume rises 74% in July; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Philippines: notice volume rises 77% in August; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Indonesia: notice volume rises 42% in December; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Canada: notice volume rises 82% in July; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Thailand: notice volume rises 77% in August; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Indonesia: notice volume rises 42% in July; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Vietnam: notice volume rises 33% in December; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Spain: notice volume rises 65% in July; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Philippines: notice volume rises 31% in July; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Ukraine: notice volume rises 85% in October; GEO-01 false positives rise accordingly. Analysts should expect more clears.
- Mexico: notice volume rises 25% in October; GEO-01 false positives rise accordingly. Analysts should expect more clears.

## Appendix D. Customer contact scripts

### D.1 Outbound verification call

Hello, this is [name] calling from Fernhill Bank's fraud department. I am calling about activity on your card ending in [last four]. Before we continue, I will never ask you for your full card number, your PIN, or your online banking password.

Can I confirm I am speaking with [cardholder name]? Thank you. To verify your identity I will ask three questions from your account profile.

We saw a transaction of [amount] at [merchant] on [date]. Did you make that purchase?

If yes: thank you, I will note your card as confirmed and remove the hold now. If no: I am going to block this card immediately and issue a replacement. You will not be responsible for this transaction.

### D.2 Voicemail

This is Fernhill Bank's fraud department calling about recent activity on your card ending in [last four]. Please call us back at the number on the back of your card. We will never ask for your full card number, PIN, or password.

### D.3 SMS

Fernhill Bank: we noticed unusual activity on your card ending [last four]. Reply YES if you made a purchase of [amount] at [merchant], or NO if you did not. We will never ask for your card number or PIN by text.

### D.4 Inbound dispute intake

Thank you for calling Fernhill Bank. I understand you want to report a transaction you do not recognize. I will take the details and place a block on the card while we investigate.

Please confirm the merchant, amount and date as they appear on your statement. Have you shared your card with anyone, or used it at a merchant you have not used before?

I have recorded the dispute. A provisional credit will post within [n] business days. You will receive a letter with the case number.


## Appendix E. Quality review findings, 2026 year to date

| Finding | Date | Rule | Summary | Outcome |
|---|---|---|---|---|
| QR-301 | 2026-03-03 | AMT-02 | Correct escalation, exemplary reason | Coaching |
| QR-302 | 2026-01-25 | ENT-01 | Contact made to recently changed phone number | No action |
| QR-303 | 2026-01-28 | GEO-03 | Terminal replacement false positive cleared correctly | Coaching |
| QR-304 | 2026-04-05 | ATM-03 | Recurring merchant escalated in error | No action |
| QR-305 | 2026-04-03 | DEV-01 | Terminal replacement false positive cleared correctly | Procedure updated |
| QR-306 | 2026-03-11 | MCC-01 | Recurring merchant escalated in error | Reported to InfoSec |
| QR-307 | 2026-03-09 | ENT-01 | Disposition reason copied from prior case | No action |
| QR-308 | 2026-05-20 | ENT-01 | Card number pasted into case note | Procedure updated |
| QR-309 | 2026-06-02 | ATO-01 | Hold exceeded 48 hours without contact attempt | Reported to InfoSec |
| QR-310 | 2026-03-21 | ATO-03 | Enrichment missing; analyst cleared large online purchase | Reported to InfoSec |
| QR-311 | 2026-03-26 | ATO-03 | Escalation lacked written reason | Commended |
| QR-312 | 2026-01-21 | DEV-01 | Disposition reason copied from prior case | Commended |
| QR-313 | 2026-09-19 | VEL-01 | Recurring merchant escalated in error | Commended |
| QR-314 | 2026-07-24 | DEV-01 | Recurring merchant escalated in error | Reported to InfoSec |
| QR-315 | 2026-06-19 | VEL-02 | Enrichment missing; analyst cleared large online purchase | Procedure updated |
| QR-316 | 2026-02-15 | ATO-02 | Hold exceeded 48 hours without contact attempt | Commended |
| QR-317 | 2026-01-10 | ENT-01 | Recurring merchant escalated in error | Procedure updated |
| QR-318 | 2026-06-24 | GEO-01 | Analyst cleared without travel notice check | No action |
| QR-319 | 2026-03-10 | MCC-01 | Contact made to recently changed phone number | Reported to InfoSec |
| QR-320 | 2026-09-12 | GEO-02 | Hold exceeded 48 hours without contact attempt | Reported to InfoSec |
| QR-321 | 2026-04-20 | MCC-02 | Analyst cleared without travel notice check | Coaching |
| QR-322 | 2026-01-01 | DUP-01 | Enrichment missing; analyst cleared large online purchase | Procedure updated |
| QR-323 | 2026-02-17 | DEV-01 | Correct escalation, exemplary reason | No action |
| QR-324 | 2026-07-19 | AMT-01 | Terminal replacement false positive cleared correctly | No action |
| QR-325 | 2026-04-12 | MCC-01 | Disposition reason copied from prior case | No action |
| QR-326 | 2026-03-01 | ATO-02 | Hold exceeded 48 hours without contact attempt | Reported to InfoSec |
| QR-327 | 2026-02-03 | MCC-02 | Hold exceeded 48 hours without contact attempt | Procedure updated |
| QR-328 | 2026-07-26 | ATO-03 | Analyst cleared without travel notice check | Coaching |
| QR-329 | 2026-09-12 | MCC-01 | Terminal replacement false positive cleared correctly | Reported to InfoSec |
| QR-330 | 2026-09-24 | ATM-03 | Card number pasted into case note | No action |
| QR-331 | 2026-01-02 | GEO-02 | Correct escalation, exemplary reason | Coaching |
| QR-332 | 2026-07-06 | ATO-02 | Hold exceeded 48 hours without contact attempt | Coaching |
| QR-333 | 2026-02-01 | MCC-01 | Correct escalation, exemplary reason | No action |
| QR-334 | 2026-03-14 | ATO-01 | Correct escalation, exemplary reason | Commended |
| QR-335 | 2026-09-21 | MCC-02 | Contact made to recently changed phone number | Commended |
| QR-336 | 2026-03-17 | AMT-01 | Escalation lacked written reason | Procedure updated |
| QR-337 | 2026-01-24 | ATM-03 | Correct escalation, exemplary reason | Coaching |
| QR-338 | 2026-07-28 | ATM-01 | Disposition reason copied from prior case | Coaching |
| QR-339 | 2026-08-06 | ATO-02 | Escalation lacked written reason | Procedure updated |
| QR-340 | 2026-04-21 | GEO-02 | Escalation lacked written reason | Procedure updated |
| QR-341 | 2026-05-23 | GEO-02 | Recurring merchant escalated in error | Commended |
| QR-342 | 2026-07-22 | ENT-01 | Recurring merchant escalated in error | Procedure updated |
| QR-343 | 2026-04-03 | ENT-01 | Analyst cleared without travel notice check | No action |
| QR-344 | 2026-05-08 | ATO-01 | Hold exceeded 48 hours without contact attempt | Procedure updated |
| QR-345 | 2026-04-13 | AMT-02 | Terminal replacement false positive cleared correctly | No action |
| QR-346 | 2026-07-28 | MCC-02 | Correct escalation, exemplary reason | Reported to InfoSec |
| QR-347 | 2026-08-27 | ENT-01 | Analyst cleared without travel notice check | Coaching |
| QR-348 | 2026-07-24 | ATO-02 | Terminal replacement false positive cleared correctly | Procedure updated |
| QR-349 | 2026-04-13 | MCC-01 | Terminal replacement false positive cleared correctly | Coaching |
| QR-350 | 2026-03-05 | GEO-02 | Analyst cleared without travel notice check | Coaching |
| QR-351 | 2026-02-20 | VEL-03 | Enrichment missing; analyst cleared large online purchase | No action |
| QR-352 | 2026-01-01 | GEO-02 | Hold exceeded 48 hours without contact attempt | Coaching |
| QR-353 | 2026-02-24 | GEO-02 | Escalation lacked written reason | Commended |
| QR-354 | 2026-06-07 | ENT-04 | Escalation lacked written reason | Reported to InfoSec |
| QR-355 | 2026-02-08 | ATO-01 | Card number pasted into case note | Coaching |
| QR-356 | 2026-01-02 | MCC-02 | Escalation lacked written reason | Procedure updated |
| QR-357 | 2026-08-04 | VEL-02 | Escalation lacked written reason | No action |
| QR-358 | 2026-05-11 | AMT-02 | Contact made to recently changed phone number | Procedure updated |
| QR-359 | 2026-01-12 | ATO-03 | Recurring merchant escalated in error | Coaching |
| QR-360 | 2026-06-11 | MCC-01 | Correct escalation, exemplary reason | Reported to InfoSec |
| QR-361 | 2026-05-20 | GEO-01 | Contact made to recently changed phone number | Coaching |
| QR-362 | 2026-07-17 | VEL-01 | Enrichment missing; analyst cleared large online purchase | Reported to InfoSec |
| QR-363 | 2026-01-18 | DUP-01 | Card number pasted into case note | Coaching |
| QR-364 | 2026-05-06 | ATM-01 | Analyst cleared without travel notice check | Commended |
| QR-365 | 2026-04-10 | GEO-02 | Analyst cleared without travel notice check | Procedure updated |
| QR-366 | 2026-08-04 | ATM-03 | Hold exceeded 48 hours without contact attempt | Reported to InfoSec |
| QR-367 | 2026-06-27 | ENT-01 | Recurring merchant escalated in error | Commended |
| QR-368 | 2026-03-10 | ATO-01 | Card number pasted into case note | Reported to InfoSec |
| QR-369 | 2026-03-04 | MCC-02 | Escalation lacked written reason | Reported to InfoSec |
| QR-370 | 2026-09-26 | VEL-01 | Enrichment missing; analyst cleared large online purchase | Procedure updated |
| QR-371 | 2026-02-13 | DEV-02 | Escalation lacked written reason | Reported to InfoSec |
| QR-372 | 2026-01-12 | ATO-01 | Recurring merchant escalated in error | Procedure updated |
| QR-373 | 2026-07-18 | ENT-01 | Hold exceeded 48 hours without contact attempt | Reported to InfoSec |
| QR-374 | 2026-04-15 | VEL-02 | Correct escalation, exemplary reason | Commended |
| QR-375 | 2026-01-12 | DUP-01 | Enrichment missing; analyst cleared large online purchase | Commended |
| QR-376 | 2026-03-28 | ATM-02 | Correct escalation, exemplary reason | Procedure updated |
| QR-377 | 2026-03-15 | ATM-02 | Recurring merchant escalated in error | Commended |
| QR-378 | 2026-04-05 | AMT-02 | Disposition reason copied from prior case | No action |
| QR-379 | 2026-09-07 | ATO-03 | Recurring merchant escalated in error | Commended |
| QR-380 | 2026-03-24 | VEL-02 | Card number pasted into case note | Procedure updated |
| QR-381 | 2026-09-12 | VEL-03 | Card number pasted into case note | Procedure updated |
| QR-382 | 2026-04-09 | VEL-01 | Hold exceeded 48 hours without contact attempt | Coaching |
| QR-383 | 2026-04-13 | VEL-02 | Hold exceeded 48 hours without contact attempt | Procedure updated |
| QR-384 | 2026-05-14 | ATO-03 | Card number pasted into case note | Coaching |
| QR-385 | 2026-02-09 | ATO-01 | Contact made to recently changed phone number | Reported to InfoSec |
| QR-386 | 2026-01-01 | DEV-02 | Contact made to recently changed phone number | No action |
| QR-387 | 2026-09-21 | AMT-01 | Disposition reason copied from prior case | Coaching |
| QR-388 | 2026-03-09 | MCC-01 | Contact made to recently changed phone number | Coaching |
| QR-389 | 2026-04-28 | ATM-01 | Terminal replacement false positive cleared correctly | Commended |
| QR-390 | 2026-07-28 | ATO-02 | Terminal replacement false positive cleared correctly | No action |
| QR-391 | 2026-03-21 | VEL-01 | Disposition reason copied from prior case | Reported to InfoSec |
| QR-392 | 2026-06-09 | MCC-02 | Escalation lacked written reason | Reported to InfoSec |
| QR-393 | 2026-04-26 | DEV-02 | Hold exceeded 48 hours without contact attempt | Procedure updated |
| QR-394 | 2026-07-16 | ATM-02 | Analyst cleared without travel notice check | Commended |
| QR-395 | 2026-07-17 | DIS-01 | Hold exceeded 48 hours without contact attempt | Procedure updated |
| QR-396 | 2026-01-13 | ATM-03 | Escalation lacked written reason | Coaching |
| QR-397 | 2026-05-18 | ATO-01 | Hold exceeded 48 hours without contact attempt | No action |
| QR-398 | 2026-09-12 | VEL-01 | Terminal replacement false positive cleared correctly | Reported to InfoSec |
| QR-399 | 2026-09-07 | ATM-03 | Correct escalation, exemplary reason | Coaching |
| QR-400 | 2026-06-17 | AMT-02 | Contact made to recently changed phone number | Reported to InfoSec |
| QR-401 | 2026-04-22 | VEL-03 | Contact made to recently changed phone number | Commended |
| QR-402 | 2026-02-24 | MCC-01 | Enrichment missing; analyst cleared large online purchase | Coaching |
| QR-403 | 2026-05-09 | DEV-02 | Contact made to recently changed phone number | Coaching |
| QR-404 | 2026-01-03 | ATM-01 | Contact made to recently changed phone number | Procedure updated |
| QR-405 | 2026-05-04 | ATO-02 | Recurring merchant escalated in error | Reported to InfoSec |
| QR-406 | 2026-09-08 | DEV-02 | Disposition reason copied from prior case | No action |
| QR-407 | 2026-03-05 | GEO-03 | Card number pasted into case note | Reported to InfoSec |
| QR-408 | 2026-09-24 | ATO-02 | Hold exceeded 48 hours without contact attempt | Procedure updated |
| QR-409 | 2026-07-15 | AMT-01 | Correct escalation, exemplary reason | No action |
| QR-410 | 2026-08-12 | ATO-02 | Recurring merchant escalated in error | Reported to InfoSec |
| QR-411 | 2026-05-14 | DIS-01 | Hold exceeded 48 hours without contact attempt | Reported to InfoSec |
| QR-412 | 2026-01-26 | ATO-03 | Enrichment missing; analyst cleared large online purchase | No action |
| QR-413 | 2026-05-11 | ATM-03 | Disposition reason copied from prior case | Reported to InfoSec |
| QR-414 | 2026-02-22 | DEV-01 | Hold exceeded 48 hours without contact attempt | Procedure updated |
| QR-415 | 2026-07-02 | GEO-03 | Terminal replacement false positive cleared correctly | Procedure updated |
| QR-416 | 2026-03-17 | DEV-01 | Terminal replacement false positive cleared correctly | Coaching |
| QR-417 | 2026-01-07 | GEO-03 | Recurring merchant escalated in error | Procedure updated |
| QR-418 | 2026-02-19 | VEL-02 | Card number pasted into case note | No action |
| QR-419 | 2026-08-12 | VEL-02 | Card number pasted into case note | Reported to InfoSec |
| QR-420 | 2026-09-06 | MCC-01 | Terminal replacement false positive cleared correctly | Coaching |
| QR-421 | 2026-09-26 | MCC-02 | Recurring merchant escalated in error | No action |
| QR-422 | 2026-08-23 | ATO-01 | Correct escalation, exemplary reason | Coaching |
| QR-423 | 2026-08-22 | VEL-01 | Correct escalation, exemplary reason | Coaching |
| QR-424 | 2026-05-14 | ATO-02 | Hold exceeded 48 hours without contact attempt | Reported to InfoSec |
| QR-425 | 2026-08-18 | GEO-02 | Disposition reason copied from prior case | Reported to InfoSec |
| QR-426 | 2026-03-23 | ATM-03 | Card number pasted into case note | Reported to InfoSec |
| QR-427 | 2026-03-18 | MCC-01 | Analyst cleared without travel notice check | No action |
| QR-428 | 2026-06-15 | DUP-01 | Disposition reason copied from prior case | Procedure updated |
| QR-429 | 2026-08-12 | ATM-01 | Contact made to recently changed phone number | Coaching |
| QR-430 | 2026-03-21 | DEV-01 | Analyst cleared without travel notice check | Coaching |
| QR-431 | 2026-01-22 | AMT-02 | Escalation lacked written reason | Commended |
| QR-432 | 2026-08-16 | VEL-02 | Analyst cleared without travel notice check | No action |
| QR-433 | 2026-07-21 | VEL-02 | Enrichment missing; analyst cleared large online purchase | Coaching |
| QR-434 | 2026-06-11 | ATM-03 | Correct escalation, exemplary reason | Commended |
| QR-435 | 2026-04-10 | ATM-01 | Enrichment missing; analyst cleared large online purchase | Reported to InfoSec |
| QR-436 | 2026-05-18 | GEO-02 | Recurring merchant escalated in error | Procedure updated |
| QR-437 | 2026-06-27 | ATM-03 | Contact made to recently changed phone number | Procedure updated |
| QR-438 | 2026-09-09 | ENT-01 | Enrichment missing; analyst cleared large online purchase | No action |
| QR-439 | 2026-08-26 | VEL-01 | Enrichment missing; analyst cleared large online purchase | No action |
| QR-440 | 2026-06-23 | AMT-01 | Hold exceeded 48 hours without contact attempt | Commended |
| QR-441 | 2026-02-26 | GEO-02 | Contact made to recently changed phone number | Commended |
| QR-442 | 2026-07-18 | DUP-01 | Analyst cleared without travel notice check | Reported to InfoSec |
| QR-443 | 2026-05-04 | GEO-01 | Analyst cleared without travel notice check | No action |
| QR-444 | 2026-08-20 | DIS-01 | Analyst cleared without travel notice check | Commended |
| QR-445 | 2026-09-20 | DEV-02 | Terminal replacement false positive cleared correctly | No action |
| QR-446 | 2026-02-07 | GEO-02 | Disposition reason copied from prior case | No action |
| QR-447 | 2026-02-22 | VEL-03 | Analyst cleared without travel notice check | Reported to InfoSec |
| QR-448 | 2026-02-21 | GEO-01 | Enrichment missing; analyst cleared large online purchase | No action |
| QR-449 | 2026-05-18 | ATO-03 | Recurring merchant escalated in error | No action |
| QR-450 | 2026-07-02 | AMT-02 | Analyst cleared without travel notice check | Reported to InfoSec |
| QR-451 | 2026-01-16 | DUP-01 | Correct escalation, exemplary reason | Coaching |
| QR-452 | 2026-02-25 | ATM-01 | Terminal replacement false positive cleared correctly | Reported to InfoSec |
| QR-453 | 2026-08-03 | GEO-01 | Contact made to recently changed phone number | Commended |
| QR-454 | 2026-03-16 | ATM-01 | Correct escalation, exemplary reason | Coaching |
| QR-455 | 2026-02-21 | ATM-03 | Card number pasted into case note | No action |
| QR-456 | 2026-01-14 | GEO-01 | Analyst cleared without travel notice check | Coaching |
| QR-457 | 2026-02-07 | VEL-01 | Hold exceeded 48 hours without contact attempt | Reported to InfoSec |
| QR-458 | 2026-01-09 | DUP-01 | Card number pasted into case note | Reported to InfoSec |
| QR-459 | 2026-03-02 | DEV-01 | Hold exceeded 48 hours without contact attempt | Coaching |
| QR-460 | 2026-05-21 | ENT-04 | Disposition reason copied from prior case | Reported to InfoSec |
| QR-461 | 2026-05-02 | GEO-02 | Analyst cleared without travel notice check | Coaching |
| QR-462 | 2026-01-21 | DIS-01 | Terminal replacement false positive cleared correctly | Coaching |
| QR-463 | 2026-07-10 | AMT-01 | Terminal replacement false positive cleared correctly | No action |
| QR-464 | 2026-08-20 | GEO-02 | Enrichment missing; analyst cleared large online purchase | Procedure updated |
| QR-465 | 2026-08-16 | DIS-01 | Hold exceeded 48 hours without contact attempt | No action |
| QR-466 | 2026-02-12 | MCC-02 | Hold exceeded 48 hours without contact attempt | Reported to InfoSec |
| QR-467 | 2026-08-13 | ATM-02 | Recurring merchant escalated in error | Commended |
| QR-468 | 2026-06-10 | ATO-03 | Analyst cleared without travel notice check | Commended |
| QR-469 | 2026-06-28 | MCC-01 | Analyst cleared without travel notice check | No action |
| QR-470 | 2026-05-19 | ATM-01 | Card number pasted into case note | Reported to InfoSec |
| QR-471 | 2026-07-22 | DEV-02 | Terminal replacement false positive cleared correctly | No action |
| QR-472 | 2026-08-10 | GEO-01 | Enrichment missing; analyst cleared large online purchase | Procedure updated |
| QR-473 | 2026-05-14 | VEL-03 | Terminal replacement false positive cleared correctly | Coaching |
| QR-474 | 2026-05-27 | VEL-02 | Terminal replacement false positive cleared correctly | No action |
| QR-475 | 2026-05-28 | ENT-04 | Disposition reason copied from prior case | Procedure updated |
| QR-476 | 2026-09-03 | ENT-04 | Correct escalation, exemplary reason | Reported to InfoSec |
| QR-477 | 2026-07-07 | ATO-02 | Recurring merchant escalated in error | Commended |
| QR-478 | 2026-01-22 | DEV-02 | Disposition reason copied from prior case | No action |
| QR-479 | 2026-05-19 | GEO-01 | Contact made to recently changed phone number | Reported to InfoSec |
| QR-480 | 2026-09-03 | ENT-04 | Enrichment missing; analyst cleared large online purchase | Coaching |
| QR-481 | 2026-04-13 | DUP-01 | Correct escalation, exemplary reason | Procedure updated |
| QR-482 | 2026-09-11 | ATM-03 | Correct escalation, exemplary reason | Commended |
| QR-483 | 2026-04-07 | ATO-01 | Card number pasted into case note | Coaching |
| QR-484 | 2026-03-26 | AMT-01 | Enrichment missing; analyst cleared large online purchase | Commended |
| QR-485 | 2026-06-13 | ENT-01 | Hold exceeded 48 hours without contact attempt | No action |
| QR-486 | 2026-01-16 | DEV-01 | Escalation lacked written reason | Procedure updated |
| QR-487 | 2026-08-26 | GEO-03 | Hold exceeded 48 hours without contact attempt | Procedure updated |
| QR-488 | 2026-01-12 | ATO-03 | Correct escalation, exemplary reason | Commended |
| QR-489 | 2026-01-04 | GEO-02 | Card number pasted into case note | Commended |
| QR-490 | 2026-08-19 | DUP-01 | Card number pasted into case note | Procedure updated |
| QR-491 | 2026-05-14 | VEL-01 | Disposition reason copied from prior case | Commended |
| QR-492 | 2026-03-09 | GEO-02 | Enrichment missing; analyst cleared large online purchase | No action |
| QR-493 | 2026-03-13 | GEO-03 | Analyst cleared without travel notice check | Coaching |
| QR-494 | 2026-01-18 | DEV-01 | Disposition reason copied from prior case | Reported to InfoSec |
| QR-495 | 2026-02-28 | MCC-01 | Contact made to recently changed phone number | Coaching |
| QR-496 | 2026-02-09 | AMT-02 | Terminal replacement false positive cleared correctly | No action |
| QR-497 | 2026-02-22 | ENT-01 | Contact made to recently changed phone number | No action |
| QR-498 | 2026-08-28 | VEL-03 | Enrichment missing; analyst cleared large online purchase | No action |
| QR-499 | 2026-04-06 | GEO-02 | Recurring merchant escalated in error | Procedure updated |
| QR-500 | 2026-01-18 | GEO-01 | Analyst cleared without travel notice check | Procedure updated |

## Appendix F. Glossary

**Authorization.** The real-time approval of a transaction by the issuer. An alert is raised on an authorization, before settlement.

**Card-present.** A transaction where the physical card was read by a terminal, by chip, contactless or magnetic stripe.

**Card testing.** Fraudsters making many small authorizations to check whether a stolen card number is live.

**Chip fallback.** A chip card processed by magnetic stripe because the chip read failed or was bypassed. A skimming indicator.

**Enrichment.** Data joined to an alert from account history, device intelligence and contact records.

**Hold.** A temporary block that declines new authorizations until the alert is resolved.

**MRM.** Model Risk Management, the second-line function that validates models and decision aids.

**PAN.** Primary account number; the full card number.

**SAR.** Suspicious activity report, filed by the BSA officer on the recommendation of a senior analyst.

**Soft decline.** A decline the merchant may retry, such as an issuer timeout.

**Tokenization.** Replacing the PAN with a surrogate value that is useless outside the bank's systems.

**Travel notice.** A customer-provided notice of travel dates and countries, used to suppress GEO rules.

**Velocity.** The count or value of transactions within a short window.


## Appendix G. Revision history

| Revision | Date | Change | Approved by |
|---|---|---|---|
| 1 | 2022-09-23 | Initial issue | VP Fraud Operations |
| 2 | 2022-12-21 | Added VEL-03 guidance | VP Fraud Operations |
| 3 | 2023-08-02 | Added section 5 on missing enrichment | VP Fraud Operations |
| 4 | 2023-02-05 | Added MRM requirements to section 2 | VP Fraud Operations |
| 5 | 2023-06-25 | Clarified ATO-02 contact guidance | VP Fraud Operations |
| 6 | 2024-01-07 | Appendix B expanded | VP Fraud Operations |
| 7 | 2024-11-24 | Appendix E added | VP Fraud Operations |
| 8 | 2024-05-19 | Data handling section rewritten after InfoSec review | VP Fraud Operations |
| 9 | 2025-10-15 | Country list updated | VP Fraud Operations |
| 10 | 2025-11-04 | Contact scripts revised | VP Fraud Operations |
| 11 | 2025-08-11 | Service levels adjusted | VP Fraud Operations |
| 12 | 2026-06-09 | Added decision-aid recording rule to section 6 | VP Fraud Operations |
| 13 | 2026-07-04 | Senior analyst withdrawal of decision aid recorded in section 5 | VP Fraud Operations |
| 14 | 2026-06-16 | Annual review, no material change | VP Fraud Operations |
