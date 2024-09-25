# Number of pages in Chapters 3, 3 and 4 Chapter 1 has 35 pages and
# each is double the previous chapter
pages = 35
for i in range(2, 5):
    print("Chapter %s is %s pages long" % (str(i), str(pages * 2)))
    pages *= 2
