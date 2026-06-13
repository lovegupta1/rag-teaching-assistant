import json
import os
import pandas as pd

data_folder = "data"
chunk_size = 5  # Kitne segments ek chunk mein

all_chunks = []

for json_file in os.listdir(data_folder):
    if json_file.endswith(".json"):
        json_path = os.path.join(data_folder, json_file)
        
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        segments = data["segments"]
        video_name = data["video"]
        
        # Segments ko chunks mein todo
        for i in range(0, len(segments), chunk_size):
            chunk_segments = segments[i:i+chunk_size]
            
            chunk_text = " ".join([s["text"] for s in chunk_segments])
            start_time = chunk_segments[0]["start"]
            end_time = chunk_segments[-1]["end"]
            
            all_chunks.append({
                "video": video_name,
                "chunk_id": len(all_chunks),
                "text": chunk_text,
                "start_time": start_time,
                "end_time": end_time
            })

# Pandas DataFrame mein save karo
df = pd.DataFrame(all_chunks)
df.to_csv("data/chunks.csv", index=False)

print(f"Total chunks bane: {len(all_chunks)}")
print(df.head())