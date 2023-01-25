import streamlit as st  # pylint: disable=import-error
from streamlit.components.v1 import html
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM 

def on_button_click():
    prompt = '인간처럼 생각하고, 행동하는 \'지능\'을 통해 인류가 이제까지 풀지 못했던'
    with torch.no_grad():
      tokens = tokenizer.encode(prompt, return_tensors='pt').to(device='cuda', non_blocking=True)
      gen_tokens = model.generate(tokens, do_sample=True, temperature=0.8, max_length=64)
      generated = tokenizer.batch_decode(gen_tokens)[0]

    st.write(generated)
        
st.button("예측확인", on_click=on_button_click)
