import os
import openai

# Set the OpenAI API key
os.environ['OPENAI_API_KEY'] = 'your-api-key-here'

# Upload the training file
file_id = openai.File.create(
    file=open("train.jsonl", "rb"),
    purpose='fine-tune'
).id

# Create a fine-tuning job
fine_tune_job = openai.FineTune.create(
    training_file=file_id,
    model="gpt-3.5-turbo"
)

# Monitor fine-tuning job status
status = openai.FineTune.retrieve(id=fine_tune_job['id'])
print("Fine-tuning status:", status['status'])

# Once fine-tuning is complete, use the fine-tuned model
response = openai.Completion.create(
    model="ft:gpt-3.5-turbo-0613:personal::your-model-id",
    prompt="What is a loss function?",
    max_tokens=50
)
print(response.choices[0].text)
