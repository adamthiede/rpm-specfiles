#!/bin/bash
COPR="adamthiede/bin"
for pkg in $(copr list-packages "$COPR"|jq .[].name -r); do
	echo "Editing $pkg..."
	copr edit-package-scm \
		--clone-url "https://github.com/adamthiede/rpm-specfiles" \
		--spec "${pkg}.spec" \
		--name $pkg \
		$COPR
done
