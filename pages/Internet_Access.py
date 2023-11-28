import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mpld3
import streamlit.components.v1 as components


st.set_page_config(page_title='Glide - Internet Connections',
                   page_icon='assets\images\logo.jpg', layout='centered')


st.title('Visualization of Internet Access in Argentina')


df = pd.read_csv('./internet_access_per_100_houses.csv', sep=',')


views = st.radio(':blue[Select The Data To Visualize]',
                 [':white[Conexions by Year]', ':white[Conexions by Province]', ':white[KPI]'], horizontal=True)


if views == ':white[Conexions by Year]':
    # Show the DataFrame
    st.dataframe(df, hide_index=True)
    st.divider()
    fig1 = plt.figure(figsize=(22, 6))
    # sns.set_style('darkgrid')
    sns.lineplot(data=df, x=df['Year'], y=df['Access per 100 households'],
                 hue='Quarter', palette='tab10', errorbar=None)

    st.pyplot(fig1)
    st.caption(f'Number of connections proyected from 2014 to 2022 in Argentina. ')

    # Set the period of time to show
    period = st.slider(':red[Desired Year]', 2014, 2022, 2014)

    # Plot the DataFrame made in our EDA
    fig = plt.figure(figsize=(10, 6))
    plt.title(f'Evolution of Internet Access throughout the year {period}')
    sns.lineplot(data=df, x=df['Year'] == period, y=df['Access per 100 households'],
                 hue='Quarter', palette='tab10', errorbar=None)
    plt.xlabel(f'Year {period}')
    plt.xticks(ticks=[])
    # Show the chart
    st.pyplot(fig)
    st.caption(f'Number of connections in {period} by quarter. ')

    # Add context to the images above
    st.markdown('')

elif views == ':white[Conexions by Province]':
    # Show the DataFrame
    st.dataframe(df, hide_index=True)
    st.divider()
    # Set the period of time to show
    period2 = st.slider(
        label=':red[Desired Year]', min_value=2014, max_value=2022, step=1, value=None)

    # Create a filter with the Provinces
    provinces = df['Province'].unique().tolist()
    selected_province = st.selectbox(
        "Select The Province to Visualize", (provinces), placeholder="Select Province",)

    # selected_province = st.radio(
    #     f':blue[Select the desired province for the year {period2}]', provinces, horizontal=True, index=0)

    df['Quarter'] = df['Quarter'].astype('str')
    df['Access per 100 households'].astype('str')

    fig, ax = plt.subplots(figsize=(12, 8))

    df_filtrado = df[df['Year'] == period2]
    sns.set_style('darkgrid')
    sns.barplot(data=df_filtrado[df_filtrado['Province'] == selected_province], x='Quarter', y=df['Access per 100 households'],
                hue='Quarter', palette='tab10', errorbar=None)
    plt.legend(title='Quarter', shadow=True, loc='upper center')
    plt.xlabel(f'Quarter')
    plt.ylim(0, 100)

    # st.dataframe(df_filtrado[selected_province])
    # Show the chart
    st.pyplot(fig)
    st.caption(
        f'Visualizing number of Internet access for {selected_province} in the year {period2}')

elif views == ':white[KPI]':

    st.markdown(f'''
                ### Our goal was to Increase internet service access by 2% for the next quarter, per 100 households, by province. <br>
                #### This would allow us to see if we are on the right track and, if not, try a different approach but with a better understanding of our data and a clearer vision 
                ''', unsafe_allow_html=True)
    st.divider()

    st.metric(label='Key Performance Indicator [KPI]',
              value=2)

    # # Set the desired year
    period3 = st.slider(
        label=':red[Desired Year]', min_value=2014, max_value=2022, step=1, value=None)

    fig = plt.figure(figsize=(10, 12))
    # increment = df['Incremental Percentage'].tolist()
    # colors = ['g' if e >= 0 else 'r' for e in increment]
    # st.markdown(colors)

    sns.set_style('darkgrid')
    sns.barplot(df[df['Year'] == period3], x='Province',
                y=df['Incremental Percentage'], errorbar=None)
    plt.ylim(-20, 100)
    plt.xticks(rotation=90)
    st.pyplot(fig)
