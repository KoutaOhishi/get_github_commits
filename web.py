#coding:utf-8
#!/usr/bin/env python

import requests, bs4
res = requests.get('https://github.com/PartnerRobotChallengeVirtual/documents/commits/master')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")

elems = soup.select("a")

new_commit_list = []
old_commit_list = []

f_r = open("document.txt", "r")
for x in f_r:
    old_commit_list.append(x.rstrip("\n"))
f_r.close()

for elem in elems:
    if elem.get("title") != None:
        if elem.get("title") == "GitHub":
            pass
        else:
            new_commit_list.append(elem.get("title"))

    else:
        pass

print new_commit_list
print "-----"
print old_commit_list

print new_commit_list == old_commit_list


"""
f_w = open("document.txt", "w")

for i in new_commit_list:
    print i
    f_w.write(str(i) + "\n")

f_w.close()
"""
