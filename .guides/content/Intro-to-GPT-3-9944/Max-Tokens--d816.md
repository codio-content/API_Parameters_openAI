----

GPT-3 takes the prompt, converts the input into a list of tokens, processes the prompt, and converts the predicted tokens back to the words we see in the response.

## Token Limits
Keep track of the following when using the API:

* **Completions** - depending on the engine used, requests can use up to $4000$ tokens shared between prompt and completion.

* **For specialized endpoints** - Answers, Search, and Classifications - the query and longest document must be below $2000$ tokens together.

Enter the following code into the IDE:

```python
prompts ="Write a tagline for an ice cream shop"

response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts, 
                                    max_tokens=6)
print(response)
```
Click the button below to see the full response.

{Try it!}(python3 tokens.py)

We can see there is a <b>usage</b> being printed and there we can see the total tokens being used. It tells us the total number of tokens, and how they are split between prompt and completion. Now try modifying the `max_tokens` keyword argument from $6$ to $9$. 

```python
response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts, 
                                    temperature=0, 
                                    max_tokens=9)
```


{Try it!}(python3 tokens.py 2)

We can see the completion token going from $6$ to $9$. 


|||challenge
## Try these variations:

* Try running the code when you set `max_tokens=10`

{Try it!}(python3 tokens.py 6)

* Try running the code when you set `max_tokens=16`

{Try it!}(python3 tokens.py 3)

* Try running the code when you set `max_tokens=30`

{Try it!}(python3 tokens.py 4)

|||


As you can see after a certain number of tokens, the completion token won't change in value. That is because we have reached the maximum number of tokens that could be assigned. Note, the **max_tokens** keyword argument has a default value of 16 and simply sets a boundary for the number of tokens to be generated in the completion.

Now try the following, change our prompt to the following:
```python
prompts ="Write a tagline for an ice cream shop in Paris"
```
{Try it!}(python3 tokens.py 5)

We can see the prompt token switch from $9$ to $11$. It is evident, that the `prompt_tokens` simply displays the number of tokens present in the given prompt.

{Check It!|assessment}(multiple-choice-1981471950)
