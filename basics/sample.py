from openai import OpenAI 
import argparse

"""
Some working assumptions: 
"""


# ====================================================================|=======: 
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

    def ask(self,question): 
        completion = self._client.chat.completions.create(
            model = self.model, 
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": question, 
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
    parser.add_argument("-d", "--debug", action="store_true")
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
    if args.debug: 
        for k,v in args.__dict__.items(): 
            print("DEBUG: [_handle_clargs]: %12s --> %s"%(k,v)) 
    return args
# ====================================================================|=======: 
if __name__ == "__main__": 
    args = __handle_clargs()
    agent0 = Agent(model = args.model, port=args.port) 
    #agent0._test_prompt()



    # Receive task: 
    task = "Create a hello-world Python program"

    final_task = f"""
    Assume you are software developer and have been given the following 
    task: 

    '{task}'


    How would you go about resolving it? What would your steps be? 
    """
 
    agent0.ask(final_task)




