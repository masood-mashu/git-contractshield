# Segregation of Duties (SOD) Policy: GitContractShield

This document establishes the role boundaries and segregation of duties for the GitContractShield agent.

## Role Separation

### 1. Maker
The Maker role is responsible for authoring proposed contract redlines, structuring commercial term sheets, and generating automated negotiation diffs.
This role cannot approve or merge its own changes into protected legal branches.

### 2. Checker
The Checker role is responsible for reviewing, auditing, and validating incoming legal agreements, indemnity clauses, and liability caps.
This role operates as an impartial auditor to verify compliance with enterprise risk benchmarks.

### 3. Approver
The Approver role is strictly reserved for human General Counsel and authorized corporate signatories.
Human approval is required for all final contract executions and commercial liability overrides.
