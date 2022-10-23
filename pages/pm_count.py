import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import koreanize_matplotlib
import streamlit as st


st.set_page_config(
    page_title="개인형이동수단 교통사고 🛴",
    page_icon="🛴",
    layout="wide",
)
st.markdown("### 개인형이동수단 교통사고 🛴")
st.markdown("""**가설** : 법이 개정된 _5월 이후 '개인 이동형 수단사고(전동킥보드)' 가 이전보다 상대적으로 줄었을 것_ 이다.\n
**예상 결과물** : 2021년의 5월 이후로는 ‘개인 이동형 수단(전동킥보드)’ 으로 발생하는 _사고는 줄어듬_ 을 확인""")

st.sidebar.markdown("# 개인형이동수단 교통사고 🛴")

car_kind = "https://raw.githubusercontent.com/meji9086/Traffic-Accident-Data-Analysis/master/data/car_kind.csv"
car_region = "https://raw.githubusercontent.com/meji9086/Traffic-Accident-Data-Analysis/master/data/car_region.csv"

@st.cache
def load_month(car_kind):
       df = pd.read_csv(car_kind, index_col=0, encoding='utf-8')
       df = df.T
       df = df.reset_index()
       return df

def load_region(car_region):
       df_region = pd.read_csv(car_region, encoding='utf-8')
       df_region_rename = df_region.rename(columns=df_region.iloc[0])
       df_region = df_region_rename.drop(index=0)
       df_region = df_region.replace("-", 0)
       df_region = df_region.reset_index(drop=True)

       return df_region       
df = load_month(car_kind)
df_region = load_region(car_region)

# 컬럼이름변경
df = df.rename(columns={"index":"월별"})
df = df.rename(columns={"이륜차(AVT포함)":"이륜차"})
df = df.rename(columns={"개인형이동수단(PM)":"개인형이동수단"})
df.columns.name = None

# 월별의 '01_사고건수' 를 언더바(_)를 기준으로 split
# '월' 컬럼과 '사고유형' 컬럼을 생성하여 각각 의 값을 넣어줌
df["월별"][0] = "차종_차종"
df["월"] = [df["월별"].str.split("_")[x][0] for x in range(len(df["월별"]))]
df["사고유형"] = [df["월별"].str.split("_")[x][1][:2] for x in range(len(df["월별"]))]
df = df.drop(columns=["월별"])


df["월"][0] = "월"
df["사고유형"][0] = "사고유형"

col = df.columns.to_list()
col1 = df.loc[0].to_list()
df.columns = [col, col1]
df.columns = df.columns.droplevel(0)
df = df.drop(index=0)
df = df.rename(columns={"개인형이동수단(PM)":"개인형이동수단"})

# 각 유형별로 변수할당하여 묶어줌
df_accident = df[df["사고유형"].isin(["사고"])].sort_values(["월"])
df_injury = df[df["사고유형"].isin(["부상"])].sort_values(["월"])
df_death = df[df["사고유형"].isin(["사망"])].sort_values(["월"])

df_copy = df.copy()
df_copy = df_copy.set_index("월")
df_copy = df_copy[["개인형이동수단"]]
df_copy_accident = df_copy.iloc[:12].sort_values(["월"]).T
df_copy_injury = df_copy.iloc[12:24].sort_values(["월"])
df_copy_death = df_copy.iloc[24:].sort_values(["월"])
# seoul = seoul.astype("int")

seoul = df_region.iloc[:31]
gg_n = df_region.iloc[31:63]
gg_e = df_region.iloc[64:]
seoul["사고건수"] = seoul["사고건수"].astype("int")
gg_n["사고건수"] = gg_n["사고건수"].astype("int")
gg_e["사고건수"] = gg_e["사고건수"].astype("int")



# plt.figure(figsize=(12, 5)) 
fig, ax = plt.subplots(figsize=(10, 5))
plt.axhline(166, color='#4374D9', linewidth=0.5, linestyle='dotted')
plt.axvline(4, color='#4374D9', linewidth=0.5, linestyle='dotted')
sns.barplot(data=df_accident, x="월", y="개인형이동수단", color="#FFD8D8").set(title="\n월별 개인형이동수단 사고건수\n")
st.pyplot(fig)
# df_copy_accident


