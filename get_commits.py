#coding:utf-8
#!/usr/bin/env python

import requests, bs4, os
import json

def get_commits_list(repo_name, URL):
    res = requests.get(URL)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    elems = soup.select("a")

    new_commit_list = []
    old_commit_list = []

    file_path = "./txt/" + repo_name + ".txt"

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
        return True

    else:
        print "There are some NEW commits."
        f_w = open(file_path, "w")

        for i in new_commit_list:
            #print i
            f_w.write(str(i) + "\n")

        f_w.close()
        return False

def slack_notice(repo_name, URL):
    web_hook = "hoge"

    message = "New Commits!\n" + repo_name + " : [" + URL + "]"

    requests.post(web_hook, data = json.dumps({
        'text': message, # 投稿するテキスト
        'username': u'Ghost', # 投稿のユーザー名
        'icon_emoji': u':ghost:', # 投稿のプロフィール画像に入れる絵文字
        'link_names': 1, # メンションを有効にする
    }))

def main():
    repo_list = {
        "documents":"https://github.com/PartnerRobotChallengeVirtual/documents/commits/",
        "human-navigation-unity":"https://github.com/PartnerRobotChallengeVirtual/human-navigation-unity/commits/",
        "human-navigation-unity_develop":"https://github.com/PartnerRobotChallengeVirtual/human-navigation-unity/commits/develop",
        "interactive-cleanup-unity":"https://github.com/PartnerRobotChallengeVirtual/interactive-cleanup-unity/commits/",
        "interactive-cleanup-unity_develop":"https://github.com/PartnerRobotChallengeVirtual/interactive-cleanup-unity/commits/develop",
        "common-unity":"https://github.com/PartnerRobotChallengeVirtual/common-unity",
        "common-unity_develop":"https://github.com/PartnerRobotChallengeVirtual/common-unity/commits/develop",
        "handyman-unity":"https://github.com/PartnerRobotChallengeVirtual/handyman-unity/commits",
        "handyman-unity_develop":"https://github.com/PartnerRobotChallengeVirtual/handyman-unity/commits/develop",
        "console-simple-tts":"https://github.com/PartnerRobotChallengeVirtual/console-simple-tts/commits",
        "interactive-cleanup-ros":"https://github.com/PartnerRobotChallengeVirtual/interactive-cleanup-ros/commits",
        "handyman-ros":"https://github.com/PartnerRobotChallengeVirtual/handyman-ros/commits",
        "human-navigation-ros":"https://github.com/PartnerRobotChallengeVirtual/human-navigation-ros/commits"
    }

    for i in repo_list:
        #print i
        #print repo_list[i]
        res = get_commits_list(i, repo_list[i])
        if res == False:
            """新しいcommitの通知"""
            slack_notice(i, repo_list[i])




if __name__ == "__main__":
    main()
