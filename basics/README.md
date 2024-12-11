---
# Overview 
In the name of simplicity, I've set this up to work with ollama. 
I am mainly concerned with the *infrastructure* rather than the 
performance at this point. 


For details of how to update ollama models see the following link: 
https://github.com/ollama/ollama/blob/main/README.md#customize-a-prompt


Server Side:
```
ollama pull llama3.2:1b
```


Client-side: 
```
python sample.py --model llama3.2:1b --backend ollama
```

