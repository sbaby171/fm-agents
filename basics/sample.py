from openai import OpenAI 
import argparse

"""
Some working assumptions: 
"""


class Agent(object):
    def __init__(self, model, port, api_key="EMPTY"): 
        self.model = model
        self._client = OpenAI(
            base_url = f"http://localhost:{port}/v1", 
            api_key=api_key
        ) 
    def _test_prompt(self,): 
        completion = self._client.chat.completions.create(
            model = self.model, 
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": "What causes a red moon?"
                }
            ]
        )# end of completion 
        print(completion.choices[0].message.content)
# ====================================================================|=======: 
def __handle_clargs(): 
    # ----------------------------------------------------------------|-------:
    parser = argparse.ArgumentParser() 
    parser.add_argument("-m", "--model", type=str, help="Model to be used")
    parser.add_argument("-b", "--backend", choices=["ollama","vllm"], 
                        help="this is used to help establish the URL "\
                         "and ports for OpenAI API compatibility.")
    parser.add_argument("--port", help="If not provided, port number will "\
                        "be inferred from `backend` argument.")
    # ----------------------------------------------------------------|-------:
    args = parser.parse_args()
    # ----------------------------------------------------------------|-------:
    if not args.model: 
        raise RuntimeError("Must provide `model` argument.")
    if not args.port: 
        if args.backend == "ollama": 
            args.port = 11434
        elif args.backend == "vllm": 
            args.port = 8000
    for k,v in args.__dict__.items(): 
        print(k,v) 
        
    return args
# ====================================================================|=======: 
if __name__ == "__main__": 
    args = __handle_clargs()
    agent0 = Agent(model = args.model, port=args.port) 
    agent0._test_prompt()