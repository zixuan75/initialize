stashedFiles="";
unstashedFiles="";
stashing=false;
def stashFiles(stash):
    stashing=true;
    stashedFiles=stash;

def unstashFiles(unstash):
    stashing=false;
    unstashedFiles=unstash;

if stashedFiles != "":
    print("Stashed files: "+stashedFiles+"\nFiles stashed")
    if (os.path.exists("stashed.txt") ):
        unstashFiles("stashed.txt")

if unstashedFiles != "":
    print("Unstashed files: "+unstashedFiles+"\nFiles unstashed")
