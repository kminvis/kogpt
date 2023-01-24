import streamlit as st  # pylint: disable=import-error
from streamlit.components.v1 import html

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM 



def on_button_click():

    st.write("다시 시도해 주십시오")
        
st.button("예측확인", on_click=on_button_click)
