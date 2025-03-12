import os
from langchain.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from dotenv import load_dotenv
load_dotenv()

model_id = os.getenv("MODEL")
max_length = int(os.getenv("TOKEN_LENGTH"))
# Load model directly
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)


pipe = pipeline(
    "text2text-generation",
    model = model,
    tokenizer=tokenizer,
    max_length = max_length,
    device_map="auto"
)

local_llm = HuggingFacePipeline(pipeline=pipe)