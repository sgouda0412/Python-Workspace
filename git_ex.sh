#!/bin/bash

# Check Git status
echo "Checking Git status..."
git status

# Stage all changes
echo "Staging changes..."
git add .

# Commit changes
commit_message="commit"
echo "Committing changes with message: $commit_message"
git commit -m "$commit_message"

# Push changes to the 'features' branch
features_branch="feautures"
echo "Pushing changes to the branch: $features_branch"
git push origin "$features_branch"

# Checkout main branch
echo "Checking out main branch..."
git checkout main

# Pull the latest changes from the main branch
echo "Pulling the latest changes from main branch..."
git pull origin main

# Merge the 'features' branch into the main branch
echo "Merging branch '$features_branch' into main..."
git merge "$features_branch"

# Push the updated main branch to the remote repository
echo "Pushing the updated main branch to the remote repository..."
git push origin main

echo "All operations completed successfully."

echo "checking out to feautures branch"
git checkout "$features_branch"
