from bubble_sort import bubble_sort
from quick_sort import quick_sort
import pandas as pd
import json

def serializeDeaths(deaths):
    data = {
        "General deaths" : [],
        "Suicides registered." : [],
        "Deaths by homicide" : [],
        "Deaths of infants younger than one year" : [],
    }
    for death in deaths:
        death['value'] = float(death['value'])
        if len(data[death['indicator']]) < 5000:
            data[death['indicator']].append(death)
    

    quick_sort(data['Deaths by homicide'],0,len(data['Deaths by homicide'])-1)
    quick_sort(data['Deaths of infants younger than one year'],0,len(data['Deaths of infants younger than one year'])-1)
    bubble_sort(data['General deaths'])
    bubble_sort(data['Suicides registered.'])

    final_array = []
    for i in data.values():
        final_array.extend(i)
    return final_array
