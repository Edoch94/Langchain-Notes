#!/usr/bin/sh

echo "Adding poetry tab completions to bash_completion"
poetry completions bash >> ~/.bash_completion
echo "Poetry tab completions added to bash_completion"