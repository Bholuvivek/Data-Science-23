import streamlit as st
import pandas as pd
import numpy as np
import os

#Page Heading
st.header(" :red[🍺🍸This ia my WebAoo and Here is All Pubs Information in United Kingdom🍺🍸]")
st.subheader(":blue[This is Developed by Vivek Kumar Singh]")

#Background Image
page_bg_img = '''
<style>
.stApp { 
background-image: url("");
background-size: cover;
background-position: top center;
background-repeat: no-repeat;
background-attachment: local;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

#Reading data
FILE_DIR1 = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(FILE_DIR1,os.pardir)
dir_of_interest = os.path.join(FILE_DIR, "resourses")
DATA_PATH1 = os.path.join(dir_of_interest, "open_pubs_clean.csv")
df = pd.read_csv(DATA_PATH1)
with st.expander(label='Click Here to see the dataset overview',expanded=False):
    st.dataframe(df)

#Unique Bars and Local Authorities
unique=['Number of Pubs', 'Number of Local Authorities','Number of Postal Code']

option=st.radio(label="Select below options to see total count",
                options=unique,label_visibility="visible", horizontal=False)

if option=='Number of Pubs':
    st.subheader(f"Total Pubs in UK: :blue[{df['name'].nunique()}]")
elif option=='Number of Postal Code':
    st.subheader(f"Total Post Codes in UK: :blue[{df['postcode'].nunique()}]")
else:
    st.subheader(f"Total Local Authorities in UK :blue[{df['local_authority'].nunique()}]")

st.subheader(":red[🥂🍹Pubs are at the heart of British communities and serve as places for friends to gather, people to relax and unwind and stories to be told🥂🍹.]")

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