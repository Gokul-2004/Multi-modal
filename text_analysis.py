# text_analysis.py

from youtube_transcript_api import YouTubeTranscriptApi
import pandas as pd

def get_transcript(video_id, languages=['en']):
    """Fetch the transcript for the given YouTube video ID."""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
        return transcript
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None

def combine_transcript_with_frames(transcript, frame_duration=5):
    """Combine the transcript with frames based on 5-second intervals."""
    results = []
    
    # Calculate the total duration based on the last transcript entry
    total_duration = transcript[-1]['start'] + transcript[-1]['duration']
    total_frames = int(total_duration // frame_duration) + 1  # Total frames calculated
    
    # Iterate through each segment of the transcript
    for frame_number in range(1, total_frames + 1):
        frame_start = (frame_number - 1) * frame_duration
        frame_end = frame_start + frame_duration
        
        # Collect transcript entries that fall within this frame
        frame_entries = []
        for entry in transcript:
            start_time = entry['start']
            end_time = start_time + entry['duration']
            
            # Check if the entry overlaps with the current frame
            if start_time < frame_end and end_time > frame_start:
                frame_entries.append({
                    "Start Time": start_time,
                    "End Time": end_time,
                    "Transcript": entry['text']
                })

        # Create a result entry for the frame
        results.append({
            "Frame Number": frame_number,
            "Frame Start": frame_start,
            "Frame End": frame_end,
            "Entries": frame_entries
        })

    return results

if __name__ == "__main__":
    # Example usage
    video_id = 'k7SZQCWt6pg'  # Replace with actual video ID
    transcript = get_transcript(video_id)

    if transcript:
        combined_results = combine_transcript_with_frames(transcript)

        # Create a DataFrame from the combined results
        frame_data = []
        for frame in combined_results:
            for entry in frame['Entries']:
                frame_data.append({
                    "Frame Number": frame['Frame Number'],
                    "Frame Start": frame['Frame Start'],
                    "Frame End": frame['Frame End'],
                    "Start Time": entry['Start Time'],
                    "End Time": entry['End Time'],
                    "Transcript": entry['Transcript']
                })

        df = pd.DataFrame(frame_data)

        # Save to an Excel file
        output_file = 'transcript_output.xlsx'
        df.to_excel(output_file, index=False)

        print(f"Transcript saved to {output_file}")
    else:
        print("No transcript available.")
