#!/usr/bin/python3

file = open("lxf-text.txt", "w")

feeds = ["http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/front_page/rss.xml",
         "http://www.tuxradar.com/rss"]

for feed in feeds:
    file.write("{0}\n".format(feed))
file.close()


with open("lxf-text.txt", "a") as file:
    pickle.dump(feeds, file)


with open("lxf-text.txt", "r") as file
    feeds = pickle.load(file)
