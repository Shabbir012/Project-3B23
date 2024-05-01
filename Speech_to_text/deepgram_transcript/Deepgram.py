import asyncio
import os
from dotenv import load_dotenv
from deepgram import Deepgram
import feedparser


load_dotenv()
DEEPGRAM_API_KEY = os.getenv('DEEPGRAM_API_KEY')

dataset_audio=["C:/Users/samik/OneDrive/Desktop/deepgram_transcript/Podcasts/AI in the Metaverse  Utopia or Dystopia.. with Louis Rosenberg.mp3","C:/Users/samik/OneDrive/Desktop/deepgram_transcript/Podcasts/Developments, Investments & Experiences in the Metaverse.mp3","C:/Users/samik/OneDrive/Desktop/deepgram_transcript/Podcasts/How the Metaverse will revolutionize everything with Matthew Ball.mp3","C:/Users/samik/OneDrive/Desktop/deepgram_transcript/Podcasts/Metaverse - beyond the buzzword.mp3","C:/Users/samik/OneDrive/Desktop/deepgram_transcript/Podcasts/The Metaverse ETF Boom is No Virtual Reality.mp3","C:/Users/samik/OneDrive/Desktop/deepgram_transcript/Podcasts/The Metaverse ETF Boom With Mario Stefanidis.mp3","C:/Users/samik/OneDrive/Desktop/deepgram_transcript/Podcasts/The Outlook for the Metaverse in 2022.mp3","C:/Users/samik/OneDrive/Desktop/deepgram_transcript/Podcasts/Welcome to 2022 in the Metaverse.mp3"]
dataset_txt=["C:/Users/samik/OneDrive/Desktop/deepgram_transcript/Podcasts/AI in the Metaverse  Utopia or Dystopia.. with Louis Rosenberg.txt","C:/Users/samik/OneDrive/Desktop/deepgram_transcript/Podcasts/Developments, Investments & Experiences in the Metaverse.txt","C:/Users/samik/OneDrive/Desktop/deepgram_transcript/Podcasts/How the Metaverse will revolutionize everything with Matthew Ball.txt","C:/Users/samik/OneDrive/Desktop/deepgram_transcript/Podcasts/Metaverse - beyond the buzzword.txt","C:/Users/samik/OneDrive/Desktop/deepgram_transcript/Podcasts/The Metaverse ETF Boom is No Virtual Reality.txt","C:/Users/samik/OneDrive/Desktop/deepgram_transcript/Podcasts/The Metaverse ETF Boom With Mario Stefanidis.txt","C:/Users/samik/OneDrive/Desktop/deepgram_transcript/Podcasts/The Outlook for the Metaverse in 2022.txt","C:/Users/samik/OneDrive/Desktop/deepgram_transcript/Podcasts/Welcome to 2022 in the Metaverse.txt"]
for dataset,datasettxt in zip(dataset_audio,dataset_txt):
    print(dataset)
    async def main():
        deepgram = Deepgram(DEEPGRAM_API_KEY)
        with open(dataset,'rb') as audio:
            source = {'buffer': audio, 'mimetype': 'audio/mp3'}
            transcription_options = {'punctuate': True, 'diarize': True, 'paragraphs': True}
            response = await deepgram.transcription.prerecorded(source, transcription_options)
            transcript = response['results']['channels'][0]['alternatives'][0]['paragraphs']['transcript']
            with open(datasettxt, 'w') as f:
                f.write(transcript)


    if __name__ == '__main__':
        asyncio.run(main())


