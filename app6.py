
import google.generativeai as genai

genai.configure(api_key = "AIzaSyB2gInwZdSlyqBOe_FMmUCFH6v2dm9XC1w")

for m in genai.list_models():
    print(m.name)
