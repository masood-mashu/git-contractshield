"""
liability_cap_auditor.py - Validates proposed limitation of liability caps against annual contract value (ACV) thresholds
"""
import sys
import json


def audit_liability_cap(cap_data_json: str):
    import json
    data = json.loads(cap_data_json) if isinstance(cap_data_json, str) else cap_data_json
    acv = data.get("acv", 100000.0)
    cap = data.get("liability_cap", 200000.0)
    ratio = cap / max(acv, 1.0)
    compliant = ratio <= 2.0
    return {
        "acv": acv,
        "liability_cap": cap,
        "multiple": round(ratio, 2),
        "compliant": compliant,
        "status": "APPROVED" if compliant else "EXCESSIVE_LIABILITY_CAP"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "liability-cap-auditor"}))
