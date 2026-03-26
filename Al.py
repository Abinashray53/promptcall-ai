import random

class TelecallingBot:

    def __init__(self):
        self.name = None
        self.is_qualified = False

    # Utility function to clean user input
    def get_input(self, message):
        return input(message).strip().lower()

    def start_call(self):
        self.introduce()
        self.capture_name()
        self.offer_pitch()

    def introduce(self):
        intro_lines = [
            "Hello! This is a quick call regarding a learning opportunity.",
            "Hi! Hope you're doing great today.",
            "Good day! I’d like to share something useful with you."
        ]
        print(random.choice(intro_lines))

    def capture_name(self):
        self.name = input("May I know your name? ").strip()
        print(f"Nice speaking with you, {self.name}.")

    def offer_pitch(self):
        print("\nWe provide a program focused on AI and career-ready tech skills.")
        choice = self.get_input("Would you like a quick overview? (yes/no): ")

        if choice == "yes":
            self.describe_program()
        else:
            self.manage_objection(choice)

    def describe_program(self):
        print("\nThe program includes live projects, mentorship, and job preparation support.")
        interest = self.get_input("Does this interest you? (yes/no): ")

        if interest == "yes":
            self.check_intent()
        else:
            self.manage_objection(interest)

    def check_intent(self):
        print("\nJust a quick check.")
        intent = self.get_input("Are you planning to improve skills for a job or switch? (yes/no): ")

        if intent == "yes":
            self.is_qualified = True
            print("\nGreat! You match our ideal learner profile. Our team will reach out soon.")
        else:
            print("\nNo problem! We can still share helpful resources with you.")

    def manage_objection(self, user_input):
        responses = {
            "no": "That's completely fine. Many people feel unsure at first.",
            "busy": "I understand you're busy. We can schedule a better time.",
            "not interested": "Got it. May I know what specifically didn’t interest you?"
        }

        print("\n" + responses.get(user_input, "I understand. Let me briefly clarify."))

        retry = self.get_input("Should I explain briefly? (yes/no): ")

        if retry == "yes":
            self.describe_program()
        else:
            self.end_call()

    def end_call(self):
        print("\nThank you for your time. Have a wonderful day!")



# Entry point
if __name__ == "__main__":
    bot = TelecallingBot()
    bot.start_call()
    