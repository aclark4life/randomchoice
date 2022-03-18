import random

# https://stackoverflow.com/a/6494519/185820

attendees = open("attendees.txt").read()
attendees = attendees.split("\n")
print(random.sample(attendees, 3))
