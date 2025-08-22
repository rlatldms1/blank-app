import streamlit as st

# 앱 제목 설정
st.title("MBTI 학습 유형 진단")

# 세션 상태 초기화 (페이지가 다시 실행되어도 값 유지)
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'answers' not in st.session_state:
    st.session_state.answers = {}

# MBTI 질문 목록
questions = {
    "EI": "사람들과 어울리며 에너지를 얻는 편이다.",
    "SN": "나무보다는 숲을 보는 경향이 있다.",
    "TF": "결정할 때 사실과 논리를 중요하게 생각한다.",
    "JP": "계획을 세우고 체계적으로 행동하는 것을 선호한다.",
    "EI_2": "혼자 조용히 시간을 보내며 재충전한다.",
    "SN_2": "실제 경험과 구체적인 사실에 더 집중한다.",
}

# 각 질문에 대한 라디오 버튼 생성
for key, question in questions.items():
    # st.session_state.answers 딕셔너리에 각 질문의 답변을 저장
    st.session_state.answers[key] = st.radio(
        question,
        ("예", "아니오"),
        key=f"radio_{key}" # 각 라디오 버튼에 고유한 key 부여
    )
    st.markdown("---") # 질문 구분을 위한 라인

# 제출 버튼
if st.button("결과 보기"):
    st.session_state.submitted = True

# 제출 버튼을 눌렀을 때 결과 표시
if st.session_state.submitted:
    # MBTI 유형 계산 (간단한 로직)
    answers = st.session_state.answers

    # E/I 지표 계산
    e_score = 1 if answers["EI"] == "예" else 0
    i_score = 1 if answers["EI_2"] == "예" else 0
    ei = "E" if e_score > i_score else "I"

    # S/N 지표 계산
    sn = "N" if answers["SN"] == "예" else "S"
    
    # 추가 질문이 있다면 여기에 더 정교한 로직을 추가할 수 있습니다.
    # 이 예제에서는 SN_2 질문을 직접 사용하지 않고 단순화했습니다.
    # 필요하다면 아래와 같이 수정할 수 있습니다.
    # n_score = 1 if answers["SN"] == "예" else 0
    # s_score = 1 if answers["SN_2"] == "예" else 0
    # sn = "N" if n_score > s_score else "S"
    

    # T/F, J/P 지표는 고정값으로 단순화 (질문이 부족하므로)
    # 실제 앱에서는 이 부분에 해당하는 질문을 추가해야 합니다.
    tf = "T" if answers["TF"] == "예" else "F"
    jp = "J" if answers["JP"] == "예" else "P"
    
    # 최종 MBTI 유형 조합
    mbti_type = f"{ei}{sn}{tf}{jp}"

    # MBTI 유형별 학습 스타일 설명
    learning_styles = {
        "ISTJ": "혼자 조용히 공부하며, 구체적이고 사실적인 정보를 바탕으로 체계적으로 학습하는 것을 선호합니다.",
        "ISFP": "실습이나 체험처럼 직접 몸으로 부딪히며 배우는 것을 좋아하며, 편안하고 자유로운 분위기에서 효율이 높습니다.",
        "INFJ": "학습 내용의 의미와 가치를 중요하게 생각하며, 토론과 협력을 통해 아이디어를 탐구하는 것을 즐깁니다.",
        "INTP": "복잡한 이론이나 개념을 논리적으로 분석하고 파고드는 것을 좋아하며, 독립적인 학습 환경을 선호합니다.",
        "ESTJ": "명확한 목표와 계획을 세워 효율적으로 학습하며, 실용적이고 현실적인 지식을 중요하게 생각합니다.",
        "ESFP": "다양한 사람들과 교류하며 재미있고 활동적인 방식으로 배우는 것을 좋아합니다. 지루한 이론은 힘들어할 수 있습니다.",
        "ENFJ": "다른 사람을 가르치거나 함께 공부하며 배우는 것을 즐깁니다. 학습 내용이 공동체에 미칠 긍정적 영향을 중요하게 생각합니다.",
        "ENTP": "새로운 아이디어를 탐구하고 논쟁하는 것을 좋아하며, 정해진 규칙보다는 자신만의 방식으로 학습하길 원합니다."
    }
    
    # 기본 결과 설정
    default_style = "분석 결과에 해당하는 유형 정보가 없습니다. 다른 선택을 시도해 보세요."
    result_style = learning_styles.get(mbti_type, default_style)

    # 결과 출력
    st.subheader(f"당신의 MBTI 학습 유형은: {mbti_type}")
    st.info(result_style)
