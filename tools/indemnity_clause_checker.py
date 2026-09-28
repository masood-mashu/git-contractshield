"""
indemnity_clause_checker.py - Audits indemnification language to ensure carveouts and consequential damage exclusions exist
"""
import sys
import json


def check_indemnity_clause(clause_text: str):
    text_lower = clause_text.lower()
    has_ip_carveout = "intellectual property" in text_lower or "infringement" in text_lower
    has_consequential_exclusion = "consequential" in text_lower or "indirect" in text_lower
    is_uncapped = "uncapped" in text_lower or "unlimited" in text_lower or "without limitation" in text_lower
    high_risk = is_uncapped and not has_consequential_exclusion
    return {
        "ip_carveout": has_ip_carveout,
        "consequential_exclusion": has_consequential_exclusion,
        "uncapped_flag": is_uncapped,
        "risk_level": "HIGH" if high_risk else "ACCEPTABLE",
        "status": "REVISE_INDEMNITY" if high_risk else "APPROVED"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "indemnity-clause-checker"}))
