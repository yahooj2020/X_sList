#!/bin/bash

for num in {0..9}
do
         ls -i | grep 389$num | xargs rm -rf {}
done
