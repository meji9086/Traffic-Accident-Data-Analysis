import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="Traffic Accident Data Analysis Results",
    page_icon="ð",
    layout="wide",
)

st.header("â¡êµíµì¬ê³  ë°ì ìì¸ ë¶ì ê²°ê³¼ í¤ìëâ¡")


image1 = Image.open('pages/images/traffic2.png')
st.image(image1)

keyword = ['í´ê°ì² ', 'ê°ì', 'ê¸ìì¼', 'í´ê·¼ìê°', 'êµì°¨ë¡', 'ë¸ì¸']
st.multiselect('êµíµì¬ê³  ë°ì ìì¸ ë¶ì ê²°ê³¼ í¤ìë', keyword, keyword)

st.markdown("---")

st.markdown("""
    # ð ë¶ì ê²°ê³¼
     
    EDAë¥¼ ë§ì¹ê³  ê°ì ë¶ìí ë´ì©ì ë¤ í¨ê» íì¸íë ê³¼ì ìì ìê°ì§ ëª»í í¤ìëê° ë±ì¥íìµëë¤.          
    ë°ë¡ **í´ê°ì² , ê°ì, ê¸ìì¼, í´ê·¼ ìê°, êµì°¨ë¡, ë¸ì¸**ìëë¤. 
    ì´ í¤ìëë¥¼ ì¤ì¬ì¼ë¡ ë¶ì ê²°ê³¼ë¥¼ ì ë¦¬í´ë³´ììµëë¤.          
""")

st.markdown("---")

st.markdown("""    
    ### 1. í´ê°ì² , ì¶í´ê·¼ ìê°ì²ë¼ êµíµëì´ ì¦ê°í¨ì ë°ë¼ ì¬ê³ ì¨ì´ ì¦ê°íë¤.          
""")

tab1, tab2, tab3 = st.tabs(["ìë³", "ìê°ë³", "ìì¼ë³"])

tab1.subheader("ìë³ ì¬ê³ ê±´ì")
image2 = Image.open('pages/images/traffic3_month.png')
tab1.image(image2)

tab2.subheader("ìê°ë³ ì¬ê³ ê±´ì")
image3 = Image.open('pages/images/traffic4_time.png')
tab2.image(image3)

tab3.subheader("ìì¼ë³ ì¬ê³ ê±´ì")
image4 = Image.open('pages/images/traffic5_weekday.png')
tab3.image(image4)


st.markdown("""
  ##### ì/ìì¼/ìê°ëë³ êµíµì¬ê³  ë°ì ê±´ì ë°ì´í°ë¥¼ ìê°ííì¬ ë¶ìí ê²°ê³¼                     
  â **ì/ìì¼/ìê°ëë³ ë¶ì ê²°ê³¼**
     -ìë¡ë 10ì, ìì¼ë¡ë ê¸ìì¼, ìê°ì¼ë¡ë ì¤í 6ì-8ìì ê°ì¥ ë§ì ì¬ê³ ê° ë°ì     
  
  â **ì°¨ì´ ë°ì ì´ì **         
     - í´ê°ì² ì¸ 7ìê³¼ 2021ë 10ì 1ì°¨ ì ì¢ë¥  70% ë¬ì±ì¼ë¡ ì¸í 10ì,11ìì êµíµëì´ ì¦ê°                               
     - ì§ì¥ì¸ë¤ì í´ê·¼ìê°ì¸ ì¤í 6ì ~ 8ìì ê°ì¥ ë§ì ì¬ê³ ê° ë°ì       
     - ì£¼ë§ëìì ìê°ì ì´ì©íì¬ ì¬í, í´ìë±ì ì¬ê°ìíì ì¦ê¸°ê¸° ìí ì ëì¸êµ¬ê° ê°ì¥ ë§ì ê¸ìì¼ì ê°ì¥ ë§ì ì¬ê³ ê° ë°ì                    
     
  â **ìì¬ì **          
     - 2021ëì ì½ë¡ëë¡ ì¸í ì´ëì¨ ì°¨ì´ ì¦ê°                      
     - êµíµëì´ ë§ì ë ì¬ê³ ë¥¼ ì¤ì´ê¸° ì°ìí ëì±ì´ íì            
""")

st.markdown("")

st.markdown("""
    #### í´ê²° ë°©ì ì ì
    1. ì´ì ìì ë³´íìì êµíµ ì¸ì êµì¡, ëë¡ ìí©ì´ë ì ë ê°ì ì´ íìíë¤.       
    2. í´ê°ì² ê³¼ ì¶í´ê·¼ ìê°ì ëë¡ íµí ê´ë¦¬ ì¸ë ¥ì ëë¦°ë¤.           
""")

