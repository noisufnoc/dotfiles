#!/bin/sh 
export PATH=$PATH:/usr/local/bin

# I have to source my zshenv in order to use the env vars below
source ~/.zshenv
# There might be a better way to do this.

# abort if we're already inside a TMUX session
[ "$TMUX" == "" ] || exit 0 

# startup a "default" session if none currently exists
tmux has-session -t _default || tmux new-session -s _default -d

# present menu for user to choose which workspace to open
PS3="Please choose your session: "
options=($(tmux list-sessions -F "#S") "NEW SESSION" "michelangelo" "donatello" "phonehome" "BASH" )
echo "Available sessions"
echo "------------------"
echo " "
select opt in "${options[@]}"
do
    case $opt in
        "NEW SESSION")
            read -p "Enter new session name: " SESSION_NAME
            tmux new -s "$SESSION_NAME"
            break
            ;;
    	"donatello")    
 	    ssh -i $SKELETON_KEY mike@$DONATELLO
	    break;;
    	"michelangelo")    
 	    ssh -i $SKELETON_KEY mike@$MICHELANGELO -t tmux -u attach -t shell
	    break;;
    	"michelangelo x11")    
 	    ssh -Y -i $SKELETON_KEY mike@$MICHELANGELO -t tmux -u attach -t shell
	    break;;
    	"phonehome")    
	    ssh -i $SKELETON_KEY -p 2222 mike@$SSH_JUMPBOX -t 'ssh mike@$MICHELANGELO -t tmux -u attach -t shell'
	    break;;
        "BASH")
            bash --login
            break;;
        *) 
            tmux attach-session -t $opt 
            break
            ;; 
    esac
done    
