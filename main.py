import whisper
import json
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip
from TTS.api import TTS


def extract_audio(video_file_path, audio_output_path):
    video_clip = VideoFileClip(video_file_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_output_path)


file_name = "test_short"
tts = TTS("tts_models/multilingual/multi-dataset/your_tts")

extract_audio(f'{file_name}.mp4', f'{file_name}.wav')
video = VideoFileClip(f'{file_name}.mp4')
video_duration = video.duration

model = whisper.load_model("base")
result = model.transcribe(f'{file_name}.wav', task="translate")
result["segments"][-1]["end"] = video_duration
with open("result.json", "w") as f:
    json.dump(result, f, indent=2)

tts_list = []
for seg in result["segments"]:
    length_of_speech = seg["end"] - seg["start"]
    content_of_speech = seg["text"]
    seg_tts = tts.tts_to_file(
        text=content_of_speech,
        language="en",
        emotion="Neutral",
        speaker_wav=f'{file_name}.wav',
        file_path=f'tts/{file_name}_{seg["id"]}.wav',
    )
    tts_list.append((seg["start"], seg["end"], f'tts/{file_name}_{seg["id"]}.wav'))


video_clips = [video.subclip(start, end).set_audio(AudioFileClip(tts)) for (start, end, tts) in tts_list]

final_clip = concatenate_videoclips(video_clips)
final_clip.write_videofile(f"{file_name}_output.mp4", audio_codec="aac")
