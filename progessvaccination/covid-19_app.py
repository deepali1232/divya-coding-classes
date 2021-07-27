import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
from PIL import Image
import cv2

#page ------------------------------------------------------------------------------------------------setup#

st.set_page_config(page_title='covid-19 world vaccination progress visualization',layout="wide")
st.sidebar.header('Covid-19 World Vaccination Progress Visualization',anchor='vaccination progress')
##################################################


#header--------------------------------------------------------------------------------------------part#
with st.spinner('loading data..'):
    st.markdown("""
                <style>
                    .mainhead{
                                text-align:left;
                                font-family: Courgette ,Book Antiqua ;
                                #letter-spacing:.1px;
                                word-spacing:1px;
                                color :#0000FF; 
                                text-shadow: 1px -1px 1px white, 1px -1px 2px white;
                                font-size:40px;
                             }
                </style>
                        """, unsafe_allow_html=True)

st.markdown("""
            <style>
                .detail{
                    font-size:18px;
                    letter-spacing:.1px;
                    word-spacing:1px;
                    font-family:Calibri;
                    color:#000000;
                    display:inline-block;
                        }
            </style>
            """, unsafe_allow_html=True)



st.markdown('<h1 class="mainhead"> Covid-19 World Vaccination Progress Visualization</h1> <img src="" />',
                unsafe_allow_html=True)

col1, col2 = st.beta_columns([5, 10])

with col1:
    img = Image.open("progessvaccination/image/4.gif")
    st.image(img, width=300)
                                                        # display image using streamlit
                                                        # width is used to set the width of an image

with col2:
    col = st.beta_container()

    with col:
        st.markdown("""
                    <style>
                        .content{
                                    margin-top: 5%;
                                    letter-spacing:.1px;
                                    word-spacing:1px;
                                    color: #00008B;
                                    margin-left:5%;}
                    </style>
                    """, unsafe_allow_html=True)
        st.markdown('<p class="content">Hey  There! <br> Welcome To My Project.This Project is all about covid-19 world vaccination progress visualization.We will be analyzing the vaccination progress across the whole world on the basis of country,dates,total vaccinations,people_vaccinated, people_fully_vaccinated,daily_vaccinations,total_vaccinations_per_hundred,people_vaccinated_per_hundred,people_fully_vaccinated_per_hundred,daily_vaccinations_per_million.Our motive is to give you idea about the vaccination progress,how many peoples are vaccinated how many of not vaccinated.<br>One last tip, if you are on a mobile device, switch over to landscape for viewing ease. Give it a go! </p>', unsafe_allow_html=True)
        st.markdown(
            '<p class="content" style = "float:right;"> Made By Divya Srivastava</p>', unsafe_allow_html=True)
st.markdown("")
st.markdown("___")


#data set ------------------------------------------------------------------detail
df=pd.read_csv("progessvaccination\dataset\country_vaccinations.csv")
df.drop(['iso_code','vaccines','source_name','source_website'],axis=1,inplace=True)


st.markdown(""" 
            <style>
                .head{
                    font-family: Calibri, Book Antiqua; 
                    font-size:4vh;
                    padding-top:2%;
                    padding-bottom:2%;
                    font-weight:light;
                    color:#ffc68a;
                    #text-align:center;
                    }
            </style>
            """, unsafe_allow_html=True)
@st.cache(suppress_st_warning=True)
def viewDataset(pathlist):
    with st.spinner("loading data....."):
        st.markdown('<p class="head"> DataSet Used In This Project  </p>',
                     unsafe_allow_html=True)

st.markdown("")
st.dataframe(df)

st.markdown(""" 
            <style>
                .block{
                         font-family: Book Antiqua; 
                         font-size:24px;
                         padding-top:11%;
                         font-weight:light;
                         color:darkblue;
                      }
            </style>
                """, unsafe_allow_html=True)
st.markdown('---')
cols = st.beta_columns(4)
cols[0].markdown(
            '<p class="block"> Number of Rows : <br> </p>', unsafe_allow_html=True)
cols[1].markdown(f"# {df.shape[0]}")
cols[2].markdown(
            '<p class= "block"> Number of Columns : <br></p>', unsafe_allow_html=True)
cols[3].markdown(f"# {df.shape[1]}")
st.markdown('---')

st.markdown('<p class= "head"> Summary </p>', unsafe_allow_html=True)
st.markdown("")
st.dataframe(df.describe())
st.markdown('---')


types = {'object': 'Categorical',
                 'int64': 'Numerical', 'float64': 'Numerical'}
types = list(map(lambda t: types[str(t)], df.dtypes))
st.markdown('<p class="head">Dataset Columns</p>',
                    unsafe_allow_html=True)
for col, t in zip(df.columns, types):
            st.markdown(f"## {col}")
            cols = st.beta_columns(4)
            cols[0].markdown('#### Unique Values :')
            cols[1].markdown(f"## {df[col].unique().size}")
            cols[2].markdown('#### Type :')
            cols[3].markdown(f"## {t}")
            st.markdown("___")

####################################################
