#!/usr/bin/env python
# coding: utf-8

# In[60]:


import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

import streamlit as st
import streamlit.components.v1 as components


# In[61]:


#Download Kununu and BMW Icon

bmw_logo = "https://upload.wikimedia.org/wikipedia/commons/4/44/BMW.svg"
kununu_logo = "https://2p9gg33w24r1kgv74eqo6qrl-wpengine.netdna-ssl.com/wp-content/uploads/2021/11/kununu_logo_black.png"

# Display header.
st.markdown("<br>", unsafe_allow_html=True)
st.image(bmw_logo, width=80)
st.image(kununu_logo, width=80)

"""
# Analyse von Arbeitnehmerbewertungen von Kununu für die BMW AG

Mit Hilfe von Webscraping haben wir uns sämtliche Bewertungen von aktuellen bzw. ehemaligen Mitarbeitern der BMW AG von Kununu
heruntergeladen und aufbereitet. Die Datenbasis repräsentiert sämtliche Bewertungen und zugehörige Informationen, die auf Kununu
frei einsehbar sind.
"""


# In[62]:



#Establish a connection to Tableau Dashboard published on Tableau Online
def main():
    html_temp = """<script type='text/javascript' src='https://dub01.online.tableau.com/javascripts/api/viz_v1.js'></script><div class='tableauPlaceholder' style='width: 1920px; height: 1003px;'><object class='tableauViz' width='1920' height='1003' style='display:none;'><param name='host_url' value='https%3A%2F%2Fdub01.online.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='&#47;t&#47;tableaumhp' /><param name='name' value='BMW_KUNUNU&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='showAppBanner' value='false' /></object></div>"""
    st.components.v1.html(html_temp, width = 10000, height = 1000, scrolling = True)
if __name__ == "__main__":    
    main()


# In[63]:




#Load the data
path = r'Unternehmensvergleich.csv'
df = pd.read_csv(path, encoding='latin-1', sep = ";")

#Set first column as index
df.set_index(df['Unternehmen'])


# In[64]:


df.set_index("Unternehmen")


# In[65]:


list(df.columns)


# In[66]:


company = df['Unternehmen']

#Multiselect option
option_company = st.multiselect('What companies do you want to compare?', company)


#Selectbox option
option_dimension = st.selectbox(
     'Which dimension would you like to inspect?',
     ('Gehalt und Sozialleistungen', 'Image', 'Karriere und Weiterbildung', 'Arbeitsatmosphäre', 
      'Kommunikation','Kollegenzusammenhalt','Work-Life-Balance', 'Vorgesetztenverhalten', 
      'Interessante Aufgaben', 'Arbeitsbedingungen','Umwelt- und Sozialbewusstsein', 'Gleichberechtigung', 
      'Umgang mit älteren Kollegen'))

#Convert the string output of option_dimension to a list
chosen_object = [option_dimension]

#Create Subset to be able to access values in barplot
selected_df = df[df['Unternehmen'].isin(option_company)]



print(selected_df)

from matplotlib import pyplot as plt

fig, ax = plt.subplots()

#Set colors
data_color = ['#000099', '#009BD2', '#4BD0FF', '#87BC49', '#F5C500', '#FFE060']

# Save the chart so we can loop through the bars below.
bars = ax.bar(
    x= selected_df["Unternehmen"],
    height= selected_df[option_dimension],
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
#bar_color = 'b'
#for bar in bars:
#    ax.text(
 #    bar.get_x() + bar.get_width() / 2,
 #    bar.get_height() + 0.2,
 #    round(bar.get_height(), 1),
 #    horizontalalignment='center',
 #    color=bar_color,
 #    weight='bold'
 #)

# Add labels and a title.
ax.set_xlabel('Companies', labelpad=15, color='#333333')
ax.set_ylabel('Rating', labelpad=15, color='#333333')
ax.set_title('Company Comparison', pad=15, color='#333333',
             weight='bold')

fig.tight_layout()

st.pyplot(fig)


# In[ ]:





# In[ ]:





# In[ ]:




