import streamlit as st  
from openai import OpenAI  

# OpenAI 설정  
client = OpenAI(api_key=st.secrets["openai"]["api_key"])  

# 페이지 설정  
st.title("🎨 작가 스타일 이미지 생성기")  

# 작가 스타일 정의  
artists = {  
    "에드워드 호퍼 (미국)": "beautiful landscape in Edward Hopper style, with strong light and shadows, urban American scene",  
    "잭슨 폴록 (미국)": "beautiful landscape in Jackson Pollock style, abstract expressionist, dynamic composition",  
    "박수근 (한국)": "beautiful landscape in Park Soo-keun style, Korean traditional scene, earth tones",  
    "이중섭 (한국)": "beautiful landscape in Lee Jung-seob style, Korean folk elements, dynamic composition"  
}  

# 사이드바 컨트롤  
st.sidebar.header("설정")  
artist = st.sidebar.selectbox("작가 선택", list(artists.keys()))  
size = st.sidebar.select_slider(  
    "이미지 크기",  
    options=["256x256", "512x512", "1024x1024"],  
    value="512x512"  
)  

# 이미지 생성  
if st.sidebar.button("이미지 생성"):  
    try:  
        with st.spinner("이미지 생성 중..."):  
            response = client.images.generate(  
                prompt=artists[artist],  
                n=1,  
                size=size  
            )  
            
            # 이미지 표시  
            st.image(response.data[0].url, caption=f"{artist} 스타일", use_column_width=True)  
            
    except Exception as e:  
        st.error(f"오류 발생: {str(e)}")  

# 작가 정보  
st.markdown("---")  
st.subheader("작가 소개")  

artist_info = {  
    "에드워드 호퍼 (미국)": "미국의 사실주의 화가로, 도시의 고독과 현대성을 표현했습니다.",  
    "잭슨 폴록 (미국)": "추상표현주의의 대표 작가로, 액션 페인팅 기법으로 유명합니다.",  
    "박수근 (한국)": "한국의 모더니즘 화가로, 서민적 소재와 질박한 화풍이 특징입니다.",  
    "이중섭 (한국)": "한국 근대미술의 대표 작가로, 민족적 정서를 담은 작품을 그렸습니다."  
}  

st.write(artist_info[artist])  
st.caption("Powered by DALL-E")
