from ollama import chat, ChatResponse
import argparse

def summarize_text(text):
    # Call the Ollama model to summarize the text
    response: ChatResponse = chat(model="gemma3:12b", messages=[
        {"role": "user", "content": f"Summarize the following text: {text}"}
    ])
    return response.get('message').get('content')


def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Process some command line arguments")

    # Add an argument for the name
    parser.add_argument("-i", "--input_file", help="File to be summarized", required=True)

    # Parse the arguments
    args = parser.parse_args()


    # Read the input file
    with open(args.input_file, 'r') as file:
        text = file.read()

    # Summarize the text
    summary = summarize_text(text)

    print("Summary:")
    print(summary)


if __name__ == "__main__":
    main()