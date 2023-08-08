##

## The N Keyword Argument

We can use the keyword argument `n` to specify the number of parameters in order to generate multiple completions. It can use up your tokens fairly quickly be warned. By default, it is set to `n=1`. Let's remove our for loop and add an extra argument to our response and set that equal to $5$. 

```python
prompts ="Write a tagline for an ice cream shop"
response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts,
                                    n=5)
print(response)
```
{Try it!}(python3 best-of.py 1)

We can further clean up our text by changing our print statement to the following:
```python
for i in (response["choices"]):
  print(i["text"].strip()) 
```

Run the script again and Python will print five different responses to the prompt.

{Try it!}(python3 best-of.py 2)

## The Best Of Keyword Argument

The `best_of` keyword argument selects the best response to a query after `n` completions. Generating multiple completion can consume your token quota. Try running a code such that `n=5` and `best_of=4`.

```python
response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts,
                                    n=5,
                                    best_of=4)
```
{Try it!}(python3 best-of.py 3)

You will generate an error essentially saying you requested the server to return more choices than it will generate. `n` needs to be less than or equal to `best_of`. We don't need to use `n` in order to use `best_of`. It will generate $4$ completions but only print the *"best"* one.
```python
response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts,
                                    best_of=4)
```
{Try it!}(python3 best-of.py 4)


{Check It!|assessment}(multiple-choice-1858163621)

