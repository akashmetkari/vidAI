from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def answer_question(context, question):
    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
    model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")

    input_text = f"question: {question}  context: {context}"
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs, max_length=64, early_stopping=True)

    return tokenizer.decode(outputs[0], skip_special_tokens=True)
