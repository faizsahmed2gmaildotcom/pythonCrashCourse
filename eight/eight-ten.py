def sendMessages(messages):
    i = 0
    for msg in messages:
        printMsg = f"{msg.title()}"
        print(printMsg)
        sentMsgList.append(msg)
        msgList[i] = 'null'
        i += 1


msgList = ['a', 'b', 'c', 'd', 'e', 'f']
sentMsgList = []
sendMessages(msgList)
print(msgList), print(sentMsgList)
