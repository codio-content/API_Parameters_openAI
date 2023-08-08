##


**top_p**, an alternative to sampling with temperature, is also referred to as nucleus sampling. Generally, it is not recommended to alter both the temperature and the `top_p`. `top_p` controls how many random results should be considered for completion as per the temperature. If we set so $0.1$ means only the tokens comprising the top $10%$ probability mass are considered.

Remember how when using the temperature of $1$ we had different answers show up. Let's try setting the `top_p=0.1`,meaning only top $10%$ of probable answers. 

```python
prompts ="Write a tagline for an ice cream shop"

response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts,
                                    n=5,
                                    top_p=0.1)
for i in (response["choices"]):
  print(i["text"].strip()) 
```

{Try it!}(python3 TopP.py 1)

We can use our probabilities tool to see the probability associated with each token.  The Probability tool can be accessed in the OpenAI playground. Make sure we toggle the show probability tab.
![We see an image of the openAI playground side bar. In the side bar there it shows a drop down called "Show probabilities" ](fullspec.png)




![we see the sentence "The best ice cream in town!". The cursor hovers over the ice word and we see a drop down with words with different probabilities. ice=99.72% ,way=0.16%,place=0.04 percent,damn=0.03%,Ice=0.01%](.guides/img/topP.PNG)



Here we can see that the response generated $5$ times was the same. That is because it is taking the top $10%$ most probable responses which is the same. What happens when we switch `top_p=0.8`.

```python
response = openai.Completion.create(model="text-davinci-002", 
                                    prompt=prompts,
                                    n=5,
                                    top_p=0.8)
for i in (response["choices"]):
  print(i["text"].strip()) 
```


{Try it!}(python3 TopP.py 2)

We start to see more variation as it has a bigger pool of responses to choose from. 

{Check It!|assessment}(multiple-choice-336323277)
