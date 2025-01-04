from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()

    def predict(self, text):
        # Load
        tokenizer = AutoTokenizer.from_pretrained("/content/tokenizer")

        # Prediction
        gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 60}

        pipe = pipeline("summarization", model=self.config.model_path, tokenizer=tokenizer)

        ##
        print("Dialogue:")
        print(text)

        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)

        return output