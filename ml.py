from transformers import pipeline

class LLM:
    
    def __init__(self, model):
        self.model = model
        self.clf = pipeline(model)
        
    def askQuestion(self, context:str, question:str):
        return self.clf(
            question=question,
            context=context
        )
        
    