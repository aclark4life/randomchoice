import random
import time

attendees = open("attendees2.txt").read()
attendees = attendees.split()

# https://stackoverflow.com/a/6494519/185820
winners = random.sample(attendees, 3)

for winner in winners:
    print("Winner: %s!\n" % winner)
    time.sleep(2)
