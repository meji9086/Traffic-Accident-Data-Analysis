import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="Traffic Accident Data Analysis Results",
    page_icon="🚗",
    layout="wide",
)

st.header("⚡교통사고 발생 원인 분석 결과 키워드⚡")


image1 = Image.open('pages/images/traffic2.png')
st.image(image1)

keyword = ['휴가철', '가을', '금요일', '퇴근시간', '교차로', '노인']
st.multiselect('교통사고 발생 원인 분석 결과 키워드', keyword, keyword)

st.markdown("---")

st.markdown("""
    # 📊 분석 결과
     
    EDA를 마치고 각자 분석한 내용을 다 함께 확인하는 과정에서 생각지 못한 키워드가 등장했습니다.          
    바로 **휴가철, 가을, 금요일, 퇴근 시간, 교차로, 노인**입니다. 
    이 키워드를 중심으로 분석 결과를 정리해보았습니다.          
""")

st.markdown("---")

st.markdown("""    
    ### 1. 휴가철, 출퇴근 시간처럼 교통량이 증가함에 따라 사고율이 증가한다.          
""")

tab1, tab2, tab3 = st.tabs(["월별", "시간별", "요일별"])

tab1.subheader("월별 사고건수")
image2 = Image.open('pages/images/traffic3_month.png')
tab1.image(image2)

tab2.subheader("시간별 사고건수")
image3 = Image.open('pages/images/traffic4_time.png')
tab2.image(image3)

tab3.subheader("요일별 사고건수")
image4 = Image.open('pages/images/traffic5_weekday.png')
tab3.image(image4)


st.markdown("""
  ##### 월/요일/시간대별 교통사고 발생 건수 데이터를 시각화하여 분석한 결과                     
  ✅ **월/요일/시간대별 분석 결과**
     -월로는 10월, 요일로는 금요일, 시간으로는 오후 6시-8시에 가장 많은 사고가 발생     
  
  ✅ **차이 발생 이유**         
     - 휴가철인 7월과 2021년 10월 1차 접종률 70% 달성으로 인한 10월,11월에 교통량이 증가                               
     - 직장인들의 퇴근시간인 오후 6시 ~ 8시에 가장 많은 사고가 발생       
     - 주말동안의 시간을 이용하여 여행, 휴식등의 여가생활을 즐기기 위한 유동인구가 가장 많은 금요일에 가장 많은 사고가 발생                    
     
  ✅ **시사점**          
     - 2021년은 코로나로 인한 이동율 차이 증가                      
     - 교통량이 많을 때 사고를 줄이기 우위한 대책이 필요            
""")

st.markdown("")

st.markdown("""
    #### 해결 방안 제시
    1. 운전자와 보행자의 교통 인식 교육, 도로 상황이나 제도 개선이 필요하다.       
    2. 휴가철과 출퇴근 시간에 도로 통행 관리 인력을 늘린다.           
""")

st.markdown("---")

st.markdown("""
    ### 2. 법 개정으로는 교통사고 증가를 막기 어려웠다.       
""")

tab4, tab5, tab6, tab7 = st.tabs(["개인형 이동수단", "사고유형", "도로형태", "법규위반"])

tab4.subheader("전동킥보드 사고건수")
image5 = Image.open('pages/images/traffic6_pm.png')
tab4.image(image5)

tab5.subheader("사고유형별 교통사고 ")
image6 = Image.open('pages/images/traffic7_accident.png')
tab5.image(image6)

tab6.subheader("도로형태별 사고건수")
image7 = Image.open('pages/images/traffic8_road.png')
tab6.image(image7)

tab7.subheader("법규위반별 사고건수")
image8 = Image.open('pages/images/traffic9_violation.png')
tab7.image(image8)


