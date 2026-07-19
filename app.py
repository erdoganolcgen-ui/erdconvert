import streamlit as st
import requests

st.set_page_config(page_title="Çok Amaçlı Hesaplayıcı", layout="centered")

st.title("🎛️ Calculators & Tools")

# Menü Seçimi (Sorun çıkaran ses kısmını temizledik, diğerleri tıkır tıkır çalışacak)
menu = st.sidebar.selectbox(
    "Bir Araç Seçin:",
    ["BMI Hesaplayıcı", "Yüzde Hesaplayıcı", "Döviz Çevirici"]
)

# 1. BMI HESAPLAYICI
if menu == "BMI Hesaplayıcı":
    st.header("⚖️ BMI (Vücut Kitle İndeksi) Hesaplayıcı")
    kilo = st.number_input("Kilonuz (kg):", min_value=1.0, max_value=300.0, value=70.0)
    boy_cm = st.number_input("Boyunuz (cm):", min_value=50.0, max_value=250.0, value=170.0)
    
    if st.button("Hesapla"):
        boy_m = boy_cm / 100
        bmi = kilo / (boy_m ** 2)
        st.subheader(f"BMI Değeriniz: {bmi:.2f}")
        
        if bmi < 18.5:
            st.warning("Zayıf kategorisindesiniz.")
        elif 18.5 <= bmi < 25:
            st.success("Normal kilolu kategorisindesiniz.")
        elif 25 <= bmi < 30:
            st.warning("Fazla kilolu kategorisindesiniz.")
        else:
            st.error("Obez kategorisindesiniz.")

# 2. YÜZDE HESAPLAYICI
elif menu == "Yüzde Hesaplayıcı":
    st.header("📊 Yüzde Hesaplayıcı")
    sayi = st.number_input("Sayıyı girin:", value=100.0)
    yuzde = st.number_input("Yüzde oranını girin (%):", value=20.0)
    
    if st.button("Hesapla"):
        sonuc = (sayi * yuzde) / 100
        st.success(f"{sayi} sayısının %{yuzde}'si = {sonuc}")

# 3. DÖVİZ ÇEVİRİCİ
elif menu == "Döviz Çevirici":
    st.header("💱 Döviz Çevirici (Canlı Kurlar)")
    miktar = st.number_input("Çevrilecek Miktar:", min_value=0.0, value=1.0)
    kaynak_doviz = st.selectbox("Kaynak Para Birimi:", ["USD", "EUR", "TRY", "GBP"])
    hedef_doviz = st.selectbox("Hedef Para Birimi:", ["TRY", "USD", "EUR", "GBP"])
    
    if st.button("Çevir"):
        with st.spinner("Canlı kurlar alınıyor..."):
            try:
                url = f"https://er-api.com{kaynak_doviz}"
                response = requests.get(url).json()
                if response["result"] == "success":
                    kur = response["rates"][hedef_doviz]
                    toplam = miktar * kur
                    st.success(f"{miktar} {kaynak_doviz} = {toplam:.2f} {hedef_doviz}")
                    st.caption(f"Güncel Kur: 1 {kaynak_doviz} = {kur:.4f} {hedef_doviz}")
                else:
                    st.error("Döviz kurları alınamadı.")
            except:
                st.error("İnternet bağlantısı kurulamadı.")

