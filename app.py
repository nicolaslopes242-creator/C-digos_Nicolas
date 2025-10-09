import streamlit as st

# python -m streamlit run app.py

# ------------------------------------------------- Sidebar

st.sidebar.image("Logo.png")
st.sidebar.title('Lopes Imports')


bike = ['Bicicleta Caloi aro 29 Elite Carbon Sport','Bicicleta Caloi Andes Aro 26', 'Porsche', 'Mitsubishi', 'Ferrari']

opcao = st.sidebar.selectbox('Escolha a bike que foi alugado', bike)



# ----------------------------------------------- Principal 
st.title('Lopes Imports- Aluguel de Bikes')

st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f'Por quantos dias a {opcao} foi alugado?')
km = st.text_input(f'Quantos km você rodou com o {opcao}?')

if opcao == 'Lamborghini':
    diaria = 5000

elif opcao == 'Mustang':
    diaria = 2000

elif opcao == 'Porsche':
    diaria = 3500

elif opcao == 'Mitsubishi':
    diaria = 3415

elif opcao == 'Ferrari':
    diaria = 2950





if st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias+total_km

    st.warning(f'Você alugou o {opcao} por {dias} dias e rodou {km}km. O valor total a pagar é R${aluguel_total:.2f}')













