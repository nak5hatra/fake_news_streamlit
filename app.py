import streamlit as st
from utils.main_urils.utils import load_models

model = load_models("models\model.pkl")
preprocessor = load_models("models\preprocessor.pkl")

st.title("Fake News Classification!")
title = st.text_input("Input News Headline:", "About Time! Christian Group Sues Amazon and SPLC for Designation as Hate Group")
test_data  = preprocessor.transform([title])
prediction = model.predict(test_data)

if prediction[0] == 1:
    st.write("The News ", "Real")
else:
    st.write("The News ", "Fake")
