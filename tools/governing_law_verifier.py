"""
governing_law_verifier.py - Verifies that the chosen governing law jurisdiction is within the pre-approved corporate registry
"""
import sys
import json


def verify_governing_law(jurisdiction: str):
    APPROVED = ["delaware", "new york", "california", "england & wales", "united kingdom"]
    norm = jurisdiction.strip().lower()
    is_approved = any(a in norm for a in APPROVED)
    return {
        "jurisdiction": jurisdiction,
        "approved": is_approved,
        "status": "JURISDICTION_ACCEPTED" if is_approved else "NON_STANDARD_JURISDICTION"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "governing-law-verifier"}))
