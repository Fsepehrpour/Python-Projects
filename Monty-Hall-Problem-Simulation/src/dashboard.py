import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src import game_simulation


st.image('images/dashboard-image.png')
st.title(':zap: Monty Hall Simulation')

num_games = st.number_input(
    'Enter number of games you want to simulate:',
    min_value=1, max_value=100000,
    value=1000
)

num_wins_without_switching, num_wins_with_switching = game_simulation(num_games)

data = {
    'Strategy': ['Stay', 'Switch'],
    'Win Percentage': [num_wins_without_switching / num_games * 100, num_wins_with_switching / num_games * 100]
}

df = pd.DataFrame(data)

st.bar_chart(data=df, x='Strategy', y='Win Percentage', height=600)

plt.ylim(0, 100)  # Set the y-axis limits from 0 to 100
plt.show()

