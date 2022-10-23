import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import koreanize_matplotlib

st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(
    page_title="도로종류와 형태의 시간대, 기상상태 교통사고 분석",
    page_icon="🚗",
    layout="wide",
)

st.markdown("## 도로종류별 교통사고 분석🚗")
st.sidebar.markdown("## 도로종류별 교통사고 분석 🚗")

# 데이터 로드
# def load_rest_data():
#     kind_time = pd.read_csv('data/kind_time.csv',encoding = "cp949")
#     shape_time = pd.read_csv("data/shape_time.csv",encoding = "cp949")
#     return kind_time, shape_time
# kind_time, shape_time = load_rest_data()

url = "https://raw.githubusercontent.com/meji9086/Traffic-Accident-Data-Analysis/master/data/kind_time.csv"

@st.cache
def load_month_data(url):
    kind_time = pd.read_csv(url, encoding='UTF-8')
    return kind_time

kind_time = load_month_data(url)


@st.cache(allow_output_mutation=True)
def load_time_data():
    shape_time = pd.read_csv(
        "https://raw.githubusercontent.com/meji9086/Traffic-Accident-Data-Analysis/master/data/shape_time.csv"
        , encoding='UTF-8')
    return shape_time
shape_time = load_time_data()



st.markdown("""
가설: 직장인이 많이 사는 특별광역시도와 시도에는 출근시간과 퇴근시간에 사고수가 많을까?


##### 도로의 종류
- 고속국도:	자동차 교통망의 중추부분을 이루는 중요도시를 연 결하는 자동차 전용의 고속교통이 이용하는 도로


- 일반국도:	중요도시, 지정항만, 중요한 비행장, 관광지 등을 연 결하며 국가 기간 도로망을 이루는 도로	)


- 특별 광역시도: 서울특별시, 부산·대구·인천·광주·대전·울산광역시 구 역내의 도로	


- 지방도(국가지원 지방도):	도내의 주요 도시를 연결하며 지방의 간선도로망을 이루는 도로


- 시도: 시 구역내의 도로	


- 군도: 군 구역내의 도로	


- 구도: 구 구역내의 도로	

""")


if st.checkbox('데이터 확인'):
    st.subheader('도로종류별 시간별 데이터')
    st.write(kind_time,shape_time)


# 도로종류별 사고수 나타내기
st.markdown("""
#### 도로종류별 사고수
""")
fig,ax = plt.subplots(figsize = (15,4))
kind_time.groupby(["도로종류"])["사고수"].mean().sort_values(ascending=False).plot(kind = "bar",title = "도로종류별 사고수",rot = 0, colormap='hsv')
plt.title("도로종류별 사고수")
st.pyplot(fig)


st.markdown("""
사람이 많이 다니는 특별광역시도와 시도에 사고가 집중적으로 나는것을 확인할 수 있다.

그럼 과연 어느시간대에 가장 많은 사고가 발생할까?
""")

# 도로종류별 시간대 사고수
st.markdown("""
#### 도로종류별 시간대 사고수
""")
fig,ax = plt.subplots(figsize = (15,4))
sns.barplot(data = kind_time, x="시간대", y = "사고수",ci=None,hue = "도로종류")
plt.title("도로종류별 시간대 사고수")
st.pyplot(fig)



st.markdown("""
그래프를 살펴보면 08시 - 10시에 사고수가 급증하고 18시 - 20시에 사고수가 줄어드는 것을 확인할 수 있다

""")


# 가설: 직장인이 많이 사는 특별광역시도와 시도에는 출근시간과 퇴근시간에 사고수가 많을까?
# 직장인이 많이 사는 특별광역시도와 시도는 출근시간인 8시경이되면 사고수가 급격하게 늘어나고 퇴근시간인 6시에 정점을 찍는다.
# 직장인이 많이 다니지않는 고속국도, 군도, 지방도, 일반국도에는 사고수가 균일함을 알 수 있음
# 어느정도 가설이 맞는것을 확인

st.markdown("""
#### 도로종류별 시간대별 사고수
""")
sns.catplot(data = kind_time, x="시간대", y = "사고수",col = "도로종류", kind="point", col_wrap=3,ci=None)
plt.title("도로종류별 시간대 사고수")
st.pyplot()



st.markdown("""
#### 결과

출근시간인 8시경이되면 사고수가 급격하게 늘어나고 퇴근시간인 18 - 20시가 지나면 사고수가 줄어든다고 해석이 가능하다.

직장인이 많이 다니지않는 고속국도, 군도, 지방도, 일반국도에는 시간대별로 큰 차이 없이 사고수가 균일함을 알 수 있다.

따라서 "직장인이 많이 사는 특별광역시도와 시도에는 출근시간과 퇴근시간에 사고수가 많을까?" 라는 가설은 성립한다고 볼 수있다.


""")


st.markdown("""
## 도로형태별 교통사고🚗
""")

st.markdown("""
분석목표: 어떤 형태의 도로에서 교통사고가 가장 많이 발생할까? 

그리고 발생하는 이유는 무엇일까?
""")

