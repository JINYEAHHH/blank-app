import streamlit as st
import random

st.title("🎲 주사위 실험기")

# 1. 슬라이더로 주사위 개수 선택
num_dice = st.slider("주사위 개수 선택", min_value=1, max_value=200, value=1)

# 유니코드 주사위 문자 매핑
dice_unicode = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅"
}

# 2. 버튼을 눌렀을 때 주사위를 굴림
if st.button("주사위 굴리기"):
    # 주사위 굴리기: 1~6 사이의 숫자
    rolls = [random.randint(1, 6) for _ in range(num_dice)]

    # 유니코드 변환
    roll_display = [dice_unicode[roll] for roll in rolls]

    # 평균 계산
    average = sum(rolls) / num_dice

    # 결과 출력
    st.write("🎲 굴린 결과:")
    st.write(" ".join(roll_display))
    st.write(f"🎯 주사위 평균: {average:.2f}")
