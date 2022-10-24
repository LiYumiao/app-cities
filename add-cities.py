import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('World Cities')

df = pd.read_csv('worldcities.csv')

#population_filter
pop_slider = st.slider('Choose population', 0.0, 40.0, 3.6)

capital_filter = st.sidebar.multiselect(
     'Capital Selector',
     df.capital.unique(),  #options
     df.capital.unique())  #default

form = st.sidebar.form("country_form")
country_filter = form.text_input('Country Name (enter ALL to reset)', 'ALL')
form.form_submit_button("Apply")

#filter by population
df = df[df.population >= pop_slider]

#fitler by capital
df = df[df.capital.isin(capital_filter)]

#filter by country
if country_filter!='ALL':
    df = df[df.country == country_filter]

#show on map
st.map(df)

st.write(df)

fig, ax = plt.subplots()
pop_sum = df.groupby('country')['population'].sum()
pop_sum.plot.bar(ax=ax)
st.pyplot(fig)
