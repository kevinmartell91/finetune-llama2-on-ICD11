import os

config = {
    "api_endpoint": os.getenv('LAMINI_LLM_API_ENDPOINT'),
    "SLACK_BOT_TOKEN": os.getenv('SLACK_BOT_TOKEN'),
    "SLACK_APP_TOKEN": os.getenv('SLACK_APP_TOKEN'),
    "channel_token_mappings": {
        "C06P4TA7S8Z": {
            "_channel_name": "#" + os.getenv('SLACK_CHANNEL_NAME'),
            "token": os.getenv('LAMINI_API_KEY'),
            "model_names": [os.getenv('SLACK_MODEL_NAMES')]
        }
    }
}