from langchain.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import torch

model_id = "facebook/blenderbot-1B-distill"

# Load model directly
tokenizer = AutoTokenizer.from_pretrained(model_id)

if torch.cuda.is_available():
    model = AutoModelForSeq2SeqLM.from_pretrained(model_id,load_in_8bit = True)
else:
    model = AutoModelForSeq2SeqLM.from_pretrained(model_id)


pipe = pipeline(
    "text2text-generation",
    model = model,
    tokenizer=tokenizer,
    max_length = 100,
    device_map="auto"
)


local_llm = HuggingFacePipeline(pipeline=pipe)