st.markdown("---")

st.markdown("""
    ### 2. ë² ê°ì ì¼ë¡ë êµíµì¬ê³  ì¦ê°ë¥¼ ë§ê¸° ì´ë ¤ì ë¤.       
""")

tab4, tab5, tab6, tab7 = st.tabs(["ê°ì¸í ì´ëìë¨", "ì¬ê³ ì í", "ëë¡íí", "ë²ê·ìë°"])

tab4.subheader("ì ëí¥ë³´ë ì¬ê³ ê±´ì")
image5 = Image.open('pages/images/traffic6_pm.png')
tab4.image(image5)

tab5.subheader("ì¬ê³ ì íë³ êµíµì¬ê³  ")
image6 = Image.open('pages/images/traffic7_accident.png')
tab5.image(image6)

tab6.subheader("ëë¡ííë³ ì¬ê³ ê±´ì")
image7 = Image.open('pages/images/traffic8_road.png')
tab6.image(image7)

tab7.subheader("ë²ê·ìë°ë³ ì¬ê³ ê±´ì")
image8 = Image.open('pages/images/traffic9_violation.png')
tab7.image(image8)


st.markdown("""
  ##### ê°ì¸í ì´ëìë¨, ì¬ê³ ì í, ëë¡ì¢ë¥, ë²ê·ìë° ë°ì´í°ë¥¼ ìê°ííì¬ ë¶ìí ê²°ê³¼               
  â **ê°ì¸í ì´ëìë¨**                      
     - ê³µì  í¥ë³´ë íì¬ âì½ì½âì ìì¬ ë°ì´í° ë¶ìì ë°ë¥´ë©´ ê³ì ë³ ì´ì©ëì ì¬ë¦ 36.0%, ê°ì 29.1%, ë´ 22.9%, ê²¨ì¸ 12.0% ìì¼ë¡ ê°ì¸í ì´ë ìë¨ ì­ì ì´ì©ëê³¼ ì¬ê³  ë°ìëì´ ë¹ë¡í¨
     - ê³µì  í¥ë³´ë íì¬ âë¼ìâì ìì¸ ì§ì­ ì´í ë°ì´í°ìì íì¼ ì¤ì  8ì ~ 10ì, ì¤í 6ì ~ 8ì ì´ì©ëì´ ì ì²´ì ì½ 34.8%ë¥¼ ì°¨ì§
     - 2021ë 5ì ê°ì¸í ì´ë ìë¨(ì ëí¥ë³´ë)ê³¼ ê´ë ¨ë ëë¡êµíµë²ì´ ê°ì ëì´ ì´í ê°ìíì ê²ì´ë¼ ììíìì§ë§, ë² ê°ì  ì´íìë ì¬ê³ ë ì¦ê°              
 
  â **ì¬ê³ ì í**           
     - ì°¨ì ì¬ë ì¬ì´ìì ë°ìí êµíµì¬ê³ ë í¡ë¨ ë³´ëê° ìë ê¸¸ ê°ì¥ìë¦¬ êµ¬ì­ íµí ì¤ì ê°ì¥ ë§ì´ ì¼ì´ë¨ì íì¸                    
     - 2022ë 4ì 20ì¼ë¶í° ê°ì  ëë¡êµíµë² ìíì¼ë¡ ë³´íìì íµí ì°ì ê¶ì´ ë³´ì¥ ë° íëê° ëìì¼ë ê·ì ë§ì¼ë¡ë ë³´íì ë³´í¸ê° ì¶©ë¶íì§ ìì         
 
  â **ëë¡ì¢ë¥**           
     - ëë¡ íí ë³ êµíµì¬ê³  ë°ì ê±´ì ë¶ìí ê²°ê³¼ êµì°¨ë¡ ë´ìì ê°ì¥ ë§ì ì¬ê³ ê° ë°ì         
     - êµì°¨ë¡ì ëí êµíµ íµì  ë° ê´ë¦¬ê° ëê³  ìì§ ìì       
 
  â **ë²ê·ìë°**                 
     - ë²ê· ìë°ë³ ì¬ê³  ê±´ì ë¶ììì êµì°¨ë¡ ì´í ë°©ë² ìë°ì ì í¸ ìë°, ìì  ê±°ë¦¬ ë¯¸íë³´ì ì´ì´ 3ìë¥¼ ì°¨ì§
     - ì í¸ ìë°, ìì ê±°ë¦¬ ë¯¸íë³´, êµì°¨ë¡ì ê´ë ¨ë ë² ê°ì ì´ íì
""")

