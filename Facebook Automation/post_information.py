# This file is for getting the text that should be posted

import pyperclip
import docx

class Post_Information:
    def __init__(self):
        pass

    def copy_text(self):
        doc = docx.Document("Post info file .docx")
        file_contents = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        contents = pyperclip.copy(file_contents)
        return contents

test = Post_Information()
test.copy_text()

