from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import warnings

warnings.filterwarnings("ignore")

model_name = "HuggingFaceTB/SmolLM2-360M-Instruct"

print("Loading model...")

tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.unk_token

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="cpu",
    torch_dtype=torch.float32
)

messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant. Give short and concise answers in 2-3 lines."
    }
]

print("Chatbot started. Type 'exit' to quit.\n")

while True:
    user_input = input("> ")

    if user_input.lower() == "exit":
        break

    # --- ALL OF THIS MUST BE INDENTED INSIDE THE LOOP ---
    # 1. Append user message
    messages.append({"role": "user", "content": user_input})

    # 2. Keep the system prompt + last 10 exchanges max
    messages = [messages[0]] + messages[-10:]

    # 3. Apply chat template
    tokenized = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        return_tensors="pt",
        return_dict=True,
        max_length=512
    )

    # 4. Generate response
    with torch.inference_mode():
        outputs = model.generate(
            tokenized["input_ids"],
            attention_mask=tokenized["attention_mask"],
            max_new_tokens=60,
            temperature=0.5,
            top_p=0.8,
            do_sample=True,
            repetition_penalty=1.3,
            no_repeat_ngram_size=3,
            pad_token_id=tokenizer.pad_token_id
        )

    # 5. Decode only the new generated tokens
    response = tokenizer.decode(
        outputs[0][tokenized["input_ids"].shape[-1]:],
        skip_special_tokens=True
    ).strip()
    
    print(f"Bot: {response}\n")

    # 6. Append assistant message to history
    messages.append({"role": "assistant", "content": response})