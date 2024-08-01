#!/usr/bin/env bash

#[30-07-24] ===========================================================================================
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

# myarray=(foo bar)
# for f in "${myarray[@]}"; do
#     cat "$f"
# done
#========================================================================================================
#[31-07-24]

#while loops
number=1

while [[ $number -le 10 ]]; do
    echo "$number"
    ((number++))
done
echo "Now, number is $number"

#until loops
number=1
until [[ $number -ge 10 ]]; do
    echo "$number"
    ((number++))
done
echo "Now, number is $number"

# arrays
devops_tools=("docker" "kubernetes" "ansible" "terraform" "jenkins")
# shellcheck disable=SC2068
for tool in ${devops_tools[@]}; do
    # shellcheck disable=SC2086
    echo $tool
done

#for loops
echo "Numbers:"
for number in 0 1 2 3 4 5 6 7 8 9; do
    echo $number
done
echo "Names:"
for name in Joe David Matt John Timothy; do
    echo $name
done
echo "Files in current folder:"
for file in $(pwd)/*; do
    echo $file
done

Welcome() {
    echo "Welcome to Linux Lessons $1 $2 $3"
    return 3
}
Welcome Joe Matt Timothy
echo $?

# Welcome() {
#     echo "Welcome to Linux Lessons $1 $2 $3"
# }
# Welcome Joe Matt Timothy

# Declare an associative array
declare -A STAR_PLAYERS

# Add elements to the associative array
STAR_PLAYERS[Argentina]="Messi"
STAR_PLAYERS[Brazil]="Neymar"
STAR_PLAYERS[England]="Kane"

# Print the value of a specific key
echo "${STAR_PLAYERS[Argentina]}" # Outputs: Messi


# Notes , All Varuables should be in ALLCAPS, it shouldn't have any special character except underscore ( _ ) to improve readability
# Always avoid using the function keyword, it reduces compatibility with older versions of bash.

# 
# #!/usr/bin/env bash

# set -o errexit
# set -o pipefail

# readonly something='immutable value'
