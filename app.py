import streamlit as st
import joblib
import numpy as np

model_path = 'PROYECTO/models/Prediccion_score_c_rf.pkl'
model = joblib.load(model_path)

st.title("💳 Predicción de Score Crediticio")

st.write("### Introduce los valores para predecir Score Crediticio:")

col1, col2, col3 = st.columns(3)

with col1:
    mezcla_credito_ordinal = st.selectbox("Mezcla de Crédito", options=[1, 2, 3])
    st.caption("**Selecciona 1 (Malo), 2 (Regular) o 3 (Bueno)**")
    
    pago_monto_minimo_f = st.selectbox("Pago Unicamente Monto Mínimo", options=[0, 1])
    st.caption("**1 si solo se ha pagado el monto mínimo o 0 si no**")
    
    tasa_interes = st.number_input("Tasa de Interés", min_value=1, max_value=100, value=25)
    st.caption("**Introduce la tasa de interés entre 1 y 100%**")

with col2:
    retraso_promedio_pagos = st.number_input("Retraso Promedio de Pagos", min_value=0, max_value=100, value=8)
    st.caption("**Introduce el promedio de días de retraso**")
    
    numero_consultas_credito = st.number_input("Número de Consultas de Crédito", min_value=0, max_value=50, value=7)
    st.caption("**Introduce el número de consultas de crédito**")
    
    deuda_pendiente = st.number_input("Deuda Pendiente (en USD)", min_value=0.0, max_value=100000.0, value=1822.87)
    st.caption("**Introduce la deuda pendiente en USD**")

with col3:
    antiguedad_historial_credito = st.number_input("Antigüedad del Historial de Crédito (meses)", min_value=0.0, max_value=1000.0, value=100.0)
    st.caption("**Introduce la antigüedad en meses**")
    
    numero_tarjetas_credito = st.number_input("Número de Tarjetas de Crédito", min_value=0, max_value=50, value=6)
    st.caption("**Introduce el número de tarjetas de crédito**")
    
    numero_cuentas_bancarias = st.number_input("Número de Cuentas Bancarias", min_value=0, max_value=50, value=6)
    st.caption("**Introduce el número de cuentas bancarias**")

suma_q_prestamos = st.number_input("Total de Préstamos Adquiridos", min_value=0, max_value=50, value=2)
st.caption("**Introduce el número total de préstamos adquiridos**")

if st.button("Predecir"):
    input_data = np.array([[mezcla_credito_ordinal, pago_monto_minimo_f, tasa_interes, 
                            retraso_promedio_pagos, numero_consultas_credito, deuda_pendiente,
                            antiguedad_historial_credito, numero_tarjetas_credito, 
                            numero_cuentas_bancarias, suma_q_prestamos]])
    
    prediction = model.predict(input_data)
    
    if prediction[0] == 0:
        st.error("🚩 Cuidado: El cliente tiene un puntaje de crédito **malo**.")
    elif prediction[0] == 1:
        st.warning("⚠️ Precaución: El cliente tiene un puntaje de crédito **regular**.")
    else:
        st.success("🎉 ¡Excelente! El cliente tiene un puntaje de crédito **bueno**.")
