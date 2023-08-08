## Word and Token

The API treats words according to their context in the text data. Remember The same word can have $2$ different tokens count depending on the structure of the text.


OpenAI provides a tokenizer tool with which we can experiment. Open the tool with this [link](https://beta.openai.com/tokenizer). Try the following in the playground: 

``` markdown
red is my favorite color.
```
![picture of the OpenAI tokenizer playground box. The text "red is my favorite color" is inside the text playground box. As response one can see the number of tokens is 6 and the number of characters is 25. After that we can see the "red is my favorite color" and a period broken up and with each word being in a different color.](.guides/img/tokenizer.PNG)


The playground uses different colors to show the breakdown between token assignment. When we click on the `TOKEN IDS` instead of text at the bottom, we can see the tokens associated with each word. 

![ We see two boxes with the words Text and Token IDS. The Token IDS box is circled in red ](.guides/img/tokenIDS.PNG)


Now change the lowercase `r` in red to capital `R`, check the token id to see if anything changed. 

The same word can have $2$ different tokens count depending on the structure of the text. On that same note, how we split up our words into tokens is language-dependent.

|||
## Try these variations: 
---
Enter the following words in the tokenizer playground and compare the token IDS with the expected output below.

**Enter the word:** `Red`
**Expected output**: `[7738]`

**Enter the words:**  `The Red`
**Expected output**: `[464, 2297]`

**Enter the words:**  `The Red keep`
**Expected output**: `[464, 2297, 1394]`

**Enter the words:**  `Red keep`
**Expected output**: `[7738, 1394]`


When comparing all the different tokens associated with `red`, you will find out that: 

* The token generated for a word varies depending on its placement within the sentence or if capitalized or not 
* Tokens can include trailing space characters

|||

The more we know about tokens it can help with a better prompt design. For example, prompts ending with a space character may result in lower-quality output. This is because the API already incorporates trailing spaces in its dictionary of tokens.

More on tokens and how to count them can be found on the OpenAI [website](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them)

{Check It!|assessment}(multiple-choice-1873431989)
