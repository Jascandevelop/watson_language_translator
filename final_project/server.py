from flask import Flask, render_template, request
import json
import machinetranslation as mt 

app = Flask(__name__)

@app.route("/englishToFrench")
def englishToFrench():
    text_to_translate = request.args.get('textToTranslate')
    french_text = mt.translator.english_to_french(text_to_translate)
    return french_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    text_to_translate = request.args.get('textToTranslate')
    english_text = mt.translator.french_to_english(text_to_translate)
    return english_text

@app.route("/")
def renderIndexPage():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
