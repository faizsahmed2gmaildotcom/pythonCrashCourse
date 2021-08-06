def buildProfile(first, last, **userInfo):
    userInfo['firstName'] = first
    userInfo['lastName'] = last
    return userInfo


userProfile = buildProfile('Poo', 'Fart', location = 'baskerville', profession = 'methane generator', origin = '???')
print(userProfile)
