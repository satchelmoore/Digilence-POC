
#For API Management
from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.responses import HTMLResponse

#For handling temporary tanscriptions
import tempfile

#For handling Paths in system
import os

#For Interacting with Azure Server
from AzureOp import send_chat_message

#Custom Python Modules
#To convert doc File to text
from file_converter import doc_to_text  # Import doc_to_text function from doc_converter.py
#To chunk Text File
from txtchunking import chunk_text, flatten_chunked_sentences
#To process chatobject variables
from messages_operations import add_message

#Initiate App
app = FastAPI()

#Initiate Route
#Route for Chatting with documents
@app.post("/chat/")
#Take two parameters file and question
async def upload_doc(file: UploadFile = File(...), question: str = Form(None)):
    try:
        # Save the uploaded file locally
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(await file.read())
            tmp.close()
            tmp_path = tmp.name

        # Convert DOC file to text using imported function
        text = doc_to_text(tmp_path)

        # Delete the temporary file
        os.remove(tmp_path)

        if text:
            #Gramamr Data
            grammar = """
    NP: {<DT>?<JJ>*<NN>}  # Chunk determiners, adjectives, and nouns
        {<NNP>+}          # Chunk sequences of proper nouns
""" 
            chunked = chunk_text(text, grammar)
           
            flattened = flatten_chunked_sentences(chunked)
            conversation=[]
            for sentence in flattened[:5]:
                for i in question.split():
                    if i in sentence:
                        conversation=add_message(conversation, "user", sentence)
            # Prepare the response dictionary
            response_data = {"text": conversation}

            # If a question was provided, include it in the response
            if question:
                conversation=add_message(conversation, "user", question)
                azure_data=send_chat_message(conversation).choices[0].message.content
                response_data["question"] = "Based on the information in the document, please provide detailed insights regarding "+question+" Ensure that the response stays strictly within the context of the document, focusing on accurate details and avoiding any unrelated information."

                if azure_data:
                    response_data["answer"] = azure_data
            return response_data
        else:
            raise HTTPException(status_code=500, detail="Failed to convert DOC file to text.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
#uvicorn api:app --reload command to start 
