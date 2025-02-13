import streamlit as st
from constant import CURRENCIES
from currency_converter import get_exchange_rate, convert_currency

st.title(':dollar: Currency Converter')

st.markdown(
    """
    <style>
    .green-text  {
        color: green;
    }
    </style>

    <p class="green-text">This tool allows you to instantly convert amounts between different currencies. Enter the amount and choose the currencies to see the result.</p>
    """,
    unsafe_allow_html=True
)

base_currency = st.selectbox('From (base):', CURRENCIES)
target_currency = st.selectbox('To (target):', CURRENCIES)

amount = st.number_input('Enter amout to convert:', min_value=0.0, value=100.0)

if amount > 0 and base_currency and target_currency:
    exchange_rate = get_exchange_rate(base_currency, target_currency)

    if exchange_rate:
        converted_amount = convert_currency(amount, exchange_rate)
        converted_amount = round(converted_amount,2)
        st.success(f"✅ Exchange Rate: {exchange_rate:.4f}")
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Base Currency", value=f'{amount:.2f} ({base_currency})')
        col2.markdown("<h1 style='text-align: center; margin: 0; color: green;'>&#8594;</h1>", unsafe_allow_html=True)
        col3.metric(label="Target Currency", value=f'{converted_amount:.2f} ({target_currency})')
    else:
        st.error('Error fetching exchange rate.')

st.markdown('___') # Devider

st.markdown("##### ℹ️ About This Tool")
st.markdown("""
This currency converter uses real-time exchange rates provided by the ExchangeRate-API.
- The conversion updates automatically as you input the amount or change the currency.
- Enjoy seamless currency conversion without the need to press a button!
""")



