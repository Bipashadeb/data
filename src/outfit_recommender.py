import json

def load_outfits():
    with open('../data/outfit_options.json', 'r') as file:
        return json.load(file)
    

def recommender_outfit(temp, weather_desc):
    outfits = load_outfits()

    if temp < 10 :
        return outfits['cold']
    elif 10 <= temp<= 20:
        return outfits['cold']
    elif 20 < temp <= 30:
        return outfits['warrm']
    else:
        return outfits['hot']