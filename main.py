import pickle
import streamlit as st

nb_model = pickle.load(open('nb_model.sav', 'rb'))

st.title('Klasifikasi Kanker Payudara Menggunakan Algoritma Naive Bayes')
st.image("BreastCancer.jpg")

Age = st.number_input("Usia", 0)
BMI = st.number_input("BMI", 0.00)
Glucose = st.number_input("Glukosa", 0)
Insulin = st.number_input("Insulin", 0.00)
HOMA = st.number_input("HOMA", 0.00)
Leptin = st.number_input("Leptin", 0.00)
Adiponectin = st.number_input("Adiponectin", 0.00)
Resistin = st.number_input("Resistin", 0.00)
MCP = st.number_input("MCP.1", 0.00)

bc_class = ''

if st.button('Cek Hasil'):
    bc_class = nb_model.predict([[Age, BMI, Glucose, Insulin, HOMA, Leptin, Adiponectin, Resistin, MCP]])
    if(bc_class == 'Healthy'):
        bc_class = 'Negative Breast Cancer'
        st.success(bc_class)
    elif(bc_class == 'Breast Cancer'):
        bc_class = 'Positive Breast Cancer'
        st.error(bc_class)

