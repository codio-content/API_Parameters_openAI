##
Getting started with setting up our environment again:

1. Now we need to retrieve our api keys:
    ```https://beta.openai.com/account/api-keys```
2. In the secret.py tab 
3. Set `openai.api_key` equal to the api key we found in the OpenAI site
4. The api key we have entered in the previous should be put in as a string 
5. You can close out the secret tab or simply click on the temp.py on the next tab
6. Now we are going to create a `prompt` variable which we will use to store the prompt we are going to work on
```python
prompts ="Write a tagline for an ice cream shop"
```
```
response = openai.Completion.create(model="text-davinci-002", prompt=prompts, temperature=0, max_tokens=6)
print(response['choices'][0]['text'].strip())
```

{Try it!}(python3 temp.py)