import random
import time

attendees = open("attendees4.txt").read().split()

# https://stackoverflow.com/a/6494519/185820
winners = random.sample(attendees, 1)

# Add suspense
for winner in winners:
    time.sleep(2)
    print("Winner: %s!\n" % winner)
