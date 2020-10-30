if [ ! "$(uname)" == "Darwin" ]
then
    if [ "$(uname -r)"=~"microsoft" ] 
    then 
        export OS_VARIANT='wsl' 
    else
        export OS_VARIANT='linux'
    fi
else 
    export OS_VARIANT='mac'
fi
# elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]