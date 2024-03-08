# Import the required module for text
# to speech conversion
from gtts import gTTS
from pypdf import PdfReader


# creating a pdf reader object
reader = PdfReader('Coffee+Machine+Program+Requirements.pdf')

# creating a page object
page = reader.pages[0]

# extracting text from page
pdf_text = page.extract_text()
print(pdf_text)


# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
text_to_speech = gTTS(text=pdf_text, lang=language, slow=False)

# Saving the converted audio in a mp3 file
text_to_speech.save("text_to_speech.mp3")
