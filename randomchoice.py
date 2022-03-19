import random
import time
from progress.bar import Bar


bar = Bar("Processing", max=3)

attendees = open("attendees3.txt").read()
attendees = attendees.split("\n")

# https://stackoverflow.com/a/6494519/185820
winners = random.sample(attendees, 3)

# print(winners)

for winner in winners:
    time.sleep(3)
    bar.next()
    print("%s!\t\n" % winner)

bar.finish
