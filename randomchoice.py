import random
import time
from progress.bar import Bar


bar = Bar("Processing", max=3)

attendees = open("attendees3.txt").read()
attendees = attendees.split()

# https://stackoverflow.com/a/6494519/185820
winners = random.sample(attendees, 3)

print(winners)

# for winner in winners:
#     # bar.next()
#     print("Winner: %s!\n" % winner)
#     time.sleep(1)

bar.finish
