a = input()

string = ""

tier = [4, 3, 2, 1]
tier2 = [0.3, 0.0, -0.3]

tierlist = ["A", "B", "C", "D", "F"]
tierlist2 = ["+", "0", "-"]

if a == "F":
    print("0.0")
else:
    temp = list(a)[0]
    temp2 = list(a)[1]
    print(tier[tierlist.index(temp)] + tier2[tierlist2.index(temp2)])