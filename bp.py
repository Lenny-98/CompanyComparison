#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

#Load the data
path = r'Unternehmensvergleich.csv'
df = pd.read_csv(path, encoding='latin-1', sep = ";")

#Set first column as index
df.set_index(df['Unternehmen'])


# In[2]:


df.set_index("Unternehmen")


# In[3]:


list(df.columns)



# In[5]:


company = df['Unternehmen']


option_company = st.multiselect(
     'What companies do you want to compare?', company)


option_dimension = st.selectbox(
     'Which dimension would you like to inspect?',
     ('Gehalt und Sozialleistungen', 'Image', 'Karriere und Weiterbildung', 'Arbeitsatmosphäre', 
      'Kommunikation','Kollegenzusammenhalt','Work-Life-Balance', 'Vorgesetztenverhalten', 
      'Interessante Aufgaben', 'Arbeitsbedingungen','Umwelt- und Sozialbewusstsein', 'Gleichberechtigung', 
      'Umgang mit älteren Kollegen'))


from matplotlib import pyplot as plt

fig, ax = plt.subplots()

#Set colors
data_color = ['#000099', '#009BD2', '#4BD0FF', '#87BC49', '#F5C500', '#FFE060']

# Save the chart so we can loop through the bars below.
bars = ax.bar(
    x=df[company],
    height=df[option_dimension],
    color = data_color
)


# Axis formatting.
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#DDDDDD')
ax.tick_params(bottom=False, left=False)
ax.set_axisbelow(True)
ax.yaxis.grid(True, color='#EEEEEE')
ax.xaxis.grid(False)

# Add text annotations to the top of the bars.
bar_color = 'b'
for bar in bars:
    ax.text(
     bar.get_x() + bar.get_width() / 2,
     bar.get_height() + 0.2,
     round(bar.get_height(), 1),
     horizontalalignment='center',
     color=bar_color,
     weight='bold'
 )

# Add labels and a title.
ax.set_xlabel('Unternehmen', labelpad=15, color='#333333')
ax.set_ylabel('Bewertung', labelpad=15, color='#333333')
ax.set_title('Kununu Bewertungen im Vergleich', pad=15, color='#333333',
             weight='bold')

fig.tight_layout()

st.pyplot(fig)







