import streamlit as st

# Título
st.title("Calculadora de la Ecuación de los Gases Ideales")

# Constante de los gases
R = 0.0821

# Menú de selección
st.write("""
Selecciona la variable que deseas calcular:
- **Presión (atm)**
- **Volumen (L)**
- **Temperatura (K)**
- **Número de moles (mol)**
""")

opcion = st.selectbox(
    "¿Qué variable deseas calcular?",
    ("Presión (P)", "Volumen (V)", "Temperatura (T)", "Número de moles (n)")
)

if opcion == "Presión (P)":
    V = st.number_input("Ingresa el volumen (L):", min_value=0.01, format="%.3f")
    n = st.number_input("Ingresa el número de moles (mol):", min_value=0.001, format="%.3f")
    T = st.number_input("Ingresa la temperatura (K):", min_value=0.01, format="%.2f")
    if st.button("Calcular Presión"):
        P = (n * R * T) / V
        st.success(f"La presión es: {P:.3f} atm")

elif opcion == "Volumen (V)":
    P = st.number_input("Ingresa la presión (atm):", min_value=0.001, format="%.3f")
    n = st.number_input("Ingresa el número de moles (mol):", min_value=0.001, format="%.3f")
    T = st.number_input("Ingresa la temperatura (K):", min_value=0.01, format="%.2f")
    if st.button("Calcular Volumen"):
        V = (n * R * T) / P
        st.success(f"El volumen es: {V:.3f} L")

elif opcion == "Temperatura (T)":
    P = st.number_input("Ingresa la presión (atm):", min_value=0.001, format="%.3f")
    V = st.number_input("Ingresa el volumen (L):", min_value=
