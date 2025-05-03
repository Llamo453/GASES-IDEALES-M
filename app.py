import streamlit as st

# Configuración de la página
st.title('Calculadora de la Ecuación de los Gases Ideales')
st.write("""
Selecciona la variable que deseas calcular y completa los demás campos.

- Presión (P) en atm
- Volumen (V) en litros
- Temperatura (T) en °C
- Número de moles (n) en mol
""")

R = 0.0821  # Constante de los gases ideales en L·atm/mol·K

# Selector para elegir la variable a calcular
variable = st.selectbox('¿Qué variable quieres calcular?', ['Presión (P)', 'Volumen (V)', 'Temperatura (T)', 'Número de moles (n)'])

if variable == 'Presión (P)':
    V = st.number_input('Volumen (V) en litros:', min_value=0.01)
    T_celsius = st.number_input('Temperatura (T) en °C:')
    n = st.number_input('Número de moles (n):', min_value=0.0001)

    if st.button('Calcular Presión'):
        T_kelvin = T_celsius + 273.15
        P = (n * R * T_kelvin) / V
        st.success(f'Presión = {P:.3f} atm')

elif variable == 'Volumen (V)':
    P = st.number_input('Presión (P) en atm:', min_value=0.01)
    T_celsius = st.number_input('Temperatura (T) en °C:')
    n = st.number_input('Número de moles (n):', min_value=0.0001)

    if st.button('Calcular Volumen'):
        T_kelvin = T_celsius + 273.15
        V = (n * R * T_kelvin) / P
        st.success(f'Volumen = {V:.3f} litros')

elif variable == 'Temperatura (T)':
    P = st.number_input('Presión (P) en atm:', min_value=0.01)
    V = st.number_input('Volumen (V) en litros:', min_value=0.01)
    n = st.number_input('Número de moles (n):', min_value=0.0001)

    if st.button('Calcular Temperatura'):
        T_kelvin = (P * V) / (n * R)
        T_celsius = T_kelvin - 273.15
        st.success(f'Temperatura = {T_celsius:.2f} °C')

elif variable == 'Número de moles (n)':
    P = st.number_input('Presión (P) en atm:', min_value=0.01)
    V = st.number_input('Volumen (V) en litros:', min_value=0.01)
    T_celsius = st.number_input('Temperatura (T) en °C:')

    if st.button('Calcular Número de moles'):
        T_kelvin = T_celsius + 273.15
        n = (P * V) / (R * T_kelvin)
        st.success(f'Número de moles = {n:.4f} mol')
