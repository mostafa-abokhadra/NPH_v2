#!/bin/bash
# Update package lists and install libmysqlclient-dev
apt-get update
apt-get install -y libmysqlclient-dev
pip install -r requirements.txt