import unittest
from chains.case_report_chain import create_case_report_chain
from state_management.conversation_state import ConversationState

class TestCaseReportChain(unittest.TestCase):
    def test_chain_creation(self):
        chain = create_case_report_chain()
        self.assertIsNotNone(chain)

    def test_chain_invoke(self):
        chain = create_case_report_chain()
        test_input = {
            "complaint_duration": "Headache for 2 days",
            "key_findings_vitals": "BP: 150/95",
            "relevant_history": "Allergic to penicillin"
        }
        response = chain.invoke(test_input)
        print(response)
        self.assertTrue(isinstance(response, str))
        self.assertIn("## Patient Summary", response)

if __name__ == "__main__":
    unittest.main()
