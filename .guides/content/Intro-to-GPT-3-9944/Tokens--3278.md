##

Copy and paste the following lines of codes into our editor on the left: 

```python
prompts ="Write a tagline for an ice cream shop"

response = openai.Completion.create(model="text-davinci-002", prompt=prompts, 
                                    temperature=0, 
                                    max_tokens=6)
print(response)
```

{Try it!}(python3 tokens.py 1)

You will notice, we switch out our print statement. It will make seeing the token variable easier. When we run the code we get the following as part of response being printed.

```python-hide-clipboard
"completion_tokens": 6,
"prompt_tokens": 9,
"total_tokens": 15
```
In order to just have the tokens being printed, we can switch our print statement to the following.

```python 
print(response['usage'])
```
{Try it!}(python3 tokens.py 2)

Before we tackle what each of the answers involving tokens means, let’s start with what the tokens are. 

## Definition: Token
The GPT family of models process text using ***tokens***. Tokens are numerical representation of words or characters.
- The process of tokenization involves dividing plain text, such as a phrase, sentence, paragraph, or entire documents into smaller chunks of data so that it is easier to analyze.
- These smaller chunks of data are referred to as *tokens*, which may include words, phrases, or sentences.

|||
Here are some helpful rules of thumb for understanding tokens in terms of lengths:
<b>1 token ~= 4 chars in English</b>
<b>1 token ~= ¾ words</b>
<b>100 tokens ~= 75 words</b>
Or 
<b>1-2 sentence ~= 30 tokens</b>
<b>1 paragraph ~= 100 tokens</b>
<b>1,500 words ~= 2048 tokens</b>
|||

One can tokenize in two ways:

* **Tokenizing by word** - The benefit of using tokenization by word is that we can pinpoint words that are frequently used. If we were analyzing a group of restaurant ads in NY, and found that the word "vegan" was used often, then we might assume that there are plenty of vegan options at these restaurants.

* **Tokenizing by sentence** - When tokenizing by sentence, we have the ability to analyze how the words in the sentence correlate with each other, which allows us to better understand the context of the words. If we were analyzing a group of restaurant ads in NY, and found that the sentence "No vegan options." was used, then we can determine that there are not plenty of vegan options at these restaurants.

Lastly, OpenAI imposes a $2048$ token limit in order to maintain latency. OpenAI works in a "pay as you go " model. Tokens are one of the units used to determine pricing for an API call.



{Check It!|assessment}(multiple-choice-2018210942)
