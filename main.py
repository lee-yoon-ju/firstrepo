import streamlit as st

# MBTI 유형별 설명 + 유명인 예시
mbti_info = {
    "INTJ": {
        "description": "전략가형 - 창의적이며 전략적인 사색가입니다. 계획을 잘 세우고 독립적으로 일합니다.",
        "examples": ["엘론 머스크 (Elon Musk)", "크리스토퍼 놀란 (Christopher Nolan)"]
    },
    "INTP": {
        "description": "논리술사형 - 혁신적이고 호기심이 많으며, 이론과 아이디어를 탐구하는 데 열정적입니다.",
        "examples": ["앨버트 아인슈타인 (Albert Einstein)", "빌 게이츠 (Bill Gates)"]
    },
    "ENTJ": {
        "description": "지도자형 - 타고난 리더로서 목표를 세우고 체계적으로 이끌어갑니다.",
        "examples": ["스티브 잡스 (Steve Jobs)", "고든 램지 (Gordon Ramsay)"]
    },
    "ENTP": {
        "description": "변론가형 - 창의적이고 유쾌하며, 새로운 아이디어를 제시하고 토론을 즐깁니다.",
        "examples": ["토마스 에디슨 (Thomas Edison)", "로버트 다우니 주니어 (Robert Downey Jr.)"]
    },
    "INFJ": {
        "description": "옹호자형 - 조용하고 직관적이며, 깊은 신념과 가치관을 가지고 있습니다.",
        "examples": ["마틴 루터 킹 주니어", "니콜 키드먼 (Nicole Kidman)"]
    },
    "INFP": {
        "description": "중재자형 - 이상주의자이며 감정이 풍부하고, 내면의 가치에 충실합니다.",
        "examples": ["윌리엄 셰익스피어 (William Shakespeare)", "앨리샤 키스 (Alicia Keys)"]
    },
    "ENFJ": {
        "description": "선도자형 - 따뜻하고 카리스마 있으며, 사람들을 이끄는 데 능숙합니다.",
        "examples": ["버락 오바마 (Barack Obama)", "오프라 윈프리 (Oprah Winfrey)"]
    },
    "ENFP": {
        "description": "활동가형 - 열정적이고 상상력이 풍부하며, 삶을 즐기고 싶어합니다.",
        "examples": ["로빈 윌리엄스 (Robin Williams)", "로버트 윌리엄스 (Robert Williams)"]
    },
    "ISTJ": {
        "description": "현실주의자형 - 신중하고 책임감이 강하며, 전통을 중시합니다.",
        "examples": ["조지 워싱턴 (George Washington)", "나탈리 포트만 (Natalie Portman)"]
    },
    "ISFJ": {
        "description": "수호자형 - 헌신적이고 친절하며, 타인을 돕는 데 보람을 느낍니다.",
        "examples": ["비욘세 (Beyoncé)", "케이트 미들턴 (Kate Middleton)"]
    },
    "ESTJ": {
        "description": "경영자형 - 체계적이고 리더십이 뛰어나며, 조직을 잘 관리합니다.",
        "examples": ["프랭크 시나트라 (Frank Sinatra)", "존 F. 케네디 (John F. Kennedy)"]
    },
    "ESFJ": {
        "description": "집정관형 - 사교적이고 충성스럽고, 타인을 잘 돌보는 성향입니다.",
        "examples": ["테일러 스위프트 (Taylor Swift)", "제니퍼 가너 (Jennifer Garner)"]
    },
    "ISTP": {
        "description": "장인형 - 조용하지만 과감하며, 실용적인 문제 해결에 능숙합니다.",
        "examples": ["브루스 리 (Bruce Lee)", "클린트 이스트우드 (Clint Eastwood)"]
    },
    "ISFP": {
        "description": "모험가형 - 감성적이고 예술적이며, 삶을 즉흥적으로 즐깁니다.",
        "examples": ["마이클 잭슨 (Michael Jackson)", "브리트니 스피어스 (Britney Spears)"]
    },
    "ESTP": {
        "description": "사업가형 - 에너지 넘치고 대담하며, 위기를 기회로 바꾸는 데 능숙합니다.",
        "examples": ["어니스트 헤밍웨이 (Ernest Hemingway)", "마돈나 (Madonna)"]
    },
    "ESFP": {
        "description": "연예인형 - 외향적이고 열정적이며, 즐거움을 중시하고 분위기를 띄우는 데 능숙합니다.",
        "examples": ["엘비스 프레슬리 (Elvis Presley)", "마일리 사이러스 (Miley Cyrus)"]
    },
}

st.title("🌟 MBTI 성격 유형 알아보기")

# MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", list(mbti_info.keys()))

# 결과 출력
if selected_mbti:
    st.subheader(f"🧠 {selected_mbti} 유형 설명")
    st.write(mbti_info[selected_mbti]["description"])

    st.subheader("🎬 유명한 {0} 유형 인물들".format(selected_mbti))
    for person in mbti_info[selected_mbti]["examples"]:
        st.write(f"- {person}")
