import os
import docx

docx_dir = "/path/to/docs/"
docx_files = os.listdir(docx_dir)

for file in docx_files:
    doc_file = docx.Document(docx_dir+file)
    print("需要的段落"+doc_file.paragraphs[20].text)
   