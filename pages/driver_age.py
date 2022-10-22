import pandas as pd
import plotly.express as px
import koreanize_matplotlib
import streamlit as st

st.set_page_config(
    page_title="연령별 교통사고 발생건수 분석",
    page_icon="🚕",
    layout="wide",
)
st.markdown("""### 🚗연령별 교통사고 발생건수 분석👶""")


url = "https://raw.githubusercontent.com/meji9086/Traffic-Accident-Data-Analysis/master/data/age_months.csv"

@st.cache
def load_month_data(url):
    age_month = pd.read_csv(url, encoding='UTF-8')
    return age_month

age_month = load_month_data(url)

age_month.columns = ["연령", "합계", "월", "발생건수"]

"""
###### 🔸데이터 : TAAS 교통사고분석시스템의 2021년 교통사고 가해운전자 연령층별 데이터를 사용했다.
\n🔸 20세 이하와 61-64세 이하 운전자는 연령 폭이 좁아 교통사고 발생 건수가 적게 나타났는데,
\n🔸 해당 연령의 구분이 분석에 필요해서 따로 처리하지 않았다.  
#
"""

"""
\n 
#### 🚗 연령별 교통사고 발생건수
**- 가설** : \n교통사고 발생량이 많은 특정 연령이 있을 것이다."""

age_hist0 = px.histogram(age_month, x="연령", y="발생건수", 
                         histfunc="sum", title="연령별 교통사고 발생 건수", width=800, height=400)
age_hist0

"""
**분석 결과** : 51-60세 운전자의 교통사고 건수가 높게 기록되었다. 
\n 그렇지만 이 차트를 보고 고령 운전자의 교통사고 비율이 높다고 판단할 수는 없다.
\n 분석에 사용한 데이터는 가해자의 연령을 기준으로 교통사고 발생 건수를 조사한 것으로, 
\n 각 연령대의 교통사고 가해자 비율이 아니다.
#
\n 51-60세 운전자가 다른 연령대에 비해 사고를 많이 발생키시는 것인지
\n 해당 연령대에 운전자 수 자체가 많은 것인지 명확하지 않아 가설을 검증할 수 없었다.  
#
#
"""


"""
#### 🚗 20세 이하 운전자의 월별 교통사고 발생 건수  
**가설** : 20세 이하 운전자의 경우 연말과 연초, 11 ~ 2월 동안 사고 건수가 많을 것이다.
\n 수능이 끝난 뒤 면허를 취득한 20세 이하 운전자들의 사고가 이 시기에 집중될 것이라 예상했다.
"""


# 20세 이하 운전자만 추출
under_age = age_month.loc[age_month["연령"] == "20세이하"]
age_bar0 = px.line(under_age, x="월", y="발생건수", title='20세 이하 운전자의 월별 교통사고 발생 건수'
                   , width=800, height=500, markers=True)
age_bar0

"""
\n **분석 결과** : 연말과 연초를 기점으로 점차 사고가 늘어나고 특히 2월과 3월 동안 큰 폭으로 상승했다.
\n 가설과 달리 오히려 연말과 연초에 사고 건수가 가장 적었다.
\n 특히 4월의 사고 건수는 1월에 비해 2배 가까이 증가했다.
\n 이는 면허를 취득하는 시기와 실제로 도로에 나오는 시기의 갭을 고려하지 않아서 생긴 오류이다. 
\n **인사이트** : 20세 이하 운전자의 사고 건수가 가장 많은 달은 4월과 7월로, 국내 여행 성수기와 일치한다. 
\n 전 연령대에 동일하게 나타났으므로 해당 시기 자동차보험사 업무 과중을 예상할 수 있다.  
#
"""

@st.cache(allow_output_mutation=True)
def load_time_data():
    age_time = pd.read_csv(
        "https://raw.githubusercontent.com/meji9086/Traffic-Accident-Data-Analysis/master/data/age_times_utf8.csv"
        , encoding='UTF-8')
    return age_time
age_time = load_time_data()

age_time.columns = ["연령", "합계", "시간", "발생건수"]


"""
#### 🚗 운전자 연령별 시간별 교통사고 발생 건수  
\n **가설** : 직장인이 많은 30-40대 운전자들은 출퇴근 시간에 교통사고가 일어났을 것이다.  
"""

# 합계 제외하고 가져오기
age_time_line = age_time.loc[age_time["연령"] != "합계"]

age_area1 = px.area(age_time_line, x="시간", y="발생건수", color='연령', title='운전자 연령별 시간대별 교통사고 발생 건수', 
            width=900, height=700, facet_col="연령", facet_col_wrap=2)
