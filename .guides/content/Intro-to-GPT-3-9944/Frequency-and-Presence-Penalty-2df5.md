##

The last keyword arguments to introduce are `frequency_penalty` and `presence_penalty`. These two arguments are used to control the amount of repetition you see in the results. Both of these arguments have a value from $-2$ to $2$.

## Frequency Penalty
 **Frequency penalty** is used to decrease the likelihood of the same line being repeated word for word. The lower the value for `frequency_penalty`, the more likely you will see the same line repeated. Think of `frequency_penalty` as a way to not have too many same-word repetitions. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim. Set the value to $2$ and run the program. Try it with others values such as  $1$ then $0$  


```python
prompts ="Write a tagline for an ice cream shop"

response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts,
                                    n=5,
                                    frequency_penalty=2,
                                    presence_penalty=0)
for i in (response["choices"]):
  print("----")
  print(i["text"].strip()) 
```

{Try it!}(python3 penalty.py 1)

You should see the same completion appear more than once. Run it one or two more times to see the different ways in which completions can be repeated.

|||challenge
## Try this variation:

* Change `frequency_penalty` to `-2`

```python
frequency_penalty=-2,
```

{Try it!}(python3 penalty.py 2)

|||

## Presence Penalty 
**Presence Penalty** can be used to measure the probability of the completion to introduce a new topic. The presence penalty does not consider how many times the word has been used, but just if the word exists in the text overall. A positive value increases the odds of introducing a new topic. Think of `presence_penalty` as a way to not have too much topic repetition

```python
prompts ="Write a tagline for an ice cream shop"

response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts,
                                    n=5,
                                    frequency_penalty=0,
                                    presence_penalty=2)
for i in (response["choices"]):
  print(i["text"].strip()) 
```

{Try it!}(python3 penalty.py 3)

The completions should introduce new ways in which the model talks about ice cream.

|||challenge
## Try this variation:

* Change `presence_penalty` to `-2`

```python
                                    presence_penalty=-2)
```

{Try it!}(python3 penalty.py 4)

|||

## Effects of Frequency and Presence

Running code snippets can provide different results, which makes talking about these two ideas a bit difficult. Instead, we are going to look at a prompt below to see how the completion changes when using frequency and presence.

```markdown-hide-clipboard
"Describe the difference between cooking and baking"
```

### Neutral Frequency and Presence

The completion repeats certain words ("cooking") and phrases ("process of preparing food"). It is also of moderate length.

> Cooking is the process of preparing food by heating it, while baking is the process of preparing food by cooking it in an oven.

### Maximum Value for Frequency

When frequency is increased, you no longer see the repetition of an entire phrase, though the word "cooking" occurs twice.

> Cooking is the process of preparing food by heating it, while baking is a method of cooking that uses dry heat, typically in an oven.

### Maximum Value for Presence

Notice how the completion introduces new topics when it lists out the different methods of cooking food — baking, frying, and grilling.

> Cooking is the process of preparing food by heating it. This can be done in a number of ways, including baking, frying, and grilling. Baking is a type of cooking that involves using dry heat to cook food, typically in an oven.

### Maximum Value for Frequency and Presence

In the last example, you see the repetition of a few words but no phrases are used more than once. You also see the introduction of ideas like the consumption of food or the explicit statement that baking is a form of cooking.

> Cooking generally refers to the process of using heat to prepare food for consumption. Baking, on the other hand, is a specific type of cooking that involves using dry heat - usually in an oven - to cook food.

You can further use this [tool](https://gpttools.com/comparisontool) to generate more comparisons.

{Check It!|assessment}(multiple-choice-2370400853)
