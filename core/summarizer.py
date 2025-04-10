import os
os.environ["TRANSFORMERS_NO_TF"] = "1"

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Use a better summarization model
model_name =  "google/pegasus-xsum"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def generate_summary(text, language="English"):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        max_length=1024,
        truncation=True,
        padding=True
    )

    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=150,
        min_length=40,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True
    )

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary
