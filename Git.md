## Git flow

## Apply patches

```bash
# Move the changes from the current branch to a new branch and delete the branch
git diff develop > out.patch
git checkout -b new-branch-name
git apply out.patch
git log
git branch -D old-branch-name
```