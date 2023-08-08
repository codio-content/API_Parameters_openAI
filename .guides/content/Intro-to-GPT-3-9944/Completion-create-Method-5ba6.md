##

To generate a response to a prompt, we use the `openai.Completion.create` method. Note that we have already imported the `openai` package.

```python
prompts ="Write a tagline for an ice cream shop"
response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts)

print(response['choices'][0]['text'].strip())
```

Copy the code above into the file on the left and click the button below to run the code file.

{Try it!}(python3 completion.py)

Notice how the method takes two keyword arguments. The **[model keyword argument](open_file completion.py panel=0 ref="model" count=1)** is mandatory and the prompt is specified using the **[prompt keyword argument.](open_file completion.py panel=0 ref=" prompt" count=1)**

[Remove highlighting](open_file completion.py panel=0)

There are many additional optional keyword arguments that can be specified in our API call. You can get a sense of these settings using the right-hand pane of the OpenAI playground. Open the [playground](https://beta.openai.com/playground) (the link opens in a new tab). Clicking on **View code** on the upper right will translate the sliders and text boxes into code.

![Animation showing OpenAI UI where cursor moves to top-right corner and clicks on the View code button resulting in a pop up titled View code with an API call with arguments model, prompt, temperature, max_tokens, top_p, frequency_penalty, and presence_penalty](.guides/img/promptPlayground.gif)

Here is an example of an API call using more keyword arguments:

```python-hide-clipboard
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-002",
  prompt="",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
```
We will cover what each of these keyword arguments does throughout this assignment.

{Check It!|assessment}(multiple-choice-1473826894)