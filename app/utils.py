from transformers import (
    GPT2LMHeadModel,
    GPT2Tokenizer,
)

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model1 = GPT2LMHeadModel.from_pretrained("gpt2")


def gen_text(min_length=20, max_length=40,
             temperature=1.0, sentence_prefix=''):
    min_length = int(min_length)
    max_length = int(max_length)
    temperature = float(temperature)

    input_ids = tokenizer.encode(
        sentence_prefix,
        add_special_tokens=False,
        return_tensors="pt",
        add_space_before_punct_symbol=True,
    )

    output_ids = model1.generate(
        input_ids=input_ids,
        temperature=temperature,
        do_sample=True,
        min_length=min_length,
        max_length=max_length,  # desired output sentence length
        pad_token_id=model1.config.eos_token_id,
    )[0].tolist()

    generated_text = tokenizer.decode(
        output_ids,
        clean_up_tokenization_spaces=True)

    return generated_text
