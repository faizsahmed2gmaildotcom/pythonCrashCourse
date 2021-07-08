lords = ['Burp', 'Pee', 'Fart', 'Puu']
input(lords)
input('INCOMING LORD...')

lords.append('Math Blurfer')
input(lords)
input("Huh??? No! Get rid of 'it'!!!")

tooInsane = 'Math Blurfer'
lords.remove(tooInsane)
print(lords)
input('Ahh, yes. Much better!')
input(f"\nThe {tooInsane.title()} was banished many commits ago.")

input("Anyways, we are inviting " + str(len(lords)) + " lords now.")
input(lords)
input("Well, that's UG-LEH! Let's sort it by alphabetical order.")
input(sorted(lords))
poppedLords = lords.pop(0)
input(lords)
input("Heh? Wat happened?! Let's put that back in.")
lords.append(poppedLords)
input(sorted(lords))
input('Bye.')
