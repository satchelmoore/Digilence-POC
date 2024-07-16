import streamlit as st

import os

from txtchunking import chunk_text, flatten_chunked_sentences, ensure_nltk_data
from messages_operations import HasInfo, answer
import convertapi
from pathlib import Path

# Ensure NLTK data is downloaded
ensure_nltk_data()

# Set your ConvertAPI secret
convertapi.api_secret = 'UVJ2EbZ5ei63xEdu'

def convert_file(doc_path):
    # Save the uploaded file to a temporary location
    temp_file_path = Path("/tmp") / doc_path.name
    with open(temp_file_path, "wb") as f:
        f.write(doc_path.getbuffer())

    # Convert the file
    result = convertapi.convert('txt', {
            'File': str(temp_file_path)
        }, from_format='doc')

    # Save the converted file to the same directory
    save_path = Path("/tmp") / (temp_file_path.stem + '.txt')
    result.save_files(str(save_path))

    return(save_path)


# Streamlit interface
st.title('DOC to Text Converter and NLTK Processor')

doc_file = st.file_uploader("Choose a DOC file", type=['doc', 'docx'])


if doc_file is not None:
    output_path = convert_file(doc_file)
            
    with open(output_path, "r", encoding="utf-8", errors="ignore") as file:
        text = file.read()
    
    if text:
        # Display the extracted text in a textbox
        st.text_area("Extracted Text", text, height=300)
        
        # Additional textbox for user input
        user_input = st.text_input("Add your question here:")
        
        # Button to process the text
        if st.button("Process Text"):
            try:
                # Grammar Data
                grammar = """
                NP: {<DT>?<JJ>*<NN>}  # Chunk determiners, adjectives, and nouns
                    {<NNP>+}          # Chunk sequences of proper nouns
                """
                
                chunked = chunk_text(text, grammar)
                flattened = flatten_chunked_sentences(chunked)
                relevant_text=''
                for sentence in flattened:
                        hasinfo = HasInfo(user_input, sentence).choices[0].message.content
                        relevant_info=''
                        print(hasinfo)
                        answers=''
                        if 'Yes' in hasinfo or 'yes' in hasinfo:
                            relevant_info=''
                            relevant_info = sentence
                            print(relevant_info)
                            st.write("Relevant information found:", relevant_info)
                            relevant_text+=sentence+' '
                            answers=answers+' '+answer(user_input,sentence).choices[0].message.content
                            print('_______________'+answers)
                            if len(relevant_text)>1000:
                                break
                print(relevant_text)
                st.write("Answers:", answers)
            except Exception as e:
                st.error(f"An error occurred during text processing: {e}")
        
       
    else:
        st.error("Failed to extract text. Please check the document format and try again.")


