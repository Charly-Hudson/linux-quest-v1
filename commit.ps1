$commitMessage = Read-Host -Prompt "What is your Commit Message"

git status
git add .
git commit -m "$commitMessage"
git push
git status
exit