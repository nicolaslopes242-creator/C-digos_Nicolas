import streamlit as st

# python -m streamlit run app.py

# ------------------------------------------------- Sidebar

st.sidebar.image("Logo.png")
st.sidebar.title('Lopes Imports')


bike = ['Bicicleta Caloi aro 29 Elite Carbon Sport','Bicicleta Caloi Andes Aro 26', 'bicicleta freeride grau aro 26', 'Bike Santa Cruz V10', 'BIke colli aro 29']

opcao = st.sidebar.selectbox('Escolha a bike que foi alugado', bike)



# ----------------------------------------------- Principal 
st.title('Lopes Imports- Aluguel de Bikes')

st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f'Por quantos dias a {opcao} foi alugado?')
km = st.text_input(f'Quantos km você rodou com o {opcao}?')

if opcao == 'Bicicleta Caloi aro 29 Elite Carbon Sport':
    diaria = 797

elif opcao == 'Bicicleta Caloi Andes Aro 26':
    diaria = 550

elif opcao == 'bicicleta freeride grau aro 26':
    diaria = 650

elif opcao == 'Bike Santa Cruz V10':
    diaria = 750

elif opcao == 'BIke colli aro 29':
    diaria = 650





if st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias+total_km

    st.warning(f'Você alugou o {opcao} por {dias} dias e rodou {km}km. O valor total a pagar é R${aluguel_total:.2f}')













