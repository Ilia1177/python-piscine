#!/usr/bin/env bash

set -euo pipefail

REMOTE="origin"
MAIN_BRANCH="main"

git checkout "$MAIN_BRANCH"
git fetch "$REMOTE"

for n in {0..9}; do
    i=$(printf "%02d" "$n")
    BRANCH="python-$i"
    FOLDER="python$i"

    if git show-ref --verify --quiet "refs/remotes/$REMOTE/$BRANCH"; then
        echo "Copying $BRANCH into $FOLDER/"

        rm -rf "$FOLDER"
        mkdir -p "$FOLDER"

        git archive "$REMOTE/$BRANCH" | tar -x -C "$FOLDER"
    else
        echo "Skipping $BRANCH (not found)"
    fi
done

echo "Done!"

