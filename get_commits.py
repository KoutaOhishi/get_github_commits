#coding:utf-8
#!/usr/bin/env python

import requests, bs4, os

def get_commits_list(repo_name, URL):
    res = requests.get(URL)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    elems = soup.select("a")

    new_commit_list = []
    old_commit_list = []

    file_path = "txt/" + repo_name + ".txt"

    f_r = open(file_path, "r")

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

    if new_commit_list == old_commit_list:
        print "There are no new commits."

    else:
        print "There are some NEW commits."
        f_w = open(file_path, "w")

        for i in new_commit_list:
            #print i
            f_w.write(str(i) + "\n")

        f_w.close()


def main():
    repo_list = {
        "documents":"https://github.com/PartnerRobotChallengeVirtual/documents/commits/",
        "human-navigation-unity":"https://github.com/PartnerRobotChallengeVirtual/human-navigation-unity/commits/",
        "interactive-cleanup-unity":"https://github.com/PartnerRobotChallengeVirtual/interactive-cleanup-unity/commits/"

    }

    slack_token = "xoxp-41888577685-164597196115-360693330051-bba97f8524c1065e466011d7535de70a"



    for i in repo_list:
        #print i
        print repo_list[i]
        get_commits_list(i, repo_list[i])


if __name__ == "__main__":
    main()
