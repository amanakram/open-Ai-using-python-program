import json
import openai
import concurrent.futures

# Set your OpenAI API key
openai.api_key = "your API Key " #it should be unique in number

# Function to make a request to OpenAI model (gpt-3.5-turbo-instruct) to generate text based on a given prompt.
def promptText_completion(question):
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",  # You can change the model if needed
            prompt=question,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"


# Function to process each question
def process_promptTexts(question_dict):
    question = question_dict["question"]
    print(f"Processing prompts: {question}")
    answer = promptText_completion(question)
    return {"question": question, "answer": answer}


def main():
    # Read the questions from the JSON file
    #The with statement ensures that the file is properly closed after reading.
    with open('promptTests.json', 'r') as file:
        promptTexts = json.load(file)

    # Create a ThreadPoolExecutor it is instance to manage a pool of threads
    # The with statement ensures that the executor is properly shut down after processing.
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Use map to process questions concurrently
        results = list(executor.map(process_promptTexts, promptTexts))

    # Print or save the results
    for result in results:
        print(f"Question: {result['question']}\nAnswer: {result['answer']}\n")


if __name__ == "__main__":
    main()