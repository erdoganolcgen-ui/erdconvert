import streamlit as st
import os

st.set_page_config(page_title="Calculators & Audio Tools", layout="centered")

st.title("🚀 Calculators & Audio Tools")
st.write("Welcome! Choose the tool you want to use from the menu below.")

# Sadece bizi yormayacak aktif modüller kaldı
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

# 2. BMI CALCULATOR
elif menu == "BMI Calculator":
    st.subheader("🏋️ Body Mass Index (BMI)")
    weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=70.0)
    height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=170.0)
    
    if st.button("Calculate BMI"):
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        st.metric(label="Your BMI Index", value=f"{bmi:.2f}")
        if bmi < 18.5: st.warning("Underweight")
        elif 18.5 <= bmi < 25: st.success("Normal Weight")
        else: st.error("Overweight / Obese")

# 3. PERCENTAGE CALCULATOR
elif menu == "Percentage Calculator":
    st.subheader("📊 Percentage Calculator")
    num = st.number_input("Main Number", value=100.0)
    percentage = st.number_input("Percentage (%)", value=20.0)
    
    if st.button("Calculate"):
        result = (num * percentage) / 100
        st.success(f"{percentage}% of {num} is: **{result:.2f}**")
