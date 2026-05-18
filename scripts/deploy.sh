#!/bin/bash
rsync -avz --exclude 'build/' --exclude '.git/' ~/Development/EcoFlow-Web/ mikkanen@192.168.1.32:/share/Docker/EcoFlow-Web/
# ssh mikkanen@Raspberry5.local "cd ~/Development/EcoFlow-Web/build && make -j$(nproc)"
