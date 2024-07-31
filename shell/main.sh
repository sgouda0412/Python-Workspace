#!/usr/bin/env bash

echo "Hello Bash Programming ......"
function sendmail() {
    echo "Hello Bash Programming...." # arguments are accessible through $1, $2,...
}
x=12
y=13

echo $x,$y

sendmail

read -r -p "Enter a Number: " a
echo "$a"

PWD=$(pwd)
BASH_VERSION=$(bash --version)
echo "$PWD"
echo "$BASH_VERSION"

myarray=(foo bar)
for f in "${myarray[@]}"; do
    cat "$f"
done
git config --global core.autocrlf true
