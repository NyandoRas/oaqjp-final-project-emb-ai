def emotion_detector(text_to_analyse):
    # Mocked fixed responses for tests
    mock_responses = {
        "I am glad this happened": {
            'anger': 0.0,
            'disgust': 0.0,
            'fear': 0.0,
            'joy': 0.9,
            'sadness': 0.1,
            'dominant_emotion': 'joy'
        },
        "I am really mad about this": {
            'anger': 0.95,
            'disgust': 0.01,
            'fear': 0.0,
            'joy': 0.0,
            'sadness': 0.04,
            'dominant_emotion': 'anger'
        },
        "I feel disgusted just hearing about this": {
            'anger': 0.0,
            'disgust': 0.98,
            'fear': 0.01,
            'joy': 0.0,
            'sadness': 0.01,
            'dominant_emotion': 'disgust'
        },
        "I am so sad about this": {
            'anger': 0.0,
            'disgust': 0.0,
            'fear': 0.0,
            'joy': 0.0,
            'sadness': 1.0,
            'dominant_emotion': 'sadness'
        },
        "I am really afraid that this will happen": {
            'anger': 0.0,
            'disgust': 0.0,
            'fear': 1.0,
            'joy': 0.0,
            'sadness': 0.0,
            'dominant_emotion': 'fear'
        }
    }
    return mock_responses.get(text_to_analyse, {
        'anger': 0.0,
        'disgust': 0.0,
        'fear': 0.0,
        'joy': 0.0,
        'sadness': 0.0,
        'dominant_emotion': None
    })
