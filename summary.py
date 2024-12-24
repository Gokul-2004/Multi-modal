import pandas as pd
from collections import Counter

def preprocess_data(file_path):
    # Load data from Excel file
    df = pd.read_excel(file_path)

    # Filter out rows with missing or "not detected" data
    valid_frames = df[(df['Dominant Emotion_x'] != 'not detected') & 
                      (df['Gesture Detected'] != 'not detected')]

    # Aggregate data across frames
    unique_people_count = valid_frames['Person ID'].nunique()
    emotions = valid_frames['Dominant Emotion_x'].tolist()
    
    # Convert gestures to strings and filter out invalid entries
    gestures = [str(gesture) for gesture in valid_frames['Gesture Detected'].dropna()]
    transcripts = " ".join(valid_frames['Transcript'].dropna().tolist())

    # Analyze overall trends
    overall_emotion = Counter(emotions).most_common(1)[0][0] if emotions else "neutral"
    gesture_summary = ", ".join(set(gestures)) if gestures else "none detected"
    
    # Return a dictionary with aggregated information
    result = {
        "overall_emotion": overall_emotion,
        "gesture_summary": gesture_summary,
        "transcripts": transcripts,
        "unique_people_count": unique_people_count
    }

    # Print result for debugging
    print("Preprocessed Data Summary:", result)
    return result

if __name__ == "__main__":
    # Set the path to your Excel file
    file_path = "combined_analysis_results.xlsx"  # Adjust if necessary
    data = preprocess_data(file_path)
