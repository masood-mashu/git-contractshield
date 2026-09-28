"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitContractShield.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.liability_cap_auditor import *
from tools.indemnity_clause_checker import *
from tools.governing_law_verifier import *

class TestGitContractShieldPredictability(unittest.TestCase):

    def test_liability_cap_auditor(self):
        res = audit_liability_cap('{"acv": 100000, "liability_cap": 150000}')
        self.assertTrue(res["compliant"])
        self.assertEqual(res["status"], "APPROVED")

    def test_indemnity_clause_checker(self):
        clause = "Vendor shall indemnify Customer for direct damages, excluding indirect or consequential damages."
        res = check_indemnity_clause(clause)
        self.assertEqual(res["status"], "APPROVED")

    def test_governing_law_verifier(self):
        res = verify_governing_law("State of Delaware")
        self.assertTrue(res["approved"])
        self.assertEqual(res["status"], "JURISDICTION_ACCEPTED")


if __name__ == "__main__":
    unittest.main()
