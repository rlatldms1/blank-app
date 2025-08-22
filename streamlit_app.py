import streamlit as st
import random

# --- 앱 제목 설정 ---
st.title("궁합테스트")

# --- 세션 상태(Session State) 초기화 ---
# 앱이 재실행되어도 점수를 기억하기 위해 세션 상태를 사용합니다.
# 'score'라는 키가 세션 상태에 없으면 None으로 초기화합니다.
if 'score' not in st.session_state:
    st.session_state.score = None

# --- 사용자 이름 입력 ---
# 두 개의 컬럼을 만들어 입력 칸을 나란히 배치합니다.
col1, col2 = st.columns(2)

with col1:
    # 첫 번째 사람의 이름을 입력받습니다.
    my_name = st.text_input("내 이름")

with col2:
    # 두 번째 사람의 이름을 입력받습니다.
    other_name = st.text_input("상대방 이름")

# --- '궁합 결과 보기' 버튼 ---
if st.button("궁합 결과 보기"):
    # 두 이름이 모두 입력되었는지 확인합니다.
    if my_name and other_name:
        # 0부터 100 사이의 랜덤한 정수를 생성하여 세션 상태에 저장합니다.
        st.session_state.score = random.randint(0, 100)
    else:
        # 이름 중 하나라도 입력되지 않았다면 경고 메시지를 표시합니다.
        st.warning("두 사람의 이름을 모두 입력해주세요!")
        # 이전 결과가 남아있지 않도록 점수를 초기화합니다.
        st.session_state.score = None

# --- 결과 출력 ---
# 세션 상태에 저장된 점수가 있을 경우 (None이 아닐 경우) 결과를 화면에 표시합니다.
if st.session_state.score is not None:
    score = st.session_state.score
    st.markdown(f"### 💖 {my_name}님과(와) {other_name}님의 궁합!")

    # 점수에 따라 다른 메시지와 스타일을 적용합니다.
    if score >= 90:
        st.success(f"결과는 **{score}%** 입니다! 천생연분이시네요! 🎉")
    elif score >= 70:
        st.info(f"결과는 **{score}%** 입니다. 아주 좋은 관계가 될 수 있어요. 😊")
    elif score >= 40:
        st.warning(f"결과는 **{score}%** 입니다. 서로 조금 더 알아가는 시간이 필요해요. 🤔")
    else:
        st.error(f"결과는 **{score}%** 입니다. 음... 친구로 지내는 건 어떠세요? 😅")
