# Step 2 :>> Text Splitting of Transcripts

from langchain_text_splitters import RecursiveCharacterTextSplitter
from indexing.yt_video_transcript_loader import transcript

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.create_documents([transcript])

# print(len(chunks))
# print(chunks[100])