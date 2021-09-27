def showMessages(messages):
    for msg in messages:
        printMsg = f"{msg.title()}"
        print(printMsg)


msgList = ['a', 'b', 'c', 'd', 'e', 'f']
showMessages(msgList)
