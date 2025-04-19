import streamlit as st
import string

sifre = st.text_input("Şifrenizi Giriniz")

if len(sifre)<3:
    st.stop()

# 8 karakter
# büyükharf,küçükharf,sembol,rakam

bh = string.ascii_uppercase
kh = string.ascii_lowercase
sy = string.punctuation
dg = string.digits

bhsay = 0
khsay = 0
sysay = 0
dgsay = 0
for harf in sifre:
    i = bh.count(harf)
    bhsay = bhsay + i

    y = kh.count(harf)
    khsay = khsay + y

    z = sy.count(harf)
    sysay = sysay + z

    t = dg.count(harf)
    dgsay = dgsay + t

#print("Küçük Harf:", khsay, "Büyük Harf:", bhsay, "Sembol:", sysay, "Rakam:", dgsay)

sonuc = khsay * bhsay * sysay * dgsay

if len(sifre) < 8:
    sonuc = 0

if sonuc != 0:
    st.success("Şifre Güvenilir")
else:
    st.error("Şifre Güvenilir Değil")
