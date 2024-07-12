# SharpConnector & LLM

## Overview
This repository contains C# code (`SharpConnector`) for connecting to an API and a Q&A document processor (`LLM`). `LLM` processes questions and answers using an API, focusing on accuracy and efficiency for shorter documents.

### SharpConnector
- C# connector for interacting with the API.

### LLM
- Q&A document processor.
- More accurate with broad questions after fine-tuning and search matching.
- Works faster with shorter documents (recommended file: `test2`).

## How to Run

### LLM
1. Change directory to `LLM`.
2. Install packages and dependencies: pip install -r requirements.txt
3. Set up your Azure OpenAI API key in a `.env` file.
4. Start the API using the following command: uvicorn api:app --reload

### SharpConnector
1. Specify filename (Currently test2.doc)
2. Specify Question
3. From within terminal type: dotnet run (make sure you cd to the right directory)

## General Notes
- Initially designed for shorter documents.
- Achieves higher accuracy for broad context (with specific context we need fine-tuning and search indexing.)
- Token-friendly for efficient processing.

## Testing
- For initial testing, use the `test2.doc` file to evaluate performance.

You can find attached some examples of previous tests using Postman:

The endpoint is the following: http://127.0.0.1:8000

Please make sure after running: uvicorn api:app --reload that you're getting the same url endpoint, otherwhise change it to the right url.

## Sample Testing

In the first request I've asked for a summary from all data fed to the model, and the answer was accurate

![Postman Test]('Capture.png')



## What's next


## License
This project is licensed under the MIT License - see the LICENSE file for details.


