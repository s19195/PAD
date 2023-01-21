import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Zadania streamlit")

page = st.sidebar.selectbox('Select page', ['Form', 'Plots'])

if page == 'Form':

    st.header("About")
    st.text("This is a Streamlit Demo")

    firstname = st.text_input("Please, enter your First name", "Type here")
    surname = st.text_input("Please, enter your Surname", "Type here")
    if st.button("Submit"):
        result = "Zapisano"
        st.success(result)
else:
    data = st.file_uploader("Upload your dataset", type=['csv'])
    if data is not None:
        df = pd.read_csv(data)
        select = st.selectbox("Select a chart:", {"Histogram", "Heatmap"})
        if select == 'Histogram':
            user_agent_df = df[["user_agent"]]
            fig = px.histogram(user_agent_df, "user_agent", title="Number Of Users Per Browser")
            st.plotly_chart(fig, use_container_width=True)
        else:
            gender = df[["gender"]]
            fig = px.bar(gender, title="User_agent")
            st.plotly_chart(fig)
