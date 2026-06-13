import whisper
import json
import os

# Whisper model load karo
print("Model load ho raha hai...")
model = whisper.load_model("base")

audio_folder = "audio"
data_folder = "data"
os.makedirs(data_folder, exist_ok=True)

# Sabhi MP3 files transcribe karo
for audio_file in os.listdir(audio_folder):
    if audio_file.endswith(".mp3"):
        audio_path = os.path.join(audio_folder, audio_file)
        print(f"Transcribing: {audio_file}")
        
        # Whisper se transcribe karo
        result = model.transcribe(audio_path)
        
        # JSON mein save karo
        output = {
            "video": audio_file.replace(".mp3", ""),
            "text": result["text"],
            "segments": result["segments"]
        }
        
        json_file = os.path.join(data_folder, audio_file.replace(".mp3", ".json"))
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
        
        print(f"Done: {json_file}")

print("Sab transcribe ho gaya!")