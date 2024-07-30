#!/bin/bash

# Check Git Status
echo "Checking Git status..."
git status

# Stage Changes
echo "Staging changes..."
git add .

# Commit Changes
read -p "Enter commit message: " commit_message
git commit -m "$commit_message"

# Push to Branch
read -p "Enter branch name to push to: " branch_name
git push origin "$branch_name"

# Merge Branch
read -p "Enter branch name to merge: " merge_branch_name
git checkout main  # or the target branch
git pull origin main
git merge "$merge_branch_name"

echo "Done!"
