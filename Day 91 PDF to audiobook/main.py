import requests

from PyPDF2 import PdfReader

reader = PdfReader("Some_text.pdf")
page = reader.pages[0]

parts = []


def visitor_body(text, cm, tm, fontDict, fontSize):
    parts.append(text)


page.extract_text(visitor_text=visitor_body)
text_body = "".join(parts)

print(text_body)

url = "https://realistic-text-to-speech.p.rapidapi.com/v3/generate_voice_over_v2"

payload = {
	"voice_obj": {
		"id": 2014,
		"voice_id": "en-US-Neural2-A",
		"gender": "Male",
		"language_code": "en-US",
		"language_name": "US English",
		"voice_name": "John",
		"sample_text": "Hello, hope you are having a great time making your video.",
		"sample_audio_url": "https://s3.ap-south-1.amazonaws.com/invideo-uploads-ap-south-1/speechen-US-Neural2-A16831901130600.mp3",
		"status": 2,
		"rank": 0,
		"type": "google_tts",
		"isPlaying": False
	},
	"json_data": [
		{
			"block_index": 0,
			"text": text_body
		}
	]
}
headers = {
	"x-rapidapi-key": "ba0c684473msh0294f0edc66fa16p1b8ad8jsn9ac9a1b0d83c",
	"x-rapidapi-host": "realistic-text-to-speech.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())




