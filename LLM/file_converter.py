import win32com.client
import os

def doc_to_text(doc_path):
    # Ensure the path is absolute
    doc_path = os.path.abspath(doc_path)

    try:
        # Initialize the Word application
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False

        # Open the DOC file
        doc = word.Documents.Open(doc_path)

        # Extract text from the DOC file
        text = doc.Range().Text

        # Close the DOC file
        doc.Close()

        # Quit the Word application
        word.Quit()

        return text
    except Exception as e:
        print(f"An error occurred: {e}")
        if 'word' in locals():
            word.Quit()
        return None

