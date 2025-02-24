#!/bin/bash

mkdir test test/archive test/main test/main/file-1 test/main/file-2

wget <git-repo> 
mv files/file-1 test/main/file-1
mv files/file-2 test/main/file-2