st.markdown("""
##### 도로의 형태

- 단일로-터널안 : 터널 내를 말하며, 입구의 도로부분을 포함하지 않음.


- 단일로-교량위 : 일반적인 교량과 고가차도(철도 또는 도로와의 교차하는 지점의교통을 원활히 하기 위해 설치한 입체시설물)을 말함


- 단일로-고가도로 위 : 기둥과 받침대 따위를 땅위에 높이 설치하고 그 위에 가설한도로에서 발생한 사고


- 단일로-지하도로 내 : 지하에 설치하는 도로(도로․광장 등의 지하에 설치된 지하공공보도시설을 포함)를 말하며 고가도로 내에서 발생한경우


- 단일로-기타 : 단일로 사고 중 상기의 어느 유형에도 해당하지 않는 경우


- 교차로-교차로 내 : 교차로 내에서 발생한 사고


- 교차로-횡단보도 내 : 교차로에서 설치된 횡단보도 위에서 사고가 발생한 경우,단 교차로 대각선 횡단보도의 경우 교차로 내 전체를 횡단보도로간주


- 교차로-교차로 부근 : 교차로 측단에서 30m 이내의 도로에서 발생한 사고
""")


# 가장 많이 사고가 일어난곳
st.markdown("""
#### 도로형태별 사고수
""")
fig,ax = plt.subplots(figsize = (15,4))
shape_time.groupby(["도로형태"])["사고수"].mean().sort_values(ascending=False).plot(kind = "bar",title = "시간대별 사고수", rot = 0,colormap = "winter")
plt.title("도로형태별 사고수")
st.pyplot(fig)


st.markdown("""
가장 많은 사고를 발생한 도로의 형태는 교차로내이다. 

2번째 3번째도 교차로에서 발생한 사고이다.

교차로 부근에서 교통사고가 가장 많이 발생하는것을 알 수있다.


""")

# 도로형태별 시간대별 사고수 시각화
st.markdown("""
#### 도로형태별 시간대별 사고수
""")
sns.catplot(data = shape_time, x="시간대", y = "사고수",col = "도로형태", kind="point", col_wrap=3,ci=None)
st.pyplot()


st.markdown("""
교차로에서 발생한 사고도 마찬가지로 08시에 사고수가 급증하고 20시 이후로 사고수가 줄어드는 것을 알 수있다.

이것또한 출퇴근 시간의 영향으로 보인다.
""")

# 도로형태별 월별 사고수 시각화
st.markdown("""
#### 도로형태별 월별 사고수
""")
sns.catplot(data = shape_time, x="월", y = "사고수",col = "도로형태", kind="point", col_wrap=3,ci=None)
st.pyplot()


st.markdown("""
교차로 부근에서 가장 많은 사고가 많이 나는 달은 4월과 여름휴가철인 7월에 가장 많은 사고가 난다.
""")



st.markdown("""
정밀한 비교를 위해 교차로내와 교차로부근 제외
""")
# 교차로가 없는 데이터 만들기
drop = shape_time["도로형태"].isin(["교차로내","교차로부근"])
df3_no_cross = shape_time[~drop]

# 교차로가 없는데이터, 도로형태별 시간대별 사고수 시각화
st.markdown("""
#### 도로형태별 시간대별 사고수_교차로부근 제외
""")

sns.catplot(data = df3_no_cross, x="시간대", y = "사고수",col = "도로형태", kind="point", col_wrap=3,ci=None)
st.pyplot()

# # 교차로가 없는데이터, 도로형태별 월별 사고수 시각화
# st.markdown("""
# #### 도로형태별 월별 사고수_교차로부근 제외
# """)
# sns.catplot(data = df3_no_cross, x="월", y = "사고수",col = "도로형태", kind="point", col_wrap=3,ci=None)
# st.pyplot()




st.markdown("""
교통사고는 터널안, 교랑위, 고가도로위, 자하차도등 형태보다 교차로 횡단보도에서 발생하는 사고가 많다.

실제로도 횡단보도에서 교통사고가 많이 발생하고 있다. 횡단보도에서 발생하는 교통사고중 가장 큰 이유가

보행자 신호등이 파란불이여도 우회전을 할 수 있어 사고가 많이 발생했었는데 이로인해

교통사고를 줄이고자 2022년 8월 우회전 할 때 '일시정지' 개정 도로교통법이 시행되었다.
""")


st.markdown("""
#### 결론

교차로 부근에서 사고가 많이 일어나는 이유를 찾아본결과

노인교통사고의 비율이 많은것을 알게되었다. 

행정안전부와 도로교통공단이 발표한 '21년 발생 노인보행자 교통사고 다발지역(30개소)'에 따르면

경동시장앞교차로부근,성바오르병원앞교차로, 충무교차로부근, 
부산진시장앞교차로 부근,대한생명앞 교차로부근 등 5곳이 선정되었다 

또한, 사고 다발지역 1위인 경동시장앞교차로부근의 보행자 사망 59%가 노인인것으로 발표되었다.

교통사고가 가장 많이 발생하는 교차로 부근에서의 사고수를 줄일려면 우선적으로

발걸음이 느린 노인들을 위한 교차로부근의 신호등 등과 관련된 정책등의 개선이 필요하다.



""")
