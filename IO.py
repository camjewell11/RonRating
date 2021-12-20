import json
from textwrap import wrap

def getBeerData():
    with open('beer_data.json') as inFile:
        beerData = json.load(inFile)
    inFile.close()
    return fileCleanup(beerData)

def getBeersFromConfig():
    with open('beers_config.json') as inFile:
        beers = json.load(inFile)
    inFile.close()
    return fileCleanup(beers)

def fileCleanup(data):
    return data

def getBeerColors(beerData):
    colors = {}
    for beer in beerData:
        colors[beer] = beerData[beer]["plot_color"]
    return colors

def getBeerType(beers, beerName):
    for beer in beers:
        if beerName == beer:
            return beers[beer]["type"]

beers = getBeerData()
beerData = getBeersFromConfig()
beersToGraph = getBeerColors(beerData)