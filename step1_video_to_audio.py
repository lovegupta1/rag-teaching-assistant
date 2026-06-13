import moviepy.editor as mp
import os

# Video folder
video_folder = "videos"
audio_folder = "audio"

# Audio folder create karo agar nahi hai
os.makedirs(audio_folder, exist_ok=True)

# Sabhi videos ko MP3 mein convert karo
for video_file in os.listdir(video_folder):
    if video_file.endswith(".mp4"):
        video_path = os.path.join(video_folder, video_file)
        audio_path = os.path.join(audio_folder, video_file.replace(".mp4", ".mp3"))
        
        print(f"Converting: {video_file}")
        video = mp.VideoFileClip(video_path)
        video.audio.write_audiofile(audio_path)
        video.close()
        print(f"Done: {audio_path}")

print("Sab videos convert ho gayi!")