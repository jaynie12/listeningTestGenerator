from openai import OpenAI
from environmentVariables import ENVIRONMENT_VARIABLES
import os
os.environ["OPENAI_API_KEY"] = ENVIRONMENT_VARIABLES["OPENAI_API_KEY"]


client = OpenAI()
# Initialize OpenAI client with your API key
class questionsGenerator:
    def __init__(self, transcript, role, input_str):
        self.transcript = transcript
        self.input_str = input_str
        self.role = role
        self.client = client
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OpenAI API key is not set in environment variables.")
        
    def generateListeningTest(self):
        """Generates a listening comprehension test based on the provided transcript.
        Returns:
            str: The generated listening comprehension questions.
        """
        try:
            completion = self.client.chat.completions.create (
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": 'system', #role of system defines the behavior of the AI
                        "content": self.role,
                    },
                    {
                        "role": 'user', #role of user defines the input to the AI
                        "content": self.input_str,
                    }
                ],
            )
            return completion.choices[0].message.content
        except Exception as e:
            print(f"Error generating listening test: {e}")
            return None


if __name__ == "__main__":
    # Example usage
    transcript = "Bonjour, je m'appelle Pierre."
    role = "You are a French teacher. Your task is to create listening comprehension questions based on the provided transcript."
    input_str = "Create a listening comprehension test based on the following transcript: " + transcript    
    generator = questionsGenerator(transcript, role, input_str)
    questions = generator.generateListeningTest()
    print(questions)  # Output the generated questions