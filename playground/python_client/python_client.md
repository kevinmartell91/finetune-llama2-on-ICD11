# Python Client

Using Lamini with Python is simple.

To start, obtain `<YOUR-LAMINI-API-KEY>` from [https://app.lamini.ai/account](https://app.lamini.ai/account)

Add the key as an environment variable. Or, authenticate via the Python library below.

```bash
export LAMINI_API_KEY="<YOUR-LAMINI-API-KEY>"
```

Install the Python library.

```python
pip install lamini
```

Run an LLM with a few lines of code.

```python
import lamini

llm_runner = lamini.LlamaV2Runner()
print(llm_runner.call("Summarize this story: once upon a time, there was a ..."))
```

<details>
<summary>Expected Output</summary>

```json
{"question": "Summarize this story: once upon a time, there was a ...", "answer": " Once upon a time, there was a young girl named Alice who lived in a small village. She was known for her kindness and helpfulness, and people often came to her for advice and support. One day, a group of travelers arrived in the village, seeking shelter and food. Alice welcomed them with open arms and offered them a place to stay.\n\nAs the travelers shared their stories, Alice learned that they were on a quest to find a magical flower that could cure a deadly disease. The flower was said to be hidden deep in the forest, and the journey was dangerous. The travelers were hesitant to continue their quest, but they knew that it was their only hope.\n\nAlice, being the kind-hearted person she was, decided to join the travelers on their journey. She packed a bag with supplies and set off into the forest with them. Together, they faced many challenges, including treacherous terrain, wild animals, and harsh weather. But Alice's courage and determination kept them going.\n\nFinally, after many days of searching, they found the magical flower. The travelers were overjoyed, and they thanked Alice for her help. They gave her a small piece of the flower, which she kept safe and gave to the villagers when they returned.\n\nFrom that day on, the village was blessed with good health and prosperity. Alice became a hero, and her kindness and bravery were celebrated for generations to come. And the travelers continued on their journey, knowing that they had made a new friend in Alice, who had helped them in their time of need."}
```

</details>


You can set the key as an environment variable or authenticate directly through the Python library provided below.

```python
lamini.api_key = "<YOUR-LAMINI-API-KEY>"
```

# Docker instruction
Assuming you are in `/playground/python-client` folder directory, execute the following bash file.

```bash
./dockerized_client/answer_sample_questions.sh 
```
This command will handle everything from creating the Python image and Docker container, calling the LLM, prompting two questions -- which can be found in `./sample_questions.jsonl`, and returning the LLM's answers in `/data/sample_answers.jsonl`.
