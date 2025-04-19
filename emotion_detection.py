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

    if response.status_code == 200:
        result = response.json()
        emotions = result["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(emotions, key=emotions.get)
        return {
            "dominant_emotion": dominant_emotion,
            "score": emotions[dominant_emotion],
            "all_emotions": emotions
        }
    else:
        return {"error": f"Request failed with status code {response.status_code}"}