st.markdown("""
법이 개정된 5월을 기준으로 확인해보면, **법이 적용되고 5개월간은 사고수가 줄지 않았다**. \n
기사를 확인해보면 이전에는 사용자가 적정선을 유지하고 있었으나 최근에 공유모빌리티가 많이 등장하고
이용이 편리하다보니 _전동킥보드 사용자가 급증_ 하고 있는 추세이다. \n
**이용자가 증가한만큼 사고수가 줄어들지 않은것으로 보이며**, 기상의 조건으로 11월과 12월에는 이용자가 적어 사고수가 적은것으로 보인다. \n
~~개인형이동수단 관련 이용자 데이터를 비교하고 싶었는데, 구매해야하는 데이터여서 확인을 못함 😭😭😭~~ \n
**+ 전동킥보드 이용자 증가 관련뉴스**\n
- http://daenews.co.kr/news/view.php?no=16524 \n
- https://it.donga.com/32544/\n
""")

df_count = pd.concat([df_death, df_injury])

fig2, ax = plt.subplots(figsize=(10, 3))
sns.pointplot(data=df_count, x="월", y="개인형이동수단", hue="사고유형",
             markers="X",scale=0.5).set(title="\n월별 개인형이동수단 사망자 및 부상자\n")
plt.axvline(4, color='#4374D9', linewidth=0.5, linestyle='dotted')
plt.axhline(186, color='#4374D9', linewidth=0.5, linestyle='dotted')
plt.axhline(0, color='black', linewidth=0.5, linestyle='dotted')
st.pyplot(fig2)

# df_copy_injury = df_copy_injury.rename(columns={"개인형이동수단":"부상자수"})
# df_copy_death = df_copy_death.rename(columns={"개인형이동수단":"사망자수"})
# df_copy_con = pd.concat([df_copy_death, df_copy_injury], axis=1).T
# df_copy_con
st.markdown("""
월별 개인형이동수단을 이용하면서 부상자 역시 법시행 후 한달정도는 부상자가 줄어드는듯 보이나, \n
사고건수 그래프와 동일하게 부상자도 겨울이전에는 늘어나는것으로 보인다.
사망자 역시 기존에 1~2명 발생하다가, 이용자 수가 늘어남과 같이 사망자수도 조금씩 늘어났다. \n
\n""")


fig3, ax = plt.subplots(figsize=(10, 4))
# plt.figure(figsize=(12, 5))
plt.xticks(rotation= 45)
plt.axhline(14, color='black', linewidth=0.5, linestyle='dotted')
sns.pointplot(data=seoul,x="경찰청세분류",y="사고건수",markers="X",scale=0.5).set(title="\n월별 서울 개인형이동수단 사고건수\n")
st.pyplot(fig3)

df_seoul = seoul[["경찰청세분류","사고건수"]]
df_seoul = df_seoul.set_index("경찰청세분류")
df_seoul = df_seoul.T
df_seoul

st.markdown("""
서울에서 발생하는 전동킥보드 사고건수는 평균적으로 14건이며, 주로 **마포,강남,송파** 에서 사고가 많이 발생하고 있다.
""")

fig4, ax = plt.subplots(figsize=(10, 5))
plt.xticks(rotation= 45)
plt.grid(True, axis='x')
plt.axhline(13, color='black', linewidth=0.5, linestyle='dotted')
sns.pointplot(data=gg_n,x="경찰청세분류",y="사고건수",markers="X",scale=0.5).set(title="\n월별 경기남부 개인형이동수단 사고건수\n")
st.pyplot(fig4)
df_gg_n = gg_n[["경찰청세분류","사고건수"]]
df_gg_n = df_gg_n.set_index("경찰청세분류")
df_gg_n = df_gg_n.T
df_gg_n
st.markdown("""
경기 남부에서는 평택, 시흥이 주로 많이 발생하고 있으며, 다른 지역은 평균을 웃돌고 있다.
""")
# seoul_des = pd.DataFrame(seoul.describe())
# seoul_des
fig5, ax = plt.subplots(figsize=(10, 5))
plt.xticks(rotation= 45)
plt.grid(True, axis='x')
plt.axhline(6, color='black', linewidth=0.5, linestyle='dotted')
sns.pointplot(data=gg_e,x="경찰청세분류",y="사고건수",markers="X",scale=0.5).set(title="\n월별 경기북부 개인형이동수단 사고건수\n")
st.pyplot(fig5)
df_gg_e = gg_e[["경찰청세분류","사고건수"]]
df_gg_e = df_gg_e.set_index("경찰청세분류")
df_gg_e = df_gg_e.T
df_gg_e
st.markdown("""
경기 북부같은 경우는 주로 인구가 많은 일산에서 많이 발생하고 있습니다.
""")

st.markdown("사용한 데이터 : 가해자 법규 위반 별 주야 별 교통사고 데이터 ( 출처 : [http://taas.koroad.or.kr/index.jsp](http://taas.koroad.or.kr/index.jsp) )")

