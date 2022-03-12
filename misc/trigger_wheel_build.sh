#!/bin/bash -eux

# Trigger a build of mypyc compiled mypy wheels by updating the mypy
# submodule in the git repo that drives those builds.

# $WHEELS_PUSH_TOKEN is stored in Github Settings and is an API token
# for the mypy-build-bot account.

COMMIT=$(git rev-parse HEAD)
pip install -r mypy-requirements.txt
V=$(python3 -m mypy --version)
V=$(echo "$V" | cut -d" " -f2)

git clone https://${WHEELS_PUSH_TOKEN}@github.com/mypyc/mypy_mypyc-wheels.git build
cd build
git config user.email "nobody"
git config user.name "mypy wheels autopush"
echo $COMMIT > mypy_commit
git commit -am "Build wheels for mypy $V"
git tag v$V
# Push a tag, but no need to push the change to master
git push --tags
