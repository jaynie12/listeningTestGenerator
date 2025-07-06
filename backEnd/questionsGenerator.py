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
        try:
            completion = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": self.role,
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
    prompt = """
    You are a French teacher.
    Based on the transcript of a spoken French video, write 5 to 10 listening comprehension questions.

    Transcript:
    \"\"\"
    {transcript}
    \"\"\"
    """
    role = "system"
    input_str = prompt.format(transcript=transcript)
    
    generator = questionsGenerator(transcript, role, input_str)
    questions = generator.generateListeningTest()
    print(questions)  # Output the generated questions