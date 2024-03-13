'''Emotion detection module'''
import json
import requests

def emotion_detector(text_to_analyse):
    '''
    Emotion detector

    Parameters:
        text_to_analyse: string

    Return:
        object:
            label: string
            score: int
    '''
    url = '''https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'''
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    emotion = { "raw_document": { "text": text_to_analyse } }
    resp = requests.post(url, headers=headers, json=emotion, timeout=300)
    if resp.status_code == 200:
        res = json.loads(resp.text)['emotionPredictions'][0]['emotion']
        emotions = list(res.keys())
        scores = list(res.values())
        dom_score = max(scores)
        res['dominant_emotion'] = emotions[scores.index(dom_score)]
        return res
    elif resp.status_code == 400:
        return {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion": None
        }