
def buildCar(name, company, **carInfo):
    carInfo['carName'] = name
    carInfo['carCompany'] = company
    return carInfo


carProfile = buildCar('Poo', 'Road Killer', sellLocation = 'baskerville', uses = 'methane generator', origin = '???')
print(carProfile)
