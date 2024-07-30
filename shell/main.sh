#!/usr/bin/env bash

echo "Hello Bash Programming ......"
function sendmail () {
    echo "Hello Bash Programming...." # arguments are accessible through $1, $2,...
}
x=12
y=13

echo $x,$y

sendmail

read -p  "Enter a Number: " a
echo $a


PWD=$(pwd)
BASH_VERSION=`bash --version`
echo $PWD
echo $BASH_VERSION


declare -A sounds
sounds[dog]="bark"
sounds[cow]="moo"
sounds[bird]="tweet"
sounds[wolf]="howl"