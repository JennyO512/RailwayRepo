from flask import Flask, jsonify, render_template, request
import os
import openai
import docx
from docx import Document
from docx2pdf import convert

app = Flask(__name__)

# This route gets the base page, its' like the 1st page that shows up 
@app.route('/', methods=['GET'])
def home():
    return render_template('base2.html')


#@app.route('/')
#def index():
 #   return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/create-cover-letter', methods=['POST'])
def create_cover_letter():
    # Get the position from the user input
    position = request.form.get('position')
    
    # Get the OpenAI API credentials
    
    openai.api_key = "YOUR API KEY"
    
    # Generate the cover letter using the OpenAI API
    prompt = f"Create a cover letter for {position} position"
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    letter = completions.choices[0].text
    
    # Create a new word document
    doc = docx.Document()
    
    # Add the cover letter text to the document
    doc.add_paragraph(letter)
    
    # Save the document
    doc.save("Cover_Letter.docx")
    
    
    # Return the cover letter to the textarea in the base2.html template
    return render_template('base2.html', letter=letter, position=position)

    
 
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
