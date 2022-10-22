import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import koreanize_matplotlib

st.set_page_config(
    page_title="Aanlysis of traffic accident",
    page_icon="🚗",
    layout="wide",
)

st.title("⏱ 월/요일/시간대별")

url = "https://raw.githubusercontent.com/meji9086/Traffic-Accident-Data-Analysis/master/data/time_zones.csv"

@st.cache
def load_data():
    df = pd.read_csv(url, encoding="cp949", index_col=0)
    return df


st.markdown("")
st.markdown("")

df = load_data()



# <sidebar>

# 월
st.sidebar.header('📌 User Input Features')
selected_month = st.sidebar.multiselect("✔ 월", df["월"].unique(), df["월"].unique())

# 요일
selected_day = st.sidebar.multiselect("✔ 요일", df["요일"].unique(), df["요일"].unique())

# 시간대
selected_time1 = st.sidebar.multiselect("✔ 시간대", df["시간대"].unique(), df["시간대"].unique())


# 월
if len(selected_month) > 0:
    df = df[df["월"].isin(selected_month)]

# 요일
if len(selected_day) > 0:
    df = df[df["요일"].isin(selected_day)]

# 시간대
if len(selected_time1) > 0:
    df = df[df["시간대"].isin(selected_time1)]


st.subheader("🚗 2021년 교통사고 데이터 🚗")
st.markdown("")

st.subheader("📍 DataFrame")
st.dataframe(df)

st.markdown("---")
st.markdown("")



df = load_data()


# <월별>
st.subheader("✔ 월별")

st.markdown("")
st.markdown('''**🔍 가설**
- **여름 휴가철, `07월` ~ `08월`과 가을 행락철, `10월` ~ `11월`의 사고 건수가 많을 것이다.**''')

df1 = df.loc[df["사고유형"] == "사고건수", ["월", "건수"]].groupby("월").sum()

tab1, tab2 = st.tabs(["📈 Chart", "🔒 Data"])

plt.figure(figsize=(20, 7))
sns.barplot(data=df1, x=df1.index, y="건수", ci=None)
sns.pointplot(data=df1, x=df1.index, y="건수", ci=None)
plt.axhline(df1["건수"].mean(), c="r", lw=1, ls="--")
tab1.markdown("**월별 사고 건수**")
tab1.pyplot(plt)

tab2.markdown("**월별 사고 건수**")
tab2.dataframe(df1.style.highlight_max(axis=0))

st.markdown("")
st.info(''' - 08월은 평균 사고 건수에도 미치지 못하고 있다.   
- 가장 많이 발생한 달은 10월이고, 11월, 07월 그 뒤를 잇달고 있다.
- 가장 적게 발생한 달은 02월로 나타났다.''')

st.markdown("")
st.markdown("---")
st.markdown("")


# <요일별>
st.subheader("✔ 요일별")

st.markdown("")
st.markdown('''**🔍 가설**
- **출퇴근을 하는 `평일`이 주말보다 사고가 많이 발생할 것이다.**
- **평일 중에서도 `금요일`에 사고가 가장 많이 발생할 것이다.**''')

day_of_week = list("월화수목금토일")
df2 = df.loc[df["사고유형"] == "사고건수", ["요일", "건수"]].groupby("요일").sum().reindex(day_of_week)

tab1, tab2 = st.tabs(["📈 Chart", "🔒 Data"])

plt.figure(figsize=(20, 7))
sns.barplot(data=df2, x=df2.index, y="건수", palette="husl", ci=None)
sns.pointplot(data=df2, x=df2.index, y="건수", ci=None)
plt.axhline(df2["건수"].mean(), c="r", lw=1, ls="--")
tab1.markdown("**요일별 사고 건수**")
tab1.pyplot(plt)

tab2.markdown("**요일별 사고 건수**")
tab2.dataframe(df2.style.highlight_max(axis=0))

st.markdown("")
st.info(''' - 토요일과 일요일은 평균에 밑도는 것으로 나타났다.  
- 금요일에 가장 많이 발생하고, 일요일에 가장 적게 발생하는 것으로 나타났다.''')

st.markdown("")
st.markdown("")

df3 = df.loc[df["사고유형"] == "사고건수", ["평일/주말", "건수"]].groupby("평일/주말").mean().reindex(["평일", "주말"])

tab1, tab2 = st.tabs(["📈 Chart", "🔒 Data"])

plt.figure(figsize=(20, 7))
sns.barplot(data=df3, x=df3.index, y="건수", palette="husl", order=["평일", "주말"], ci=None)
plt.axhline(df3["건수"].mean(), c="r", lw=1, ls="--")
tab1.markdown("**평일/주말 사고 발생 평균**")
tab1.pyplot(plt)

tab2.markdown("**평일/주말 사고 발생 평균**")
tab2.dataframe(df3.style.highlight_max(axis=0))

st.markdown("")
st.info(''' - 평일이 주말보다 더 많이 발생한 것으로 나타났다.''')


st.markdown("")
st.markdown("---")
st.markdown("")


# <시간대별>
st.subheader("✔ 시간대별")

st.markdown("")
st.markdown('''**🔍 가설**
- **퇴근 시간인 `18 ~ 20시`의 사고 건수가 가장 많을 것이다.**
- **오전보다 이동량이 많은 `오후`에 사고 건수가 더 많을 것이다.**
- **주간보다 `야간`에 사고 건수가 더 많을 것이다.**''')
st.caption('''- 주간 : 08 ~ 18시
- 야간 : 18 ~ 08시''')
st.markdown("")

