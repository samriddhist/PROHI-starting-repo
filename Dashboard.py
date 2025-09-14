import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="Dashboard",
    page_icon="👋",
)

st.title("Welcome to PROHI Dashboard! 👋")

name = st.text_input("Enter your name:")

age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ", age, "years old")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °C", "1.2 °C")
col2.metric("Wind", "9 kmph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.title("Select the Chart Colour!")

data = pd.DataFrame({
    "x": np.arange(20),          
    "y": np.random.randn(20)     
})


colour = st.color_picker("Pick the line chart colour here:", "#00f900")
st.write("You've selected colour: ", colour)

chart = (
    alt.Chart(data)
    .mark_line(color=colour)
    .encode(
        x="x",
        y="y"
    )
)

st.altair_chart(chart, use_container_width=True)
