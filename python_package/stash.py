stashedFiles="";
unstashedFiles="";
stashing=False;
def stashFiles(stash):
    stashing=True;
    stashedFiles=stash;

def unstashFiles(unstash):
    stashing=False;
    unstashedFiles=unstash;

if stashedFiles != "":
    print("Stashed files: "+stashedFiles+"\nFiles stashed")
    if os.path.exists("stashed.txt"):
        unstashFiles("stashed.txt")
    core=open("stashing.txt")
    core.write(stashedFiles)
    core.close()

if unstashedFiles != "":
    print("Unstashed files: "+unstashedFiles+"\nFiles unstashed")
    core2=open("unstashing.txt")
    core2.write(unstashedFiles)
    core2.close()
