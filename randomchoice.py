import random

attendees = open("attendees.txt").read()
attendees = attendees.split("\n")

# https://stackoverflow.com/a/6494519/185820
winners = random.sample(attendees, 3)

print(winners)
