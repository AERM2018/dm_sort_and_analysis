import pandas as pd
from api_requests import getDeaths

death_data = getDeaths(200000)

df = pd.DataFrame(death_data)
df = df.dropna()
df = pd.crosstab(index=df['indicator'],columns=df['year'],values=df['value'],aggfunc='mean')

# Generate html view
out_file = open("./output.html",'w')
out_file.write(df.to_html())
out_file.close()

