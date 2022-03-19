import random
import time
from progress.bar import Bar


bar = Bar("Processing", max=3)

attendees = open("attendees3.txt").read()
attendees = attendees.split("\n")

# https://stackoverflow.com/a/6494519/185820
winners = random.sample(attendees, 2)

# print(winners)

for winner in winners:
    time.sleep(1)
    print("\n")
    bar.next()
    print("%s!\n" % winner)

bar.finish