st.markdown("")

st.markdown("""
    #### í´ê²° ë°©ì ì ì
    1. ê´ë ¨ ë²ê³¼ ì ë ë¿ë§ ìëë¼ ì¤ì§ì ì¸ ëì±ì ë§ë ¨íë¤. 
    2. ê°íí ë´ì©ì íë³´í´ ì¸ìì ê°ííë¤.
""")

st.markdown("---")

st.markdown("""
    ## 3. ë¸ì¸ì êµíµì¬ê³ ì í¼í´ìì¼ ë¿ ìëë¼ ê°í´ìê° ë  ì ìë¤.          
""")

# ì°ë ¹ìê°í
tab8,tab9 = st.tabs(["50~60ë","ì°ë ¹ë³"])
tab8.subheader("50~60ë ì¬ê³ ê±´ì")
image9 = Image.open('pages/images/traffic10_age.jpeg')
tab8.image(image9)

tab9.subheader("ì°ë ¹ë³ ì¬ê³ ê±´ì")
image10= Image.open('pages/images/traffic11_age2.png')
tab9.image(image10)


st.markdown("""
  â **ì°ë ¹ë³ ë¶ìê²°ê³¼**                 
     - 51ì¸ìì 64ì¸ ì´ì ìë ë¤ë¥¸ ì°ë ¹ëì ëì¼íê² ì¶í´ê·¼ ìê°ì ì¬ê³ ê° ê°ì¥ ë§ì            
     - 65ì¸ ì´ìì ì´ì ìì ê²½ì° ì¤ì  **10ì ~ 12ì, ì¤í 2ì ~ 4ì**ì ê°ì¥ ì¬ê³ ê° ë§ì               
     
  â **ì°¨ì´ ë°ì ì´ì **         
     - í´ì§ì°ë ¹ê³¼ ê´ë ¨ìëê²ì¼ë¡ íì¸ëìë¤. **ë¹ìë°ì  ì¡°ê¸° í´ì§ì¼ë¡ 65ì¸ ì´ìì ì´ì ì ìí ìê°ì´ ë¬ë¼ì¡ë¤.**                               
     - 9 to 6ìì ë©ì´ì§ 65ì¸ ì´ì ê³ ë ¹ ë¸ëìì 19.7%ë ì´ì¡ìì ì¢ì¬í´, ì´ì ê³¼ ìê³ê° ì°ê²°                       
     - ì ë¶ê° ê³ ë ¹ ì´ì ì êµíµì¬ê³  ê°ìë¥¼ ëª©íë¡ ì´ì ë©´í ìì§ ë°ë© ë° ì§ìê¸ ì ëë¥¼ ì´ìíê³  ìììë ì°¸ì¬ê° ì ì¡°í ì´ì                     
     
  â **ìì¬ì **          
     - íêµ­ì 2025ë ê³ ë ¹ ì¸êµ¬ê° 20.3%ì ë¬í´ ì´ê³ ë ¹ ì¬íë¡ ì§ì             
     - **ê³ ë ¹ ë³´íì ë³´í¸ì ëë¶ì´, ê³ ë ¹ ì´ì ìì êµíµì¬ê³  ê°ìë¥¼ ìí´ ì¤ì§ì ì¸ ëì± ë§ë ¨ì´ íìí¨ì ì´ë² íë¡ì í¸ë¥¼ íµí´ íìí  ì ììë¤.**                   
""")

st.markdown("")

st.markdown("""
    #### í´ê²° ë°©ì ì ì
    1. ì´ì ë©´í ê°±ì  ì£¼ê¸° ë¨ì¶ ë° êµíµ ìì  êµì¡ì ìííë¤.
    2. í¹ì  ì°ë ¹ ì´ì ì´ì ìì ì ì²´ê²ì¬ë¥¼ ê°ííë¤.

""")

st.sidebar.header('ð êµíµì¬ê³  ìì¸ ë¶ì ê²°ê³¼ ð')
st.sidebar.markdown("""
    ### ð¥ ëª©ì°¨
    1. í¤ìë
    2. ë¶ìê²°ê³¼ 
     - êµíµëì ì¦ê°ë¡ ì¸í ì¬ê³  ì¦ê°
     - ë²ê°ì ì¼ë¡ë ì¬ê³ ë¥¼ ë§ê¸° ì´ë ¤ì
     - ë¸ì¸ì êµíµí¼í´ì, ê°í´ìë ëë¤.

    ### â ííì´ì§
    github : [https://github.com/meji9086/Traffic-Accident-Data-Analysis](https://github.com/meji9086/Traffic-Accident-Data-Analysis)
""")