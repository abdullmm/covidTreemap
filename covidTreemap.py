import pandas as pd
import matplotlib.pyplot as plt
# pip install squarify
import squarify
# pip install mplcursors
import mplcursors
import datetime
import numpy as np

# get yesterdays date
now = now =datetime.date.today()
days = datetime.timedelta(2)
now = now - days

# Import Data
df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv', parse_dates=['date'])

# filter recent date
df = df.loc[df.date == str(now)]
# I add this to filter out Guam and Puerto Rico
states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas',
          'California', 'Colorado', 'Connecticut', 'Delaware',
          'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois',
          'Indiana', 'Iowa',
          'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
          'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
          'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
          'New Jersey', 'New Mexico', 'New York', 'North Carolina',
          'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
          'Rhode Island', 'South Carolina','South Dakota', 'Tennessee',
          'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
          'West Virginia', 'Wisconsin', 'Wyoming']
# a dictionary for each state and its abbreviation
statesAbbr = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

# filter out Guam and PR
df = df[df['state'].isin(states)]

# add state abbreviation column
df['abbr']=''

# set state abbreviation
for key in statesAbbr:
    df.loc[df['state'] == key, 'abbr'] = statesAbbr[key] 

            
# Prepare Data
df = df.groupby(['cases','abbr','state','deaths']).size().reset_index(name='counts')
labels = df.apply(lambda x: str(x[2]) +"\nCases: "+ str(x[0]) + "\nDeaths: "+str(x[3]), axis=1)
labels2 = df.apply(lambda x: str(x[1]), axis=1)
sizes = df['cases'].values.tolist()
colors = [plt.cm.Spectral(i/float(len(labels))) for i in range(len(labels))]

# Draw Plot
plt.figure(figsize=(20,12), dpi= 90)
squarify.plot(sizes=sizes, label=labels2, color=colors, alpha=.95)

# shows the cases and deaths as you hover over a box
cursor = mplcursors.cursor(hover=True)
cursor.connect("add", lambda sel: sel.annotation.set_text(
    f"{labels[sel.target.index]}"))


# Label and show
plt.title('Treemap of Covid Cases By State \n Date: '+str(now))
plt.axis('off')
plt.show()





















