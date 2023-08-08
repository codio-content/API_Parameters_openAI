##

Let's start by seeing how **temperature** impacts the generated response. Temperature defaults to 1 and accepts values between $0$ and $2$ inclusive.

Try changing the value of temperature from the **default of $1$** to $0$ in the file on the left and compare how your output changes.

```python
prompts ="Write a tagline for an ice cream shop"
response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts,
                                    temperature=0) ## added

print(response['choices'][0]['text'].strip())
```

Try running the code a few times by clicking the button below multiple times.

{Try it!}(python3 temp.py 1)

You probably got the same output each time. When `temperature` is set to $0$ it is referred to as **argmax sampling**, meaning the option with the highest probability is always selected. The option with the highest probability will perceive as the most *"correct"* answer. Higher temperatures will generate a more diverse response.

|||challenge
## Try these variations:

* Try running the code multiple times when you set `temperature` to `0.5`:

```python
response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts,
                                    temperature=0.5)
```

{Try it!}(python3 temp.py 2)

* Try running the code multiple times when you set `temperature` to `1.7`:

```python
response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts,
                                    temperature=1.7)
```

{Try it!}(python3 temp.py 3)
|||

You might have picked up at this point that *temperature controls how much randomness is in the output.* **Lower temperature means less randomness** which is suitable for contexts which require more stable output. **Higher temperature means more randomness** which is suitable for more creative applications.

You can read more about `temperature` in the [OpenAI docs.](https://beta.openai.com/docs/api-reference/completions/create#completions/create-temperature) 

<details>
  <summary>
     <strong>Seeing Probabilities</strong>
  </summary>
  <blockquote>
    The <a href="https://beta.openai.com/playground">OpenAI playground</a> has a <strong>Show Probabilities</strong> setting you can turn on that shows the probability of generated words:

  <img src=".guides/img/playgroundProbability.png" alt="a close up of the OpenAI playground settings options with Show probabilities setting set to Most likely" width="200">

  This creates a heat map where the darker the shade of the generated text means the more confident the model is about it. You can click on a word to see the different options that were considered and their related probabilities.

  <img src=".guides/img/probabilities.png" alt="The generated text My favorite animal is a lion where all except the last word are highlighted with a deep orange indicating high confidence and the last word, lion, is a lighter shade. The word lion has been clicked on to reveal the probabilities menu revealing lion had a 50% probability, dog had 14%, cat 11%, horse 8% and tiger 4%" width="400">

You can run the same prompt multiple times with different temperatures to see how it affects the displayed probabilities.
</blockquote>
</details>
<br>

To see this difference, let's generate 3 responses at a low temperature $(0.2)$ and $3$ responses at a high temperature $(0.8)$:

```python
prompts ="Write a tagline for an ice cream shop"

print('Temperature 0.2:')
print('----------------')
for i in range(3):
  response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts,
                                    temperature=0.2)

  print(response["choices"][0]["text"].strip())

print('\n\nTemperature 0.8:')
print('----------------')

for i in range(3):
  response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts,
                                    temperature=0.8)

  print(response["choices"][0]["text"].strip())
```
{Try it!}(python3 temp.py 4)

You can try running the above a few times but note that it is asking for $6$ generations for each run so it will consume tokens quickly.

Here is an example of the output:

```markdown-hide-clipboard
Temperature 0.2:
----------------
The best ice cream in town!
The best ice cream in town!
The best ice cream in town!


Temperature 0.8:
----------------
Make your summer sweeter with our delicious ice cream!
There's always room for ice cream!
Come in for a brain freeze!
```

We can see that when we use a lower temperature, the same text response is generated repeatedly. With the higher temperature, we get a wider variety of output.

{Check It!|assessment}(multiple-choice-1704043853)
