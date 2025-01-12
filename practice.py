import streamlit as st
import random

full = 0

num = int(st.number_input("お好きな数字を入力？",min_value=1,max_value=100,step=1))

if st.button("ここをクリックして希少品をget?"):
    for i in range(num):
        rundom_number = random.randint(-1000,1000)
        st.write(f"{rundom_number}万円をget!")
        full += rundom_number
    st.write(f"合計{full}万円をゲット！")
    st.text_input("ここにメールアドレスを入力！")