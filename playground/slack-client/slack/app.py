from lamini import Lamini  # Import Lamini library

import logging
import json
import re
import requests
import time
from config import config

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


SLACK_BOT_TOKEN = config["SLACK_BOT_TOKEN"]
app = App(token=SLACK_BOT_TOKEN)


logging.basicConfig(filename="/tmp/docker.log", encoding='utf-8', level=logging.DEBUG)  # Configure logging settings

@app.event("app_mention")
def main_event(client, event, say):  # Define main_event function for handling app mentions
    """
    Handle app mentions event

    Args:
        client (obj): The Slack client object
        event (dict): The event data
        say (func): The function to send a message back to Slack
    """
   
    channel_id = event["channel"]  # Get the channel ID from the event
    thread_ts = event.get("thread_ts", None) or event["ts"]  # Get the thread timestamp from the event
    question = re.sub("<[^>]+>", "", event["text"])  # Remove the @mention tag

    print("Mentioned in channel " + channel_id + " with question " + question)  # Print channel ID and question

    try:
        model_names = config["channel_token_mappings"][channel_id][
            "model_names"
        ]  # Get model names from config based on channel ID
    except:
        say(
            "Channel mapping does not exist or is incorrect: check config",
            thread_ts=thread_ts,
        )  # Respond if channel mapping is missing or incorrect
        return

    print("Model names: " + str(model_names))  # Print model names

    for index, model in enumerate(model_names):  # Iterate over model names
        try:
            loading = say("_Typing..._", thread_ts=thread_ts)  # Display typing indicator

            answer = ask_lamini_model_question(channel_id, model, question)  # Get answer from model
            clean_answer = post_process(answer)  # Clean the answer

            if len(model_names) == 1:
                text = clean_answer  # Set text to clean answer if only one model
            else:
                text = f"*Model {index + 1}:*\n" + clean_answer  # Format text with model number

            print(clean_answer)  # Print the clean answer
            reply = client.chat_update(  # Update the chat with the answer
                channel=loading["channel"],
                ts=loading["ts"],
                text=text,
            )
            print("Lamini replied: ",reply) 
            
        except Exception as e:
            print(e)  # Print any exceptions
            continue

def ask_lamini_model_question(channel_id, model, question):  
    """
    Ask a question to the model and retrieve the answer.

    Args:
        channel_id (str): The ID of the channel where the question is asked.
        model (str): The name of the model to use for answering the question.
        question (str): The question to ask the model.

    Returns:
        str: The answer provided by the model.
    """
    token = config["channel_token_mappings"][channel_id]["token"]  

    system_prompt = """\
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information."""  

    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
    }  

    prompt = f"<s>[INST] <<SYS>>\n{system_prompt}\n<</SYS>>\n\n{question} [/INST]"  

    body = {
        "id": "LaminiSDKSlackbot",
        "model_name": model,
        "prompt": prompt,
        "out_type": {
            "Answer": "string",
        }
    }  

    response = requests.post(  
        config["api_endpoint"] + "/v1/completions",
        headers=headers,
        json=body,
    )

    if response.status_code == 200:  
        answer = response.json()["Answer"]  
        return answer  
    else:
        print(response.status_code, response.reason)  
        return f"Sorry I can't answer that: {response.status_code} {response.reason}"  

def post_process(answer):
    """
    Clean the answer by removing leading spaces
    """
    clean_answer = answer.lstrip(' ')  # Remove leading spaces from the answer
    return clean_answer  # Return the cleaned answer

# Start your app
if __name__ == "__main__":  # Check if the script is run directly
    print("til this point is correct kevin!")
    # Get Slack app token
    SLACK_APP_TOKEN = config["SLACK_APP_TOKEN"]  
    # Start the SocketModeHandler with the app and app token
    SocketModeHandler(app, SLACK_APP_TOKEN).start()  

