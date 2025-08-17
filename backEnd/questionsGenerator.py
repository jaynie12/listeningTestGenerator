from openai import OpenAI
from environmentVariables import ENVIRONMENT_VARIABLES
import os
os.environ["OPENAI_API_KEY"] = ENVIRONMENT_VARIABLES["OPENAI_API_KEY"]
from transcriptExtractor import TranscriptExtractor


client = OpenAI()
# Initialize OpenAI client with your API key
class questionsGenerator:
    def __init__(self, url):
        self.transcript = TranscriptExtractor(url).get_transcript()
        self.client = client
        self.role = (
        f"You are a French teacher. Your task is to create listening comprehension questions based on the provided transcript: {self.transcript}. "
        "The order of questions should follow the order of the video. Based on the transcript, evaluate the DELF/DALF level. "
        "Give half the test as multiple choice and half as short written answers."
    )
        self.input_str = "Create a listening comprehension test based on the following transcript: " + self.transcript    

        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OpenAI API key is not set in environment variables.")
        
    def generateListeningTest(self):
        """Generates a listening comprehension test based on the provided transcript.
        Returns:
            str: The generated listening comprehension questions.
        """
        try:
            completion = self.client.chat.completions.create (
                model="gpt-5-nano",
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
    url = "https://www.youtube.com/watch?v=EN9lEZgyymI"
    generator = questionsGenerator(url)
    questions = generator.generateListeningTest()
    print(questions)  # Output the generated questions