#!/bin/bash
while :
do
sleep 5
python3 download.py
sleep 5
python3 tx_rx.py
sleep 5
python3 photo.py
sleep 5
python3 upload.py
sleep 5
done