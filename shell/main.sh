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
number=1

while [[ $number -le 10 ]]; do
    echo "$number"
    ((number++))
done
echo "Now, number is $number"

number=1
until [[ $number -ge 10 ]]; do
    echo "$number"
    ((number++))
done
echo "Now, number is $number"

devops_tools=("docker" "kubernetes" "ansible" "terraform" "jenkins")
# shellcheck disable=SC2068
for tool in ${devops_tools[@]}; do
    # shellcheck disable=SC2086
    echo $tool
done

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