age_area1

"""
**분석 결과** : 가설대로 30-40대 운전자들은 출퇴근 시간에 높은 사고 건수를 기록했다. 
\n 또한 흡사한 그래프 형태를 통해 두 연령대의 운전자들의 생활 시간이 유사함을 알 수 있다.   
#
"""


"""
#### 🚗 20-40대 운전자의 시간별 교통사고 발생 건수 비교  
"""

age_2040_col = (age_time_line["연령"] == "21~30세") | (age_time_line["연령"] == "31~40세") | (age_time_line["연령"] == "41~50세")
age_2040_time = age_time_line[age_2040_col]

age_line5 = px.line(age_2040_time, x="시간", y="발생건수",color="연령", title='20~40대 운전자의 시간대별 교통사고 발생 건수 비교', width=900, height=400, markers=True)
age_line5

"""
**분석 결과** : 30-40대 운전자들뿐만 아니라 20대 운전자도 시간대별 교통사고 발생 건수가 흡사한 양상을 보였다.
\n 오전에는 출근 시간인 8-10시에, 오후에는 퇴근 시간인 18-20시에 피크를 찍는다.
\n 직장에 다니는 주요 경제활동인구라는 공통점을 가지고 있기 때문이다.  
#
"""


"""
#### 🚗 51-60세 운전자와 65세 이상 운전자의 시간별 교통사고 발생 건수 
\n**가설** : 50대 운전자의 수가 많으니 사고량도 더 많겠지만, 사고 발생 시간에는 차이가 없을 것이다.
"""
# 해당 연령대만 잘라오기
age_5060_col = (age_time_line["연령"] == "51~60세") | (age_time_line["연령"] == "61~64세") | (age_time_line["연령"] == "65세이상")
age_5060 = age_time_line[age_5060_col]

age_line6 = px.line(age_5060, x="시간", y="발생건수",color="연령", title='50~60대 운전자의 시간대별 교통사고 발생 건수 비교', width=900, height=400, markers=True)
age_line6

"""
**분석 결과** : 61~64세 운전자보다 65세 이상 운전자의 교통사고 발생 건수가 많다는 점이 눈에 띄는데
\n 연령 범위가 더 넓어서 나타나는 현상일 수 있으므로 유의미한 지표는 아니다.
\n 51-60세, 61-64세 운전자는 20-40대 운전자와 마찬가지로 출퇴근 시간에 높은 사고 건수를 기록했다.
\n 그러나 65세 이상 운전자는 10-12시, 14-16시에 피크를 찍어, 출퇴근 시간이 있는 직장인은 아니라고 추측할 수 있다.

\n 실제로 한국의 정년퇴직 나이를 분석한 기사에 따르면
\n 한국인이 '주된 일자리(가장 오랜 기간 일한 일자리)'에서 퇴직하는 연령은 평균 49.3세이다. 
\n 이들 대부분이 퇴직 후에도 경제 및 사회활동 지속을 위해 재취업을 원하지만
\n 65세 이상은 9-6 정규직 형태의 취업은 잘 이뤄지지 않음을 확인할 수 있다.  
#
\n 기사 출처 : https://www.donga.com/news/Economy/article/all/20220309/112238197/1  
\n 기사 출처 : http://www.seniorsinmun.com/news/articleView.html?idxno=44364  
#
"""

"""
##### 🚗 전 연령 운전자의 월별 교통사고 발생 건수 
"""
age_line0 = px.line(age_month, x="월", y="발생건수",color="연령", 
                    title='전 연령 운전자의 월별 교통사고 발생 건수', width=900, height=400, markers=True)
age_line0

""" 
#### 결론
\n 운전자 연령이 교통사고 발생에 미치는 영향은 예상했던 것보다 크지 않았다.
\n 대부분의 분석에서 연령이 아닌 외부 변수(차량 이용이 많은 특정 시기, 운전자의 생활 시간, 사회활동 여부 등)의 영향이 컸다. 
\n 이 외에도 교통사고 가해자 연령별 요일 / 법규위반 / 사고유형 / 기상별  
\n 교통사고 발생 건수를 분석했지만 유의미한 결과가 나오지 않아 생략했다.  
#
\n ###### 그러나 연령이 교통사고 발생 특성이 되지 않는다는 점에서
\n ###### 연령별 교통사고 가해 운전자 수를 랜덤 샘플링한 연령별 운전자 수 대신 활용할 수 있다.  
#
"""
