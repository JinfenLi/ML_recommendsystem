f = open("./data/result.txt", "r")
result = {}
lines = f.readlines()
for item in lines:

    print "item",item
    uid, bid = item.strip("\n").split("\t")
    print "bid",bid
    result[uid] = set(bid.split(","))

f.close()