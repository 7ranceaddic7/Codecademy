#!/bin/bash
clear

greeting="Greetings and Falicitations!"
echo "$greeting"

read -ra firstline <<< "$(head -n1 ./source/changelog.md)"
version=${firstline[1]}
echo "$version"


versioncontinue=9

while [ $versioncontinue -eq 9 ]
do
echo "Is this version correct?"
echo "Enter '1' (for yes) to continue or '0' (for no) to exit"
read -r versioncontinue
  if [ "$versioncontinue" -eq 1 ]; then
    echo "Okie Dokie. Here we go ..."
    for file in source/*
    do
      if [ "$file" == 'source/secretinfo.md' ]
        then echo "$file not copied."
        else
        echo "$file copied."
        cp "${file}" build/.
      fi
    done
    echo "Required files copied."
    echo "Build version $version contains:"
    ls -1 ./build/*
  else
    echo "Laterz."
    break
  fi
done
