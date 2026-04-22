import streamlit as st
import plotly.express as px

st.title("Plotly Test App")
st.write("If you see this, Plotly is working!")

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")
st.plotly_chart(fig)
