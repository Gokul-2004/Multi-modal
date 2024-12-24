import openai

class ChatGPTWrapper:
    def __init__(self, api_key):
        openai.api_key = api_key

    def correct_text(self, text):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Correct the grammar and improve the clarity of the following text: {text}"}
            ]
        )
        return response['choices'][0]['message']['content']

    def generate_summary(self, text):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Provide a meaningful summary of the following text: {text}"}
            ]
        )
        return response['choices'][0]['message']['content']


def main(excel_file, api_key):
    # Initialize ChatGPT wrapper
    chat_gpt = ChatGPTWrapper(api_key)

    # Read and combine text from Excel file
    combined_text = read_excel(excel_file)
    print("Combined Text:")
    print(combined_text)  # Print the combined text for verification

    # Correct the text
    corrected_text = chat_gpt.correct_text(combined_text)
    print("Corrected Text:")
    print(corrected_text)  # Print the corrected text for verification

    # Generate summary
    summary = chat_gpt.generate_summary(corrected_text)
    print("Summary:")
    print(summary)  # Print the generated summary

