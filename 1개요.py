import streamlit as st
import pandas as pd
from PIL import Image



st.set_page_config(
    page_title="Traffic Accident Data Analysis",
    page_icon="🚗",
    layout="wide",
)

st.header("🔥 핫식스 6조")
st.markdown("""
    **🦁 Likelion AI SCHOOL7 Mid Project**           
    이영빈, 정세리, 손진선, 김예지, 김준모, 이선오
""")

st.markdown("---")

st.markdown("""
    # 교통사고는 왜 일어날까?🚗🤷‍♀️  
""")

image = Image.open('pages/images/traffic1.png')
st.image(image)

st.markdown("""
    대형 화물차부터 개인형 이동수단(PM)까지 다양한 이동 수단이  등장하며 관련 법이 제정되고 있지만, 교통사고의 다양화를 막을 수는 없었습니다.                
    사고 현장의 블랙박스만 전문으로 다루는 변호사 유튜버까지 등장할 정도로 교통사고는 핫한 이슈입니다.           
    **교통사고가 어디서 어떻게 왜 발생하는지, 그 답을 찾기 위해 데이터 분석 프로젝트를 진행**해보았다습니다.             
""")

st.markdown("""
    ## 🗃️ 활용 데이터 정보   
    도로교통공단 TAAS : [http://taas.koroad.or.kr/sta/acs/exs/typical.do?menuId=WEB_KMP_OVT_UAS_ASA#](http://taas.koroad.or.kr/sta/acs/exs/typical.do?menuId=WEB_KMP_OVT_UAS_ASA#)            
    공공데이터포털 : [https://www.data.go.kr/index.do](https://www.data.go.kr/index.do)
""")

st.markdown("---")

st.markdown("""
    ## 🔍 활용 데이터셋
""")

def main():
    if st.checkbox('월/요일/시간별 교통사고 데이터'):
        st.subheader('월/요일/시간별 교통사고 데이터')
        df = pd.read_csv('data/통계청_요일별_시간대별_교통사고.csv')
        st.dataframe(df)
    
    if st.checkbox('가해자 연령별 교통사고 데이터'):
        st.subheader('가해자 연령별 교통사고 데이터')
        df2 = pd.read_csv('data/통계청_가해자_연령층별_사고.csv')
        st.dataframe(df2)

    if st.checkbox('사고유형별 교통사고 데이터'):
        st.subheader('사고유형별 교통사고 데이터')
        df3 = pd.read_csv('data/사고유형별_월별_교통사고.csv')
        st.dataframe(df3)

    if st.checkbox('차종별 교통사고 데이터'):
        st.subheader('차종별 교통사고 데이터')
        df4 = pd.read_csv('data/가해운전자_차종별_월별_교통사고.csv')
        st.dataframe(df4)  

    if st.checkbox('도로종류별 교통사고 데이터'):
        st.subheader('도로종류별 시간별 데이터')
        df5 = pd.read_csv('data/도로종류별 시간별 교통사고 data.csv')
        st.dataframe(df5)    

    if st.checkbox('도로형태별 교통사고 데이터'):
        st.subheader('도로형태별 교통사고 데이터')
        df6 = pd.read_csv('data/도로형태별 시간별 교통사고 data.csv')
        st.dataframe(df6)     

    if st.checkbox('법규위반별 교통사고 데이터'):
        st.subheader('법규위반별 교통사고 데이터')
        df7 = pd.read_csv('data/통계청_가해자_법규위반별_주야별_교통사고.csv')
        st.dataframe(df7)     


if __name__ == "__main__" :
    main()

st.markdown("---")

st.markdown("""
    ## 👩‍👩‍👧‍👦 역할
""")

role = pd.DataFrame({
    '이름' : ['이영빈', '정세리', '손진선', '김예지', '김준모', '이선오'],
    '역할' : ['사고유형별 교통사고 데이터 전처리 및 시각화, PPT 제작',
    '차종별 교통사고 데이터 전처리 및 시각화, PPT 제작',
    '월/요일/시간별 교통사고 데이터 전처리 및 시각화, PPT 제작',
    '법규위반별 교통사고 데이터 전처리 및 시각화, streamlit 메인 페이지 작성',
    '도로형태별 교통사고 데이터 전처리 및 시각화, streamlit 메인 페이지 작성',
    '가해자 연령별 교통사고 데이터 전처리 및 시각화, 노션 작성, PPT 발표']
}, index=[1,2,3,4,5,6])
role


st.sidebar.header('🚗 교통사고 원인 분석 🚗')
st.sidebar.markdown("""
    ### 🥕 목차
    1. 주제선정이유
    2. 데이터 소개
    3. 역할

    ### ☘ 홈페이지
    github : [https://github.com/meji9086/Traffic-Accident-Data-Analysis](https://github.com/meji9086/Traffic-Accident-Data-Analysis)
""")