df4 = df.loc[df["사고유형"] == "사고건수", ["시간대", "건수"]].groupby("시간대").sum()

tab1, tab2 = st.tabs(["📈 Chart", "🔒 Data"])

plt.figure(figsize=(20, 7))
sns.barplot(data=df4, x=df4.index, y="건수", ci=None)
sns.pointplot(data=df4, x=df4.index, y="건수", ci=None)
plt.axhline(df4["건수"].mean(), c="r", lw=1, ls="--")
tab1.markdown("**시간대별 사고 건수**")
tab1.pyplot(plt)

tab2.markdown("**시간대별 사고 건수**")
tab2.dataframe(df4.style.highlight_max(axis=0))

st.markdown("")
st.info(''' - 02 ~ 04시의 사고 건수가 가장 적고, 18 ~ 20시 사고 건수가 가장 많은 것으로 나타났다.
- 02시부터 20시까지 사고 건수가 점차 증가하고 있는 것으로 나타났다.
- 22시부터 08시까지 사고 건수가 평균에 밑도는 것으로 나타났다.''')

st.markdown("")
st.markdown("")

df5 = df.loc[df["사고유형"] == "사고건수", ["오전/오후", "건수"]].groupby("오전/오후").sum()

tab1, tab2 = st.tabs(["📈 Chart", "🔒 Data"])

plt.figure(figsize=(20, 7))
sns.barplot(data=df5, x=df5.index, y="건수", palette="husl", ci=None)
plt.axhline(df5["건수"].mean(), c="r", lw=1, ls="--");
tab1.markdown("**오전/오후 사고 발생 건수**")
tab1.pyplot(plt)

tab2.markdown("**오전/오후 사고 발생 건수**")
tab2.dataframe(df5.style.highlight_max(axis=0))

st.markdown("")
st.info(''' - 오전보다 오후에 더 많이 발생한 것으로 나타났다.''')



st.markdown("")
st.markdown("")

df6 = df.loc[df["사고유형"] == "사고건수", ["주간/야간", "건수"]].groupby("주간/야간").mean().reindex(["주간", '야간'])

tab1, tab2 = st.tabs(["📈 Chart", "🔒 Data"])

plt.figure(figsize=(20, 7))
sns.barplot(data=df6, x=df6.index, y="건수", palette="husl", ci=None)
plt.axhline(df6["건수"].mean(), c="r", lw=1, ls="--")
tab1.markdown("**주간/야간 사고 발생 평균**")
tab1.pyplot(plt)

tab2.markdown("**주간/야간 사고 발생 평균**")
tab2.dataframe(df6.style.highlight_max(axis=0))

st.markdown("")
st.info(''' - 야간보다 주간에 더 많이 발생한 것으로 나타났다.''')

st.markdown("")
st.markdown("---")
st.markdown("")


# <범주별 영향>
st.subheader("✔ 범주별 영향")
st.markdown("")
tab1, tab2, tab3 = st.tabs(["📈 Chart1", "📈 Chart2", "📈 Chart3"])

pv1 = df.pivot_table(index="요일", columns="월", values="건수")
pv1 = pv1.reindex(index=list("월화수목금토일"))

plt.figure(figsize=(15, 10))
sns.heatmap(pv1, annot=True, fmt=".2f", cmap="flare")
tab1.markdown("**월/요일에 따른 사고 발생 평균**")
tab1.pyplot(plt)


pv2 = df.pivot_table(index="시간대", columns="요일", values="건수")
pv2 = pv2.reindex(columns=list("월화수목금토일"))

plt.figure(figsize=(15, 10))
sns.heatmap(pv2, annot=True, fmt=".2f", cmap="flare")
tab2.markdown("**요일/시간대에 따른 사고 발생 평균**")
tab2.pyplot(plt)


pv3 = df.pivot_table(index="시간대", columns="월", values="건수")

plt.figure(figsize=(15, 10))
sns.heatmap(pv3, annot=True, fmt=".2f", cmap="flare");
tab3.markdown("**월/시간대에 따른 사고 발생 평균**")
tab3.pyplot(plt)




st.markdown("")
st.markdown("---")
st.markdown("")


# <결론>
st.subheader("✔ 결론")

st.markdown("")
st.success(''' - 교통사고는 **가을 행락철**에 가장 많이 발생한다.
- 요일을 기준으로 **평일**, 그중에서도 **금요일**에 사고가 많이 발생한다.
- 시간을 기준으로 **오후**, 그중에서도 퇴근시간인 **18시-20시**에 사고가 많이 발생한다.
- 차량 이동이 많은 시점과 사고 건수가 비례한 것을 파악할 수 있다.''')

st.markdown("")
st.markdown("")
st.caption("사용한 데이터 : [도로교통공단_TAAS] - 요일별 시간대별 교통사고 (http://taas.koroad.or.kr/)")

st.markdown("")
st.markdown("")
st.caption(''' <참조 기사>
- http://www.wonjutoday.co.kr/news/articleView.html?idxno=127301
- https://m.khan.co.kr/national/national-general/article/202110011213001#c2b
- http://www.nspna.com/news/?mode=view&newsid=598721
- https://www.safetynews.co.kr/news/articleView.html?idxno=213458''')