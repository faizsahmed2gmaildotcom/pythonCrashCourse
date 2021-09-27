def sendMessages(messages):
    i = 0
    for msg in messages:
        printMsg = f"{msg.title()}"
        print(printMsg)
        sentMsgList.append(msg)
        msgListCopy[i] = 'null'
        i += 1


msgList = ['a', 'b', 'c', 'd', 'e', 'f']
msgListCopy = ['a', 'b', 'c', 'd', 'e', 'f']
sentMsgList = []
sendMessages(msgListCopy)
print(f"Copy list: {msgListCopy}"), print(f"Original list: {msgList}"), print(f"Sent list: {sentMsgList}")
