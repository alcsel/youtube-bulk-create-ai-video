import moviepy.editor as mp
import whisper
import os
def auto_caption_video(video_path, output_path):
    video = mp.VideoFileClip(video_path)
    audio_path = "temp_audio.wav"
    video.audio.write_audiofile(audio_path)
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    srt_path = "output_captions.srt"
    with open(srt_path, "w", encoding="utf-8") as srt_file:
        for i, segment in enumerate(result["segments"]):
            start = segment["start"]
            end = segment["end"]
            text = segment["text"]

            srt_file.write(f"{i+1}\n")
            srt_file.write(f"{format_time(start)} --> {format_time(end)}\n")
            srt_file.write(f"{text.strip()}\n\n")

    os.system(f"ffmpeg -i \"{video_path}\" -vf subtitles={srt_path} \"{output_path}\"")

    os.remove(audio_path)
    print(f"created successfully: {output_path}")

def format_time(seconds):
    millis = int((seconds - int(seconds)) * 1000)
    seconds = int(seconds)
    mins = seconds // 60
    hours = mins // 60
    mins = mins % 60
    secs = seconds % 60
    return f"{hours:02}:{mins:02}:{secs:02},{millis:03}"

video_path = input("exact way of the video you wanted captions: ").strip()
output_path = input("exact way of the video who is gonna saved: ").strip()
auto_caption_video(video_path, output_path)
