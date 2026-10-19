import streamlit as st
import utils

st.title("Machine Translator")

tokenizer, model = utils.get_model("facebook/nllb-200-distilled-1.3B") # need to change when I move to the cluster

source = st.selectbox(
    "Choose a source language",
    utils.FLORES200_CODES.items(),
    index=None, 
    format_func=lambda x: x[1]
)

target = st.selectbox(
    "Choose a target language",
    utils.FLORES200_CODES.items(),
    index=None,
    format_func=lambda x: x[1]
)

if not target or not source:
    st.warning("Please select both a target and a source language.") 

if source and target:
    input = st.text_area("Text to translate")
    translate_btn = st.button("Ready to Translate")

    if translate_btn:    
        with st.spinner("Translating. Please wait a moment..."):
            translation = utils.translate(
                input_seq=input,
                tokenizer=tokenizer,
                model=model,
                source=source[0],
                target=target[0]
            )

        output = st.text_area("Translated text", value=translation)