from typing import Dict, Any, Callable
from langchain.schema.messages import HumanMessage, AIMessage
from utils.Worker import Worker

class Expert(Worker):
    def __init__(self, model: str, expert_instruction: Dict[str, str]) -> None:
        super().__init__(model=model)
        self.expert_instruction = expert_instruction
        self.system_prompts = self.config["expert"]['system_prompts']
        self.examples = self.config["expert"]['examples']
    
    def generate_argument(self, debate: Any, stream_handler: Callable) -> str:
        system_prompt = self.system_prompts["system1"].replace("##debate_topic##", debate.topic)
        system_prompt += "\n" + self.expert_instruction["instructions"]

        messages = [HumanMessage(content=system_prompt)]

        last_role = "user"
        for m in debate.memory:
            if m.role == "assistant":
                if last_role == "assistant":
                    # Insert a user message to maintain alternation
                    interjection = "What are your thoughts on this?"
                    messages.append(HumanMessage(content=interjection))
                messages.append(AIMessage(content=m.content))
                last_role = "assistant"
            else:
                messages.append(HumanMessage(content=m.content))
                last_role = "user"

        if last_role == "assistant":
            final_user_input = "What are your thoughts on this?"
            messages.append(HumanMessage(content=final_user_input))


        config = {
            "callbacks": [stream_handler]
        }

        for chunk in self.model.stream(messages, config=config):
            pass
        
