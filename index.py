'''
streamlit多页面程序的入口文件
'''
import streamlit as st
st.title("AI大模型应用产品网")
col,col1 = st.columns(2)
#
with col:
    st.image("https://p1.ssl.qhmsg.com/dr/270_500_/t01d2029fc263d2ce98.png?size=650x650",use_column_width=True)
    flag = st.button("绘言",use_container_width=True)
    if flag:
        st.switch_page("pages/huiyan.py")
#
with col1:
    st.image("https://ts1.cn.mm.bing.net/th/id/R-C.904b7f1fa9bf6cd0067e9c30411dfc54?rik=2ZQYglWivBB%2fjg&riu=http%3a%2f%2fwww.cidianwang.com%2ffile%2fshufa%2fxingshu%2fwenzhengming%2f2015103120322471.jpg&ehk=C3D6hQq%2bIKLUKw11ftAJhUsPHWjLSzfwPrfp1eqXXJE%3d&risl=&pid=ImgRaw&r=0&sres=1&sresct=1", use_column_width=True)
    flag = st.button("绘图",use_container_width=True)
    if flag:
        st.switch_page("pages/textToImage.py")
# c1,c2,c3,c4 = st.columns(4)
# with c1:
#     flag = st.button("基础版")
#     if flag:
#         st.switch_page("pages/demo.py")
# with c2:
#     flag1 = st.button("进阶版")
#     if flag1:
#         st.switch_page("pages/demo01.py")
# with c3:
#     flag2 = st.button("最终版")
#     if flag2:
#         st.switch_page("pages/huiyan.py")
# with c4:
#     flag3 = st.button("文生图")
#     if flag3:
#         st.switch_page("pages/textToImage.py")