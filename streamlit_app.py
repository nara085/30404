import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="유나라 | 자기소개",
    page_icon="☁️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

SNOOPY_IMAGE = "https://upload.wikimedia.org/wikipedia/en/5/53/Snoopy_Peanuts.png"

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&family=Jua&display=swap');

    :root {
        --ink: #193b50;
        --muted: #567486;
        --sky: #bde9f8;
        --blue: #55acd2;
        --line: #d9edf4;
    }

    .stApp {
        background:
            radial-gradient(ellipse at 9% 8%, rgba(255,255,255,.8), transparent 33%),
            repeating-linear-gradient(135deg, rgba(255,255,255,.22) 0 1px, transparent 1px 20px),
            linear-gradient(145deg, #e9f9ff 0%, #c6edfa 48%, #f4fbff 100%);
        color: var(--ink);
        font-family: 'Gowun Dodum', sans-serif;
    }

    [data-testid="stHeader"] { background: transparent; }
    [data-testid="stToolbar"], footer { visibility: hidden; }
    .block-container { max-width: 1060px; padding: 2.5rem 1.5rem 3.5rem; }

    .topline {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding-bottom: 1.25rem;
        border-bottom: 1px solid rgba(57, 126, 155, .18);
        color: #447890;
        font-size: .9rem;
    }
    .topline strong { color: #244e64; font-family: 'Jua', sans-serif; font-size: 1.05rem; font-weight: 400; }

    .hero-copy { padding: 3.5rem 0 2.6rem; }
    .eyebrow {
        display: inline-block;
        padding: 7px 12px;
        border: 1px solid #c3e5f1;
        border-radius: 999px;
        background: rgba(255,255,255,.62);
        color: #397d9a;
        font-size: .84rem;
    }
    .hero-copy h1 {
        margin: 20px 0 10px;
        color: var(--ink);
        font-family: 'Jua', sans-serif;
        font-size: 3.7rem;
        font-weight: 400;
        line-height: 1.2;
    }
    .hero-copy h1 span { color: #3199c3; }
    .school { margin: 0; color: #527286; font-size: 1.08rem; }
    .intro { max-width: 560px; margin: 22px 0 0; color: #365b70; font-size: 1.08rem; line-height: 1.9; }
    .tag-row { display: flex; flex-wrap: wrap; gap: 9px; margin-top: 24px; }
    .tag {
        padding: 8px 12px;
        border: 1px solid rgba(255,255,255,.85);
        border-radius: 8px;
        background: rgba(255,255,255,.55);
        color: #3e7188;
        font-size: .9rem;
    }

    .snoopy-stage {
        position: relative;
        display: flex;
        min-height: 145px;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        border-bottom: 2px solid rgba(76, 154, 184, .25);
        background: linear-gradient(180deg, rgba(255,255,255,.15), rgba(255,255,255,.46));
    }
    .snoopy-stage::before {
        position: absolute;
        right: 8%;
        bottom: 0;
        left: 8%;
        height: 92px;
        border-radius: 100% 100% 0 0;
        background: linear-gradient(180deg, #d4f0e3, #b8e6d1);
        content: '';
    }
    .snoopy-stage img {
        position: relative;
        z-index: 1;
        width: min(55%, 150px);
        max-height: 135px;
        object-fit: contain;
        filter: drop-shadow(0 12px 8px rgba(35, 83, 106, .12));
        animation: arrive .8s ease-out both;
    }
    [data-testid="stImage"] img {
        border: 3px solid rgba(255,255,255,.95);
        border-radius: 14px;
        box-shadow: 0 12px 28px rgba(35, 83, 106, .16);
    }
    .cloud-note {
        position: absolute;
        z-index: 2;
        top: 12%;
        right: 1%;
        padding: 11px 15px;
        border: 1px solid rgba(255,255,255,.9);
        border-radius: 16px 16px 4px 16px;
        background: rgba(255,255,255,.88);
        color: #44788e;
        font-family: 'Jua', sans-serif;
        font-size: 1rem;
    }

    .section { margin-top: 3.1rem; }
    .section-kicker { margin: 0 0 7px; color: #318cb0; font-size: .8rem; font-weight: 700; }
    .section h2 { margin: 0 0 19px; color: var(--ink); font-family: 'Jua', sans-serif; font-size: 1.8rem; font-weight: 400; }
    .interest {
        min-height: 154px;
        padding: 21px;
        border: 1px solid rgba(255,255,255,.96);
        border-radius: 12px;
        background: rgba(255,255,255,.7);
        box-shadow: 0 8px 24px rgba(54, 132, 169, .07);
    }
    .interest .emoji { font-size: 1.7rem; }
    .interest h3 { margin: 9px 0 5px; color: #244b63; font-family: 'Jua', sans-serif; font-size: 1.15rem; font-weight: 400; }
    .interest p { margin: 0; color: var(--muted); line-height: 1.7; }

    .roadmap {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        border-top: 1px solid rgba(57, 126, 155, .2);
        border-bottom: 1px solid rgba(57, 126, 155, .2);
        background: rgba(255,255,255,.34);
    }
    .step { padding: 20px 21px 22px; }
    .step + .step { border-left: 1px solid var(--line); }
    .step-number { color: #388fb3; font-family: 'Jua', sans-serif; font-size: .95rem; }
    .step h3 { margin: 10px 0 7px; color: #244b63; font-family: 'Jua', sans-serif; font-size: 1.12rem; font-weight: 400; }
    .step p { margin: 0; color: var(--muted); line-height: 1.75; }
    .closing {
        margin-top: 2.8rem;
        padding: 18px 22px;
        border-left: 4px solid #70c4e2;
        background: rgba(255,255,255,.54);
        color: #315b73;
        line-height: 1.8;
    }
    .credit { margin-top: 1.4rem; color: #648496; font-size: .78rem; text-align: right; }

    @keyframes arrive {
        from { opacity: 0; transform: translateY(12px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @media (max-width: 700px) {
        .block-container { padding: 1.25rem 1rem 2.5rem; }
        .hero-copy { padding: 2.3rem 0 1.2rem; }
        .hero-copy h1 { font-size: 2.55rem; }
        .snoopy-stage { min-height: 125px; }
        .snoopy-stage img { max-height: 115px; }
        .cloud-note { top: 7%; right: 2%; }
        .section { margin-top: 2.4rem; }
        .roadmap { grid-template-columns: 1fr; }
        .step + .step { border-top: 1px solid var(--line); border-left: 0; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="topline">
        <strong>☁️ NARA'S LITTLE WORLD</strong>
        <span>자기소개 · 2026</span>
    </div>
    """,
    unsafe_allow_html=True,
)

hero_text, hero_art = st.columns([1.15, 0.85], gap="large", vertical_alignment="center")
with hero_text:
    st.markdown(
        """
        <section class="hero-copy">
            <span class="eyebrow">HELLO, NICE TO MEET YOU!</span>
            <h1>안녕, 나는<br /><span>유나라</span>야!</h1>
            <p class="school">경복비즈니스고등학교 3학년 · IT과</p>
            <p class="intro">
                노래와 다양한 콘텐츠를 즐기며 새로운 이야기를 만나는 걸 좋아해요.
                앞으로 소프트웨어와 데이터로 더 편리한 세상을 만드는 사람이 되고 싶습니다.
            </p>
            <div class="tag-row">
                <span class="tag">🎧 음악</span>
                <span class="tag">🍿 영화 · 드라마 · 예능</span>
                <span class="tag">💻 IT · 데이터</span>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

with hero_art:
    st.image(Path(__file__).parent / "img" / "30404유나라.JPG", width=280)
    st.markdown(
        f'<div class="snoopy-stage"><span class="cloud-note">오늘도 좋은 하루! ☁️</span><img src="{SNOOPY_IMAGE}" alt="스누피 캐릭터" /></div>',
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <section class="section">
        <p class="section-kicker">MY LITTLE JOYS</p>
        <h2>내가 좋아하는 시간</h2>
    </section>
    """,
    unsafe_allow_html=True,
)
music, watching = st.columns(2, gap="medium")
with music:
    st.markdown(
        """
        <article class="interest">
            <span class="emoji">🎶</span>
            <h3>노래 듣기</h3>
            <p>좋아하는 음악을 들으며 기분을 전환하고 에너지를 채워요.</p>
        </article>
        """,
        unsafe_allow_html=True,
    )
with watching:
    st.markdown(
        """
        <article class="interest">
            <span class="emoji">🎬</span>
            <h3>OTT 시청</h3>
            <p>영화와 드라마, 예능을 보며 다채로운 이야기와 즐거움을 만나요.</p>
        </article>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <section class="section">
        <p class="section-kicker">A DREAM IN PROGRESS</p>
        <h2>꿈을 향한 나의 다음 장</h2>
        <div class="roadmap">
            <article class="step">
                <span class="step-number">STEP 01</span>
                <h3>IT 기초 다지기</h3>
                <p>학교에서 배우는 내용을 바탕으로 소프트웨어와 데이터에 대한 기본기를 쌓아가요.</p>
            </article>
            <article class="step">
                <span class="step-number">STEP 02</span>
                <h3>소프트웨어공학과 진학</h3>
                <p>대학에서 소프트웨어를 깊이 공부하고, 문제를 기술로 해결하는 힘을 기르고 싶어요.</p>
            </article>
            <article class="step">
                <span class="step-number">STEP 03</span>
                <h3>데이터 분야에서 성장</h3>
                <p>IT 분야의 데이터 관련 기업에 취업해 의미 있는 데이터 서비스를 만드는 것이 목표예요.</p>
            </article>
        </div>
    </section>
    <aside class="closing">
        좋아하는 일에서 에너지를 얻고, 궁금한 것은 하나씩 배워가며 제 속도로 성장하고 있어요.<br />
        데이터와 소프트웨어를 연결하는 멋진 IT 인재가 되겠습니다. 만나서 반가워요! 💙
    </aside>
    <p class="credit">Snoopy image: Wikimedia Commons</p>
    """,
    unsafe_allow_html=True,
)