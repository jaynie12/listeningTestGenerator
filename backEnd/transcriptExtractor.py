from youtube_transcript_api import YouTubeTranscriptApi

class TranscriptExtractor:
    """A class to extract transcripts from YouTube videos.
    This class uses the YouTubeTranscriptApi to fetch transcripts in French.
    It requires a valid YouTube video URL to initialize.
    Attributes:
        url (str): The YouTube video URL.
    """
    def __init__(self, url=None):
        if url:
            self.url = url
        else:
            raise ValueError("URL must be provided to extract video ID")

    def extract_video_id(self):
        """Extracts the video ID from the YouTube URL.
        Returns:
            str: The video ID extracted from the URL.
        Raises:
            ValueError: If the URL is not a valid YouTube URL.
        """

        if "youtu.be" in self.url:
            return self.url.split("/")[-1]
        elif "youtube.com" in self.url:
            return self.url.split("v=")[-1].split("&")[0] # Handles both short and long YouTube URLs  #example https://www.youtube.com/watch?v=EN9lEZgyymI
        else:
            raise ValueError("Invalid YouTube URL")
    
    def get_transcript(self):
        try:
            video_id = self.extract_video_id()
            fetched_transcript = YouTubeTranscriptApi().fetch(video_id, languages=['fr'])
            raw_data = fetched_transcript.to_raw_data() 
            transcript =" ".join(phrase['text'] for phrase in raw_data)  #list comprehension should be used as we are creating a new list
            return transcript
        except Exception as e:
            print(f"Error fetching transcript for video {video_id}: {e}")
            return None
        
if __name__ == "__main__":
    # Example usage
    video_url = "https://www.youtube.com/watch?v=EN9lEZgyymI"
    get_transcriptor = TranscriptExtractor(video_url).get_transcript()
    if get_transcriptor:
        print(get_transcriptor)
    else:
        print("No transcript available.")

        