st.markdown("""
  ##### 개인형 이동수단, 사고유형, 도로종류, 법규위반 데이터를 시각화하여 분석한 결과               
  ✅ **개인형 이동수단**                      
     - 공유 킥보드 회사 ‘씽씽’의 자사 데이터 분석에 따르면 계절별 이용량은 여름 36.0%, 가을 29.1%, 봄 22.9%, 겨울 12.0% 순으로 개인형 이동 수단 역시 이용량과 사고 발생량이 비례함
     - 공유 킥보드 회사 ‘라임’의 서울 지역 운행 데이터에서 평일 오전 8시 ~ 10시, 오후 6시 ~ 8시 이용량이 전체의 약 34.8%를 차지
     - 2021년 5월 개인형 이동 수단(전동킥보드)과 관련된 도로교통법이 개정되어 이후 감소했을 것이라 예상하였지만, 법 개정 이후에도 사고는 증가              
 
  ✅ **사고유형**           
     - 차와 사람 사이에서 발생한 교통사고는 횡단 보도가 아닌 길 가장자리 구역 통행 중에 가장 많이 일어남을 확인                    
     - 2022년 4월 20일부터 개정 도로교통법 시행으로 보행자의 통행 우선권이 보장 및 확대가 되었으나 규제만으로는 보행자 보호가 충분하지 않음         
 
  ✅ **도로종류**           
     - 도로 형태 별 교통사고 발생 건수 분석한 결과 교차로 내에서 가장 많은 사고가 발생         
     - 교차로에 대한 교통 통제 및 관리가 되고 있지 않음       
 
  ✅ **법규위반**                 
     - 법규 위반별 사고 건수 분석에서 교차로 운행 방법 위반은 신호 위반, 안전 거리 미확보에 이어 3위를 차지
     - 신호 위반, 안전거리 미확보, 교차로와 관련된 법 개정이 필요
""")

st.markdown("")

st.markdown("""
    #### 해결 방안 제시
    1. 관련 법과 제도 뿐만 아니라 실질적인 대책을 마련한다. 
    2. 강화한 내용을 홍보해 인식을 강화한다.
""")

st.markdown("---")

st.markdown("""
    ## 3. 노인은 교통사고의 피해자일 뿐 아니라 가해자가 될 수 있다.          
""")

# 연령시각화
tab8,tab9 = st.tabs(["50~60대","연령별"])
tab8.subheader("50~60대 사고건수")
image9 = Image.open('pages/images/traffic10_age.jpeg')
tab8.image(image9)

tab9.subheader("연령별 사고건수")
image10= Image.open('pages/images/traffic11_age2.png')
tab9.image(image10)


st.markdown("""
  ✅ **연령별 분석결과**                 
     - 51세에서 64세 운전자는 다른 연령대와 동일하게 출퇴근 시간에 사고가 가장 많음            
     - 65세 이상의 운전자의 경우 오전 **10시 ~ 12시, 오후 2시 ~ 4시**에 가장 사고가 많음               
     
  ✅ **차이 발생 이유**         
     - 퇴직연령과 관련있는것으로 확인되었다. **비자발적 조기 퇴직으로 65세 이상의 운전자 생활 시간이 달라졌다.**                               
     - 9 to 6에서 멀어진 65세 이상 고령 노동자의 19.7%는 운송업에 종사해, 운전과 생계가 연결                       
     - 정부가 고령 운전자 교통사고 감소를 목표로 운전면허 자진 반납 및 지원금 제도를 운영하고 있음에도 참여가 저조한 이유                    
     
  ✅ **시사점**          
     - 한국은 2025년 고령 인구가 20.3%에 달해 초고령 사회로 진입             
     - **고령 보행자 보호와 더불어, 고령 운전자의 교통사고 감소를 위해 실질적인 대책 마련이 필요함을 이번 프로젝트를 통해 파악할 수 있었다.**                   
""")

st.markdown("")

st.markdown("""
    #### 해결 방안 제시
    1. 운전면허 갱신 주기 단축 및 교통 안전 교육을 시행한다.
    2. 특정 연령 이상 운전자의 신체검사를 강화한다.

""")

st.sidebar.header('🚗 교통사고 원인 분석 결과 🚗')
st.sidebar.markdown("""
    ### 🥕 목차
    1. 키워드
    2. 분석결과 
     - 교통랑의 증가로 인한 사고 증가
     - 법개정으로는 사고를 막기 어려움
     - 노인은 교통피해자, 가해자도 된다.

    ### ☘ 홈페이지
    github : [https://github.com/meji9086/Traffic-Accident-Data-Analysis](https://github.com/meji9086/Traffic-Accident-Data-Analysis)
""")