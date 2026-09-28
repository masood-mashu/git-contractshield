# GitContractShield Explainability Specification

This document provides a transparent, verifiable architectural breakdown of how **GitContractShield** operates, processes input, makes decisions, and enforces security boundaries.

---

## 1. Input Data and Data Sources Used

GitContractShield consumes enterprise master services agreements (MSAs), statements of work (SOWs), vendor commercial schedules, and standard corporate negotiation playbooks. These data sources include annual contract values, indemnification clauses, limitation of liability thresholds, and choice of law provisions. The agent ingests these inputs in raw markdown, text, and JSON metadata format and parses them into structured contract clause models for downstream legal risk analysis. Approved jurisdictional registries and pre-authorized redline templates are also monitored as sensitive data sources to ensure legal governance rules are strictly maintained.

---

## 2. How It Decides and Reasoning Process

The decision making process follows a deterministic, five-stage analytical pipeline designed to eliminate ambiguity and hallucination. When an agreement draft is received, the agent first evaluates limitation of liability terms using the liability-cap-auditor tool to verify that the proposed cap does not exceed approved multiples of annual contract value. Next, the reasoning engine invokes the indemnity-clause-checker tool to audit indemnification language for uncapped consequential damage exposures. Furthermore, the choice-of-law provision is screened using the governing-law-verifier tool against approved forum jurisdictions. Finally, the agent correlates all findings against predefined corporate risk thresholds to issue a conclusive verdict of APPROVED, BLOCKED, or NEEDS_REVIEW alongside an automated redline patch.

---

## 3. Constraints, Limitations, and Known Issues

GitContractShield operates under strict operational constraints to prevent false positives and non-deterministic behavior across different agent frameworks. GitContractShield operates under strict operational constraints to prevent legal misinterpretations and non-compliant risk exposures across execution frameworks. The agent is deliberately limited to contract clause parsing and risk scoring and cannot provide formal legal advice or execute legally binding signatures autonomously. Another known issue and limitation is that novel hybrid bespoke warranties without clear statutory precedents may require secondary human review rather than autonomous blocking. Furthermore, the agent enforces a low temperature constraint of 0.1 to maintain strict predictability across all supported export frameworks.
