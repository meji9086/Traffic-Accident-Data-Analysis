import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import seaborn as sns
import koreanize_matplotlib
import plotly.express as px

st.set_page_config(
    page_title="Traffic Accident data analysis",
    page_icon="🚗",
    layout="wide",
)

st.markdown("# 🚗 교통사고 원인 분석 🚗")
st.sidebar.markdown("# 🚗 교통사고 원인 분석 🚗")

st.sidebar.header('법규위반으로 인한 교통사고')
st.sidebar.markdown("""
    ### 목차
    1. 가설 세우기
    2. 데이터 시각화
    3. 시각화 한 결과로 분석
    4. 가설 검증
""")

st.markdown("""
    ## 법규위반편
    ### 가설   
        1. 성격이 급한 한국인의 특성을 고려하여 신호위반의 사고가 가장 많을 것이다.       
        2. 야간에는 차가 많지 않아 신호를 무시하는 사람들이 많을 것이다. 
""")

# 데이터 불러오기
url = "https://github.com/meji9086/Traffic-Accident-Data-Analysis/raw/master/data/violation_raw_data.txt"
@st.cache
def load_data(url):
   df = pd.read_table(url, sep='\t')
   return df

data_load_state = st.text('Loading data...')
df = load_data(url)
data_load_state.text("Success! (using st.cache)")

# 사용할 데이터
## 유형별
df_ac = df.loc[df['유형']=='사고건수']
df_in = df.loc[df['유형']=='부상자수']
df_de = df.loc[df['유형']=='사망자수']
df_al = df.pivot_table(index='월', columns='유형', values='사고수')

## 법규위반별
df_r = df_ac.pivot_table(index='법규위반유형', values='사고수', 
                aggfunc='sum').sort_values(by='사고수', ascending=False)
df_r2 = df_in.pivot_table(index='법규위반유형', values='사고수',
                aggfunc='sum').sort_values(by='사고수', ascending=False)
df_r3 = df_de.pivot_table(index='법규위반유형', values='사고수', 
                aggfunc='sum').sort_values(by='사고수', ascending=False)
df_al2 = df.pivot_table(index='법규위반유형', columns='유형', values='사고수')

## 주야별
df_d = df.pivot_table(index='주야', columns='유형', values='사고수')
df_d1 = df_ac.pivot_table(index='주야', columns='법규위반유형', values='사고수')
df_d2 = df_in.pivot_table(index='주야', columns='법규위반유형', values='사고수')
df_d3 = df_de.pivot_table(index='주야', columns='법규위반유형', values='사고수')

# 데이터 시각화
st.markdown("### 데이터 시각화")

st.write("- 법규위반별 사고건수")

fig, ax = plt.subplots(figsize=(16,4))
sns.barplot(data=df_r, x=df_r.index, y='사고수', ci=None)
plt.title("법규위반별 사고건수")
plt.xticks(rotation=45)
st.pyplot(fig)

st.write("- 법규위반별 부장자수")

sns.barplot(data=df_r2, x=df_r.index, y='사고수', ci=None)
plt.title("법규위반별 부상자수")
plt.xticks(rotation=45)
st.pyplot(fig)

st.write("- 법규위반별 사망자수")

sns.barplot(data=df_r3, x=df_r3.index, y='사고수', ci=None)
plt.title("법규위반별 사망자수")
plt.xticks(rotation=45)
st.pyplot(fig)

st.write("- 주야별 법규위반별 사고건수")

fig, ax = plt.subplots(figsize=(16,4))
p2 = px.histogram(df_ac, x='주야', y='사고수', color='법규위반유형', barmode="group",
            title='주야별 법규위반별 사고건수')
p2

st.write("- 주야별 법규위반별 부상자수")

fig, ax = plt.subplots(figsize=(16,4))
p3 = px.histogram(df_in, x='주야', y='사고수', color='법규위반유형', barmode="group",
            title='주야별 법규위반별 부상자수')
p3

st.write("- 주야별 법규위반별 사망자수")

fig, ax = plt.subplots(figsize=(16,4))
p4 = px.histogram(df_de, x='주야', y='사고수', color='법규위반유형', barmode="group",
            title='주야별 법규위반별 사망자수')
p4

st.markdown("""
    ### 법규위반별 시각화를 통한 분석
    1. 신호위반과 안전거리미확보의 사고가 가장 많다.
        - 매 교통사고에 흔히 발생하는 교통사고의 원인이므로 법을 강화할 필요가 있다.
    2. 과속으로 인한 사망자가 많다.
        - 교통사고의 사망자를 줄이기 위해서는 과속했을 때의 안전을 더 유의해야 한다.
    3. 야간에는 신호위반 데이터가 월등하게 높다.
        - 야간에는 신호를 무시하는 경향이 높은 것이 원인이므로 신호를 철저하게 지켜야 한다.

    
    ### 가설 검증
    1. 성격이 급한 한국인의 특성을 고려하여 신호위반의 사고가 가장 많을 것이다.        
        -> 신호위반의 사고가 가장 많은 것을 알 수 있었다.        
        -> 안전거리의 미확보의 사고도 많이 발생한다.              
    2. 야간에는 차가 많지 않아 신호를 무시하는 사람들이 많을 것이다.          
        -> 야간에는 신호를 무시하는 사람들이 많았다.        
        -> 과속으로 인한 사망자도 많이 발생한다.              
""")

