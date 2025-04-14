from ollama import chat, ChatResponse
import argparse

# Other things to consider:
# - Add error handling
# - Keep track of messsage history for the LLM's context
# - Other sources of data besides text files / user input
# - Vector databases for text embeddings, RAG, etc
# - Use more robust libraries like LangChain
# - Optimize for your hardware
# - Integrate with your apps to do useful things!

def answer_question(text):
    # Call the Ollama model to summarize the text
    response: ChatResponse = chat(model="llama3.2:latest", messages=[
        {"role": "system", "content": "You are a helpful assistant."},  # System prompt
        {"role": "user", "content": f"{text}"}    # User prompt
    ])
    return response.get('message').get('content')


def main():
    text = input("Please ask a question: ").strip()
    while text != "exit":
        
        # Answer the question
        answer = answer_question(text)

        print("Answer:")
        print(answer)

        text = input("Please ask a question: ").strip()


if __name__ == "__main__":
    main()