#!/bin/sh

echo "[MERGE] Starting"

cd /opt/app/

while :
do
  sort -u stash.txt out/paths.txt | sponge out/paths.txt
done

echo "[MERGE] Done"
