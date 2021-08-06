responses = {}

pollingTrue = True
while pollingTrue:
    name = input("\nWhat's your name?")
    response = input("Where would you like to go someday?")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (Yes/No)")
    if repeat == 'no':
        pollingTrue = False

print("\nPoll Results")
for name, response in responses.items():
    print(f"{name.title()} would like to visit {response.title()}.")
