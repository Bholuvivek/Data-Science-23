import streamlit as st
import pandas as pd
import numpy as np
import os

#Page Header
st.header(" :red[🍺🍸Search Nearest Pubs🍺🍸]")


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
#Load data
FILE_DIR1 = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.join(FILE_DIR1,os.pardir)
dir_of_interest = os.path.join(FILE_DIR, "resourses")
DATA_PATH1 = os.path.join(dir_of_interest, "open_pubs_clean.csv")
df = pd.read_csv(DATA_PATH1)

#Take input -latitude and longitude
col1,col2=st.columns(2, gap='medium')
with col1:
    lat=st.number_input(label="Enter Latitude Here", min_value=49.892485, max_value=60.764969)
with col2:
    lon=st.number_input(label="Enter Longitude Here", min_value=-7.384525, max_value=1.757763)

#Entered location
search_location=np.array((lat,lon))
#Original/available Location
original_location=np.array([df['latitude'],df['longitude']]).T
#Finding Euclidean distance
dist=np.sum((original_location-search_location)**2, axis=1)
#Adding Distance column to dataframe
df['Distance']=dist

#Asking user that how many nearest Pub they want to see
nearest=st.slider(label="How Many Nearest Pub You Want to See",
                   min_value=1, max_value=50, value=5)
data=df.sort_values(by='Distance', ascending=True)[:nearest]

#List of Bar Names
st.subheader(f"{nearest} Nearest Pubs:")

#Show Nearest Pubs on Map
st.map(data=data, zoom=None, use_container_width=True)

#Name and Address of Nearby Pubs
st.table(data[['name','address','local_authority']])