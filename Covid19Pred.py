# -*- coding: utf-8 -*-
"""
Created on Tue May  5 17:00:21 2020

@author: sChikamhi
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Data set1
df = pd.read_csv('covid_19_data.csv')
df.rename(columns={'ObservationDate':'Date', 'Country/Region':'Country'}, inplace=True)

# Data set2

df_confirmed = pd.read_csv('time_series_covid_19_confirmed.csv')
df_recovered = pd.read_csv("time_series_covid_19_recovered.csv")
df_deaths = pd.read_csv("time_series_covid_19_deaths.csv")

df_confirmed.rename(columns={'Country/Region':'Country'}, inplace=True)
df_recovered.rename(columns={'Country/Region':'Country'}, inplace=True)
df_deaths.rename(columns={'Country/Region':'Country'}, inplace=True)

# By country in diffreent provinces and dates
df2 = df.groupby(["Date", "Country", "Province/State"])[['SNo', 'Date', 'Province/State', 
                'Country', 'Confirmed', 'Deaths', 'Recovered']].sum().reset_index()
df2
# China
df.query('Country=="Mainland China"').groupby("Last Update")[['Confirmed', 'Deaths', 
        'Recovered']].sum().reset_index()
# data frame by country
df.groupby("Country")[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index()

# World wide data
confirmed = df.groupby('Date').sum()['Confirmed'].reset_index()
deaths = df.groupby('Date').sum()['Deaths'].reset_index()
recovered = df.groupby('Date').sum()['Recovered'].reset_index()

# Summary Plot of Worldwide Cases - Confirmed, Deaths & Recovered

