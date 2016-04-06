noc = parse(NOC)

print "How many characters are in the NOC list?"
print "----------------------------------------"
print len(noc)
print
# +- 800

print "What is the distribution of political views in the NOC list?"
print "------------------------------------------------------------"
print freq(col(noc, "Politics"))
print

print "Which characters wear a hat?"
print "----------------------------"
for r in noc: # {"Character": "Daniel Day-Lewis", "Seen Wearing": ["stove-pipe hat"]}
    for v in r["Seen Wearing"]:
        if "hat" in v:
            print r["Character"]
            break
print
# Abraham Lincoln, Jack Sparrow, ...

print "Which characters are astronauts?"
print "--------------------------------"
jobs = index(noc, "Category", unique=False)
for r in jobs["Astronaut"]:
    print r["Character"]
print
# Buzz Aldrin, Mr. Spock, ...

print "Which characters are ugly?"
print "--------------------------"
traits1 = index(noc, "Positive Talking Points", unique=False)
traits2 = index(noc, "Negative Talking Points", unique=False)
traits = {}
traits.update(traits1)
traits.update(traits2)
for r in traits["ugly"]:
    print r["Character"]
print
# Jabba the Hutt, Freddy Krueger, ...

print "What do rich people wear?"
print "-------------------------"
clothes = []
for r in traits["rich"]:
    clothes.append(r["Seen Wearing"])
for x in freq(clothes):
    print x
print
# sharp suit, three-piece suit, ...

print "What do bad guys do?"
print "--------------------"
seen = set()
activities = []
for k in traits:
    if k in ("cruel", "sadistic", "cold", "traitorous"):
        for r in traits[k]:
            if r["Character"] not in seen:
                # Multiple traits may point to a character,
                # so we need to make sure we don't count it twice.
                seen.add(r["Character"])
                activities.append(r["Typical Activity"])
for x in freq(activities):
    print x
print
# devise evil schemes, backstabbing, ...

print "What are the most common properties in the NOC list?"
print "----------------------------------------------------"
properties = []
for r in noc:
    for p in r["Positive Talking Points"]:
        properties.append(p)
    for p in r["Negative Talking Points"]:
        properties.append(p)
for count, p in freq(properties, top=25):
    print count, "\t", p
print
