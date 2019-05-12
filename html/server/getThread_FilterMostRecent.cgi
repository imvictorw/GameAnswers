#!/bin/sh
cd "`dirname "$0"`"
. ~suits/pub/init.sh
python getThread_FilterMostRecent.py
