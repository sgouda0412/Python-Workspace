#!/usr/bin/env bash

# read -p "Enter a number: " number

# if [[ $number -gt 20 ]]
# then
#     echo "$number is greather"
# fi

#We can use Relational Operators, String \ 
# Operators or File Test Operators inside the square brackets ( [ ] ) in the if statement above.


# read -p "Input first number: " first_number
# read -p "Input second number: " second_number
# read -p "Select an math operation
# 1 - addition
# 2 - subtraction
# 3 - multiplication
# 4 - division
# " operation
# case $operation in
#   "1") 
#      echo "result= $(( $first_number + $second_number))"
#   ;;
#   "2")
#      echo "result= $(( $first_number - $second_number))"
#   ;;
#   "3")
#      echo "result= $(( $first_number * $second_number))" 
#      ;;
#   "4")
#      echo "result= $(( $first_number / $second_number))"
#   ;;
#   *)
#      echo "Wrong choice..." 
#   ;;
# esac
mem(){
    ls -la
}
sys(){
    date
}
cal(){
    ls -ltrh
}
while getopts 'abc' OPTION; do
    case "$OPTION" in
        a)
            mem
            ;;
        b)
            sys
            ;;
        c) 
            cal
            ;;
    esac
done

function_one () {
   echo "This is from the first function"
   function_two
}
function_two () {
   echo "This is from the second function"
}
function_one


file_count=$(ls | wc -l)
echo "Number of files: $file_count"