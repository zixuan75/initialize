stashedFiles="";
unstashedFiles="";
stashing=false;
def stashFiles(stash):
    stashing=true;
    stashedFiles=stash;

def unstashFiles(unstash):
    stashing=false;
    unstashedFiles=unstash;