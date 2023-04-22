import streamlit as st
import os

st.set_page_config(layout="wide")
st.title("🍻Here is all Name of Pubs of United Kingdom To Have Some Drink And Chillout🍻")
st.subheader('By: :blue[Vivek Kumar Singh]')


st.subheader(":green[For Any Query Connect with me on,]")

col1,col2,col3=st.columns(3, gap='small')
with col1:
    st.subheader("[LinkedIn](https://www.linkedin.com/in/vivekbholu/)")
with col2:
    st.subheader("[GitHub](https://github.com/Bholuvivek)")
with col3:
    st.subheader("[Instagram](https://www.instagram.com/thevivekbholu/)")
#with col4:
 #   st.subheader("[Tableau](tblu link dalna hai)")


st.header(":green[Go To Another Page With the given Link]")

st.subheader("For Pubs Innformation [Click Here](/Pub_Info)")
st.subheader("For Pubs Location[Click Here](/Pub_Location)")
st.subheader("For Finding Near Pub to you[Click Here](/Find_Nearest_Pubn)")



annotations = [
    dict(
        name="draft watermark",
        text="Vivek",
        textangle=-30,
        opacity=0.1,
        font=dict(color="blue", size=100),
        xref="paper",
        yref="paper",
        x=0.5,
        y=0.5,
        showarrow=False,
    )
]