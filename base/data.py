import pandas as pd
import numpy as np
from datetime import date, timedelta

df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv')


date_string = df['date']

DF_Date = df['date']
DF_Cases = df['total_cases']
DF_deaths = df['total_deaths']
DF_Continent = df['continent']
DF_country = df['location']
DF_people_vaccinated = df['people_vaccinated']

DF_total = pd.concat([DF_Date, DF_Continent, DF_country, DF_Cases, DF_deaths, DF_people_vaccinated], axis=1)

DF_total.columns = ['Fecha', 'Continente', 'Pais', 'Total contagiados', 'Total fallecidos', 'Total vacunados']


##################################
#### Tabla resumen

yesterday = date.today()-timedelta(days=1)
fecha2 = yesterday.strftime("%Y-%m-%d")
otro = df[df['date'] == fecha2]
Only_world2 = otro[otro['location'] == 'World']
Contagios = Only_world2['total_cases'].sum() 
Total_deaths = Only_world2['total_deaths'].sum()
Vacunados = Only_world2['people_vaccinated'].sum()

total_res_wor = pd.DataFrame({'Contagiados': [Contagios],'Fallecidos': [Total_deaths], 'Vacunados':[Vacunados] ,'Fecha':[fecha2]})
total_res_wor.fillna(0, inplace=True)
total_res_wor.style.hide_index()


##################################
#### contagio fecha

Wd = df[df['location'] == 'World']

##################################
#### Mapa Contagios

otro2 = df[df['date'] == fecha2]
With_world = otro2[otro2['location'] != 'World']
actual = With_world[With_world['location'] != 'International'] 
actual = actual[actual['location'] != 'Europe']
actual = actual[actual['location'] != 'North America']
actual = actual[actual['location'] != 'Asia']
actual = actual[actual['location'] != 'South America']
actual = actual[actual['location'] != 'Africa']
actual = actual[actual['location'] != 'European Union']  
actual = actual[actual['location'] != 'South Africa']
actual = actual[actual['location'] != 'Oceania']  

##################################
#### For cases and deaths select

Wd_cases = Wd['total_cases']
Wd_deaths = Wd['total_deaths']
Wd_people_vaccinated = Wd['people_vaccinated']
Wd_date = Wd['date']

date_cases_deaths = pd.concat([Wd_cases, Wd_deaths, Wd_people_vaccinated, Wd_date],   axis=1)


date_cases_deaths.columns = ['Total contagiados', 'Total fallecidos', 'Total vacunados', 'Fecha']

features = date_cases_deaths.columns

date_cases_deaths.set_index(['Total contagiados', 'Total fallecidos', 'Total vacunados', 'Fecha'])

date_cases_deaths.fillna(0, inplace=True)


##################################
#### For map select

iso = actual['iso_code']
Map_total_cases = actual['total_cases']
Map_total_deaths = actual['total_deaths']
Map_people_vaccinated  = actual['people_vaccinated']
Pais = actual['location']

# Contagiados 

map_cases_deaths = pd.concat([Pais, Map_total_cases], axis=1)

map_cases_deaths.columns = ['Country', 'Total contagiados']

map_cases_deaths.fillna(0, inplace=True)

map_cases_deaths.loc[-1] = ['Country', 'Total contagiados'] 

map_cases_deaths.index = map_cases_deaths.index + 1

map_cases_deaths = map_cases_deaths.sort_index()

# fallecidos

map_final_deaths = pd.concat([Pais, Map_total_deaths], axis=1)

map_final_deaths.columns = ['Country', 'Total fallecidos']

map_final_deaths.fillna(0, inplace=True)

map_final_deaths.loc[-1] = ['Country', 'Total fallecidos'] 

map_final_deaths.index = map_final_deaths.index + 1

map_final_deaths = map_final_deaths.sort_index()

# Vacuandos

map_final_vaccins = pd.concat([Pais, Map_people_vaccinated], axis=1)

map_final_vaccins.columns = ['Country', 'Total vacunados']

map_final_vaccins.fillna(0, inplace=True)

map_final_vaccins.loc[-1] = ['Country', 'Total vacunados'] 

map_final_vaccins.index = map_final_vaccins.index + 1

map_final_vaccins = map_final_vaccins.sort_index()


##################################
#### For country select

Country_total_cases = actual['total_cases']
Country_total_deaths = actual['total_deaths']
Country_total_people_vaccinated = actual['people_vaccinated']
Pais = actual['location']

Country_total_cases_deaths = pd.concat([Country_total_cases, Country_total_deaths, Country_total_people_vaccinated, Pais], axis=1)

Country_total_cases_deaths.columns = ['Total contagiados', 'Total fallecidos', 'Total vacunados', 'Pais']

##################################
#### For continent select

Continent_total_cases = actual['total_cases']
Continent_total_deaths = actual['total_deaths']
Continent_total_people_vaccinated = actual['people_vaccinated']
Continente = actual['continent']

Continent_total_cases_deaths = pd.concat([Continent_total_cases, Continent_total_deaths, Continent_total_people_vaccinated, Continente], axis=1)

Continent_total_cases_deaths.columns = ['Total contagiados', 'Total fallecidos', 'Total vacunados', 'Continente']

Continent_total_cases_deaths.fillna(0, inplace=True)

##################################
#### for table

# table1 = pd.concat([Pais, Continente, Country_total_cases, Country_total_deaths, Country_total_people_vaccinated], axis=1)

# table1.columns = ['País', 'Continente','Total_contagiados', 'Total_fallecidos', 'Total_vacunados']

table1 = pd.concat([Pais, Country_total_cases, Country_total_deaths, Country_total_people_vaccinated], axis=1)

table1.columns = ['País','Total_contagiados', 'Total_fallecidos', 'Total_vacunados']