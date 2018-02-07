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

if unstashedFiles != "":
    print("Unstashed files: "+unstashedFiles+"\nFiles unstashed")
