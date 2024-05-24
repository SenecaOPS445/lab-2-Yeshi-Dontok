#!/usr/bin/env python3

#Autor: Yeshi Dhontok Lama	
#Author ID: 131348211
#Date Created: 2024/05/24

import sys

if len(sys.argv) == 1:
    timer = 3
elif len(sys.argv) == 2:
    timer = int(sys.argv[1])
else:
    print("timer")
    sys.exit(1)
while timer !=0:
    print(timer)
    timer = timer - 1

print('blast off!') 
