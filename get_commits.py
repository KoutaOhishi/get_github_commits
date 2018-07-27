#coding:utf-8
#!/usr/bin/env python

import requests, bs4

dic = {
    "documents":"https://github.com/PartnerRobotChallengeVirtual/documents/commits/",
    "human-navigation-unity":"https://github.com/PartnerRobotChallengeVirtual/human-navigation-unity/commits/",
    "interactive-cleanup-unity":"https://github.com/PartnerRobotChallengeVirtual/interactive-cleanup-unity/commits/"
}



for i in dic:
    print dic[i]
