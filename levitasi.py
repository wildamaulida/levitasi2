import openai
import streamlit as st
import streamlit.components.v1 as components
import os
from dotenv import load_dotenv

# Memuat file .env
load_dotenv()

# Mengambil API key
openai.api_key = os.getenv("OPENAI_API_KEY")
# Setup OpenAI API key


def get_sensory_play_recommendation(prompt):
    try:
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Kamu adalah asisten yang memberikan rekomendasi sensory play yang aman dan efektif untuk anak-anak dengan autism"},
            {"role": "user", "content": prompt}
        ]
        )
        return response.choices[0].message['content'].strip()
    except openai.error.RateLimitError:
        print("Rate limit reached. Waiting before retrying...")
        time.sleep(60)  # Tunggu 60 detik sebelum mencoba lagi
        return get_sensory_play_recommendation(prompt)
# Setup CSS responsif dan tambahan gaya
def apply_custom_css():
    css = """
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f0f8ff;
        padding: 20px;
    }
    .container {
        max-width: 800px;
        margin: 0 auto;
        background-color: #ffffff;
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
    }
    .header, .footer {
        text-align: center;
        color: #333333;
    }
    .info-box {
        background-color: #e6f7ff;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    .input-container {
        margin-top: 20px;
    }
    .info-text {
        font-size: 1.1em;
        color: #666666;
    }
    </style>
    """
    components.html(css, height=0)

# Streamlit app layout
def main():
    st.title("💡 Aplikasi Rekomendasi Sensory Play untuk Anak dengan Autisme")
    apply_custom_css()

    # Bagian informasi tentang sensory play untuk anak autisme
    st.write("<div class='container'>", unsafe_allow_html=True)
    st.markdown("<div class='header'><h2>Dapatkan Ide Sensory Play yang Tepat Untuk Si Kecil</h2></div>", unsafe_allow_html=True)
    st.markdown("<div class='info-box'><p class='info-text'>"
                "Sensory play adalah aktivitas yang melibatkan indera anak untuk membantu perkembangan mereka, terutama dalam hal taktil, visual, dan motorik. "
                "Aktivitas ini sangat bermanfaat bagi anak dengan autisme, membantu mereka merespons rangsangan secara positif dan nyaman."
                "</p></div>", unsafe_allow_html=True)

    # Input dari pengguna
    st.write("<div class='input-container'>", unsafe_allow_html=True)
    prompt = st.text_input("Deskripsikan preferensi sensory anak Anda (contoh: 'lebih suka tekstur lembut, bermain dengan air')")

    if st.button("Dapatkan Rekomendasi"):
        if prompt:
            # Meminta rekomendasi dari ChatGPT
            recommendation = get_sensory_play_recommendation(f"Beri rekomendasi sensory play untuk {prompt}")
            st.success(f"Rekomendasi: {recommendation}")
        else:
            st.error("Silakan masukkan deskripsi")

    # Footer atau tambahan informasi
    st.markdown("<div class='footer'><p>🌟 Temukan aktivitas sensory play lainnya yang sesuai dengan kebutuhan khusus anak Anda. "
                "Sensory play dapat menjadi bagian penting dalam terapi dan kegiatan sehari-hari mereka.</p></div>", unsafe_allow_html=True)
    st.write("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
