import random

# https://stackoverflow.com/a/6494519/185820

attendees = open("attendees.txt").read()
print(random.sample(attendees, 3))
