from moviepy.editor import *


def extract_audio(video_file_path, audio_output_path):
    video_clip = VideoFileClip(video_file_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_output_path)


extract_audio("test_replaced_audio.mp4", "test_cloned.wav")
