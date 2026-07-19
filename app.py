import streamlit as st

st.set_page_config(page_title="Calculators & Audio Tools", layout="centered")

st.title("🚀 Calculators & Audio Tools")
st.write("Welcome! Choose the tool you want to use from the menu below.")

menu = st.sidebar.selectbox("Select a Tool", [
    "MP4 to MP3 Converter", 
    "BMI Calculator", 
    "Percentage Calculator"
])

# 1. MP4 TO MP3 CONVERTER
if menu == "MP4 to MP3 Converter":
    st.subheader("🎵 MP4 to MP3 Video Converter")
    st.write("Extract audio from your MP4 videos instantly.")
    
    uploaded_file = st.file_uploader("Upload your MP4 video file", type=["mp4"])
    
    if uploaded_file is not None:
        st.success("File uploaded successfully! Ready to convert.")

# 2. BMI CALCULATOR (TAM TAMINA ÇALIŞAN HESAPLAMA MOTORU)
elif menu == "BMI Calculator":
    st.subheader("🏋️ Body Mass Index (BMI)")
    
    weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=70.0, step=0.1)
    height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=170.0, step=1.0)
    
    # Doğrudan canlı hesaplama tetikleyicisi
    height_m = height / 100.0
    bmi = weight / (height_m ** 2)
    
    st.markdown("---")
    st.metric(label="Your Calculated BMI Index", value=f"{bmi:.2f}")
    
    if bmi < 18.5:
        st.warning("Category: Underweight ⚠️")
    elif 18.5 <= bmi < 25.0:
        st.success("Category: Normal Weight  (Healthy)")
    elif 25.0 <= bmi < 30.0:
        st.info("Category: Overweight ⚠️")
    else:
        st.error("Category: Obese 🚨")

# 3. PERCENTAGE CALCULATOR (TAM TAMINA ÇALIŞAN YÜZDE MOTORU)
elif menu == "Percentage Calculator":
    st.subheader("📊 Percentage Calculator")
    
    num = st.number_input("Main Number (X)", value=100.0, step=1.0)
    percentage = st.number_input("Percentage Rate (Y %)", value=20.0, step=1.0)
    
    # Doğrudan canlı yüzde hesaplaması
    result = (num * percentage) / 100.0
    
    st.markdown("---")
    st.success(f"Result: **{percentage}%** of **{num}** is exactly = **{result:.2f}**")

