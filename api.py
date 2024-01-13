import PyPDF2
import os
import tensorflow

from ml import LLM
from flask import Flask, request

app = Flask(__name__)

# implementing the ML models
llm = LLM("question-answering")

# helper functions
def sendResponse(message, status=400, results=[]):
    return { "message": message, "status": status, "results": results }

documents = []
i = 0

# adding raw test
@app.route("/add-text", methods=["POST"])
def addText():
    global i
    content:str = request.form["text"]
    
    if len(content.split(" ")) < 5:
        return sendResponse(message='This content should be atleast 5 words')

    documents.append(content)
    i += 1
    return sendResponse(message='Text understood successfully!', results=[{"id":i}], status=200)

# upload document, read the pdf file and stack the text content into array
@app.route("/upload", methods=["PUT"])
def uploadDocs():
    global i
    if 'pdf' not in request.files:
        return sendResponse(message='No PDF file uploaded.')

    pdf_file = request.files['pdf']

    if pdf_file.filename == '':
        return sendResponse(message='No selected PDF file.')

    try:
        with pdf_file.stream as f:  # Access the file stream directly
            pdf_reader = PyPDF2.PdfReader(f)
            pdf_content = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_content += page.extract_text()

        pdf_content = pdf_content.replace("\n", " ")
        documents.append(pdf_content)
        i += 1
        return sendResponse(message='PDF understood successfully!', results=[{"id":i}], status=200)
    except Exception as e:
        return sendResponse(message='Error reading PDF: ' + str(e))

# send an id and the question to answer from the stacked text
@app.route("/ask", methods=["POST"])
def askQuestion():
    try :
        index = request.form["id"]
        index = int(index)
        context = documents[index - 1]
        qst = request.form["qst"]
        ans = llm.askQuestion(context=context, question=qst)
        return sendResponse(message="Answer ready", results=[ans], status=200)
    except IndexError:
        return sendResponse(message="No document with this id", status=500)
    except ValueError:
        return sendResponse(message="id must be an integer", status=500)
    except:
        return sendResponse(message="Kindly ensure your payload is correct", status=500)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3000))  # Default to 5000 if not set
    app.run(host='0.0.0.0', port=port)