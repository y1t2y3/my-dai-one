import streamlit as st   # 导入Streamlit并用st代表它

st.title('🕶学生 小陆-数字档案  ' )

st.header('🔑 基础信息')

st.caption('学生ID：:red[NEO·2023·301]')
st.caption('注册时间 :`2023-10-01 08:30:17`  |精神状态：✅:red[未知]')
st.caption('当前教室 :`实训楼301`  |安全等级 :red[绝密]')



import streamlit as st
st.title("📊 技能矩阵")


c1, c2, c3 = st.columns(3)
c1.metric(label="c语音", value="95%", delta="2%")
c2.metric(label="python", value="87%", delta="-1%")
c3.metric(label="Java", value="68%", delta="-10%", delta_color="off")

st.subheader("Streamlit课程进度")
st.progress(0.25)



st.subheader('📝任务日志')

import pandas as pd 
data = {
    '日期':['2023-10-01', '2023-10-05', '2023-10-12'],
    '任务':['学生数字档案', '课程管理系统','数据图表展示'],
    '状态':['✅完成', ' 🕒 进行中', '❌未完成' ],
    '难度':['★★☆☆☆','★☆☆☆☆','★★★☆☆']}

index = pd.Series([0, 1, 2,])
    
df = pd.DataFrame(data, index=index)
st.dataframe(df)
















st.header('🔐最新代码成果' )

python_code = '''def matrix_breach():
     while True
       if detect_vulnerability()
          exploit()
          return "ACCESS GRANTED"
       else:
           stealth_evade()
'''
# 创建一个代码块，用于展示python_code的内容
# 并设置language为None，即该代码块无语法高亮
st.code(python_code)

st.caption(' `>>SYSTEM MESSAGE:` 下一个任务目标已经解锁...')
st.caption(' `>>TARGET:` 课程管理系统')
st.caption(' `>>COUNTDOWW:` 2025-06-03 15:24:58')
st.caption('系统状态: :green[在线] 连接状态: :red[已加密]')
