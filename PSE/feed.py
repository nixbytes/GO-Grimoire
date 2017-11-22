#!/usr/bin/python3
import pickle

file = open("lxf-text.txt", "wb")

feeds = "http://www.tuxradar.com/rss"

for feed in feeds:
	file.write("{0}\n".format(feed))
file.close()

# feeds = str(feeds)

# feeds = str(feeds)

with open("lxf-text.txt", "wb") as file:
    pickle.dump(feeds, file)


with open("lxf-text.txt", "r") as file:
    feeds = pickle.load(file)


# 