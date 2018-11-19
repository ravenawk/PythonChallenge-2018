#!/usr/bin/env python

import re


message = r"""Gi0/2                        connected    16         a-full a-1000 10/100/1000BaseTX
Gi0/3                        connected    206        a-half   a-10 10/100/1000BaseTX
Gi0/4                        connected    16         a-full a-1000 10/100/1000BaseTX
Gi0/5                        connected    16         a-full  a-100 10/100/1000BaseTX
Gi0/6                        connected    16         a-full a-1000 10/100/1000BaseTX
Gi0/7                        notconnect   3            auto   auto 10/100/1000BaseTX
Gi0/8                        connected    16         a-full a-1000 10/100/1000BaseTX
Gi0/9                        connected    16         a-full a-1000 10/100/1000BaseTX
Gi0/10                       connected    26         a-full a-1000 10/100/1000BaseTX
Gi0/11                       connected    16         a-full a-1000 10/100/1000BaseTX"""

newmessage = message.split("\n")
for i in newmessage:
    tenmeg = re.compile(r'a-10\s')
    mo = tenmeg.search(i)
    if mo != None:
        print(f"Another - {i}")

tenmeg = re.compile(r'a-10\s')
mo = tenmeg.search(message)
print(mo.group())
