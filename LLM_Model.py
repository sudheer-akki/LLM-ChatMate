from langchain.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline


model_id = "MBZUAI/LaMini-Flan-T5-248M"

# Load model directly
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)


pipe = pipeline(
    "text2text-generation",
    model = model,
    tokenizer=tokenizer,
    max_length = 100,
    device_map="auto"
)


local_llm = HuggingFacePipeline(pipeline=pipe)