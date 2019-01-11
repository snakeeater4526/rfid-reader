#!/bin/bash

ipetmasque='10.1.1.24/24'
sudo sed -i "42s/#static ip_address=192.168.0.10\/24/static ip_address=$ipetmasque/" /etc/dhcpcd.conf
