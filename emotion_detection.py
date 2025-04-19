import requests
import json

def emotion_detector(text_to_analyze):
    # Endpoint URL and headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
     # Input payload
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Make POST request to the EmotionPredict endpoint
    response = requests.post(url, headers=headers, json=input_json)
    print("STATUS CODE:", response.status_code)
    print("FULL RESPONSE:", response.text)  # <-- Print raw response text for debugging


    # If response is successful, return the 'text' field from the response JSON
        try:
            result = response.json()
            return result
         except Exception as e:
             return {"error": f"Could not parse JSON: {str(e)}"}
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=input_json)

    print("STATUS CODE:", response.status_code)
    print("RESPONSE TEXT:", response.text)

    try:
        result = response.json()
        return result
    except Exception as e:
        return {"error": f"Could not parse JSON: {str(e)}"}