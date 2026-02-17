# Step 1 :>> Youtube Video Transcript Loader 


from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound


video_id = "Gfr50f6ZBvo"  # only the ID, not full URL

try:
    # If you don't care which language, this return "best" one
    ytt_api = YouTubeTranscriptApi()    # create instance 
    transcript_list = ytt_api.fetch(video_id, languages=["en"])

    # Flatten it to plain text
    transcript = " ".join(chunk.text for chunk in transcript_list)
    # print(transcript)

except TranscriptsDisabled:
    print("Transcripts are disabled for this video.")

except NoTranscriptFound:
    print("No transcript found for this video.")