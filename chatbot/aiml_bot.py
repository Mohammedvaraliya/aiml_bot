import os
import aiml


BRAIN_FILE = "brain.dump"
AIML_DIR = "aiml"

class AIMLBot:
    def __init__(self):
        self.kernel = aiml.Kernel()

        if os.path.exists(BRAIN_FILE):
            print("Loading from brain file: " + BRAIN_FILE)
            self.kernel.loadBrain(BRAIN_FILE)
        else:
            print("Parsing AIML files")
            self.kernel.bootstrap(learnFiles=os.path.join(AIML_DIR, r"chatbot\std-startup.aiml"), commands="load aiml b")
            print("Saving brain file: " + BRAIN_FILE)
            self.kernel.saveBrain(BRAIN_FILE)

    def respond(self, input_text):
        response = self.kernel.respond(input_text)
        print("Bot response:", response)
        return response

