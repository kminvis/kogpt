import streamlit as st  # pylint: disable=import-error
from streamlit.components.v1 import html

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM 

def on_button_click():
    tokenizer = AutoTokenizer.from_pretrained(
      'kakaobrain/kogpt', revision='KoGPT6B-ryan1.5b-float16',  # or float32 version: revision=KoGPT6B-ryan1.5b
      bos_token='[BOS]', eos_token='[EOS]', unk_token='[UNK]', pad_token='[PAD]', mask_token='[MASK]'
    )
    model = AutoModelForCausalLM.from_pretrained(
      'kakaobrain/kogpt', revision='KoGPT6B-ryan1.5b-float16',  # or float32 version: revision=KoGPT6B-ryan1.5b
      pad_token_id=tokenizer.eos_token_id,
      torch_dtype='auto', low_cpu_mem_usage=True
    ).to(device='cuda', non_blocking=True)
    _ = model.eval()
    prompt = '인간처럼 생각하고, 행동하는 \'지능\'을 통해 인류가 이제까지 풀지 못했던'
    with torch.no_grad():
      tokens = tokenizer.encode(prompt, return_tensors='pt').to(device='cuda', non_blocking=True)
      gen_tokens = model.generate(tokens, do_sample=True, temperature=0.8, max_length=64)
      generated = tokenizer.batch_decode(gen_tokens)[0]

    st.write(generated)

st.button("예측확인", key='confirm_btn', on_click=on_button_click)
