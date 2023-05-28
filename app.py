import streamlit as st
from parser import parser

st.title('Reconocedor de Cadenas')
st.subheader('Segundo Parcial')
st.markdown('''
Sea un lenguaje como el siguiente:

$$
L = (^nabc)^{n−1}
$$

Asumamos que 

$$
n=1,2,…
$$ 

Desarrollemos un reconocedor de caadenas que acepte las cadenas de este mismo lenguaje.  Usemos Python junto con la librería PLY para implementar tal reconocedor.
''')

st.header('Parser')
cadena = st.text_input('Ingrese una cadena:')

if st.button('Ingresar'):
    resultado = parser(cadena)
    st.text(f'Resultado: {resultado}')

    