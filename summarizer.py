from transformers import T5Tokenizer, T5ForConditionalGeneration

# Initialize the T5 model and tokenizer
model_name = "t5-base"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Sample data for summarization
narrative_input = (
    "The overall mood of the interaction was happy with emotions like excited and cheerful expressed. "
    "Gestures included thumbs up and smiling. Key discussions revolved around the success of the project, "
    "teamwork, and future plans. There were three unique speakers."
)

# Prepare input for the model
input_text = f"summarize: {narrative_input}"
input_ids = tokenizer(input_text, return_tensors="pt").input_ids

# Generate summary
summary_ids = model.generate(input_ids, max_length=150, num_beams=4, early_stopping=True)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print("Dynamic Summary:")
print(summary)
