from chains.case_report_chain import create_case_report_chain
from state_management.conversation_state import ConversationState
from utils.input_validators import validate_non_empty_string
from utils.logging_utils import logger

TRIGGER_KEYWORDS = ["new case", "start new patient file", "log new patient"]

QUESTIONS = [
    "What is the patient's primary complaint and its duration?",
    "What are the key clinical observations or vital signs you've noted so far?",
    "Please provide relevant patient history (e.g., major conditions, allergies, current medications)."
]

STATE_KEYS = ["complaint_duration", "key_findings_vitals", "relevant_history"]

def main():
    conversation_state = ConversationState()
    print("🩺 Emergency Case Assistant Ready. Type 'New case' to start.")

    while True:
        user_input = input("\nDoctor: ").strip().lower()

        if user_input in TRIGGER_KEYWORDS:
            logger.info("New case initiated by trigger keyword.")
            print("Chatbot: Okay, starting a new case. Let's gather some initial details.")

            # Sequentially ask questions and validate responses
            for question, state_key in zip(QUESTIONS, STATE_KEYS):
                while True:
                    response = input(f"\nChatbot: {question}\nDoctor: ").strip()
                    if validate_non_empty_string(response):
                        conversation_state.set(state_key, response)
                        logger.info(f"Stored response for {state_key}: {response}")
                        break
                    else:
                        print("Chatbot: Invalid input. Please provide a clear response.")

            # Confirm collected details
            print("\nChatbot: Thank you. I have recorded the following details:")
            for key in STATE_KEYS:
                print(f"{key.replace('_', ' ').title()}: {conversation_state.get(key)}")

            print("\nChatbot: Generating preliminary report...")

            # Generate report using the chain
            try:
                case_report_chain = create_case_report_chain()
                report_input = {
                    "complaint_duration": conversation_state.get("complaint_duration"),
                    "key_findings_vitals": conversation_state.get("key_findings_vitals"),
                    "relevant_history": conversation_state.get("relevant_history"),
                }
                report = case_report_chain.invoke(report_input)

                print("\n📝 Preliminary Case Report:")
                print("-" * 50)
                print(report)
                print("-" * 50)
                logger.info("Successfully generated and displayed the report.")

            except Exception as e:
                logger.error(f"Failed to generate report: {e}")
                print("Chatbot: Sorry, there was an error generating the report.")

            # Optionally break or continue for a new case
            next_step = input("\nChatbot: Would you like to start another case? (yes/no)\nDoctor: ").strip().lower()
            if next_step not in ["yes", "y"]:
                print("Chatbot: Closing session. Take care!")
                break

        elif user_input in ["exit", "quit"]:
            print("Chatbot: Session ended. Goodbye!")
            break

        else:
            print("Chatbot: Unrecognized command. Type 'New case' to begin or 'exit' to quit.")

if __name__ == "__main__":
    main()
