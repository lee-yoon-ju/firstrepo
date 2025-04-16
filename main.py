import streamlit as st

# MBTI 유형별 설명 + 유명인 + 이미지 링크
mbti_info = {
    "INTJ": {
        "description": "전략가형 - 창의적이고 계획적인 사색가입니다.",
        "examples": ["엘론 머스크", "크리스토퍼 놀란"],
        "image": "https://i.imgur.com/uEO2Lhm.png"
    },
    "ENFP": {
        "description": "활동가형 - 열정적이고 상상력이 풍부하며, 새로운 경험을 즐깁니다.",
        "examples": ["로빈 윌리엄스", "로버트 윌리엄스"],
        "image": "https://i.imgur.com/XwAF6qD.png"
    },
    "ISTJ": {
        "description": "현실주의자형 - 책임감 있고 신중하며, 전통을 중시합니다.",
        "examples": ["조지 워싱턴", "나탈리 포트만"],
        "image": "https://i.imgur.com/W4hLZ4x.png"
    },
    "INFP": {
        "description": "중재자형 - 감성적이고 이상주의적이며, 내면의 가치에 충실합니다.",
        "examples": ["셰익스피어", "앨리샤 키스"],
        "image": "https://i.imgur.com/yY2Jk5u.png"
    },
    # (다른 유형들도 필요 시 추가 가능)
}

st.title("🎨 MBTI 성격 유형 알아보기")

selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", list(mbti_info.keys()))

if selected_mbti:
    info = mbti_info[selected_mbti]
    
    st.image(info["image"], caption=f"{selected_mbti} 유형 일러스트", use_column_width=True)
    
    st.subheader(f"🧠 {selected_mbti} 설명")
    st.write(info["description"])

    st.subheader("🎬 유명한 인물")
    for person in info["examples"]:
        st.write(f"- {person}")
