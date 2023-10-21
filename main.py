import pickle
import streamlit as st
from sklearn.model_selection import train_test_split

model = pickle.load(open('estimasi_global_sales_vidio_game.sav', 'rb'))

st.title('Estimasi Data Global Sales Vidio Game')

NA_Sales = st.number_input('Input Penjualan Amerika Utara')
EU_Sales = st.number_input('Input Penjualan Eropa')
JP_Sales = st.number_input('Input Penjualan Jepang')
Other_Sales = st.number_input('Input Penjualan Lainnya')

predict = ''

if st.button('Estimasi Global'):
    predict = model.predict(
        [[NA_Sales, EU_Sales, JP_Sales, Other_Sales]]
    )
    st.write('Estimasi Penjualan Global : ', predict)
