# BerkeleyAIHackathon
https://ai.calhacks.io/
https://devpost.com/software/youcanspeakalllangs/

## Inspiration
There are content creators, lecturer, educators in non-English speaking countries who makes great videos.
What if they want to reach more audience?
Some use English CC, but not everyone likes to read CC.
Some even remake videos in English, which costs too much.

Now with this service, they can generate localized video with their own voice and lip movements to bring the audience a smooth enjoying experience.


## What it does
1. Accurate translation
2. Dubbed with YouTuber's own voice, not a random AI voice
3. Lip sync to make it looks natural

## How we built it
For the model:
1. Speech to text and translation: OpenAI Whisper + OpenAI ChatGPT
2. Voice clone: CoquiAI
3. Lip Syncing: Wav2lip

For the API service:
1. API provided with FastAPI
2. API and model services are virtualized with Docker
3. Deployed on Lambda GPU servers.

## Challenges we ran into
1. Customizing models and open source project for this specific use.
2. Virtualize the service with Docker. So many environmental issues.

## Accomplishments that we're proud of
The video outcome just already looks good without any fine-tuning.

## What's next for RecordOnce,WatchEverywhere
1. It's just a MVP, need fine-tuning
2. Make an UI, then market it to mass users
3. Explore possible uses for education or entertainment: Movies, conference recordings, lectures...
