import requests
from decouple import config

ELEVEN_LABS_API_KEY = config("ELEVEN_LABS_API_KEY")

# Eleven Labs convert text to speech
def convert_text_to_speech(message):
    # Define data (Body)
    body = {
        "text": message,
        "voice_settings": {
            "stability": 0,
            "similarity_boost": 0,
        }
    }
    # Define voice
    voice_rachel = "21m00Tcm4TlvDq8ikWAM"

    # Contructing Headers and Endpoint
    headers = {"xi-api-key": ELEVEN_LABS_API_KEY, "Conent-Type": "application/json", "accept": "audio/mpeg"}
    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_rachel}"

    # Send Request
    try:
        response = requests.post(endpoint, json=body, headers=headers)
    except Exception as e:
        print(e)
        return
    
    # Handle response
    if response.status_code == 200:
        return response.content
    else:
        return