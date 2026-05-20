#!/bin/bash
rsync -avz --exclude 'build/' --exclude '.git/' ~/Development/EcoFlow-Web/ mikkanen@192.168.1.32:/share/Docker/EcoFlow-Web/
# rsync -avz --exclude 'build/' --exclude '.git/' ~/Development/EcoFlow-Web/ mikkanen@192.168.1.32:/share/Docker/ecoflow-app-5002/
# ssh mikkanen@Raspberry5.local "cd ~/Development/EcoFlow-Web/build && make -j$(nproc)"
