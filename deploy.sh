#!/bin/sh
ssh -o StrictHostKeyChecking=no $OVH_USER@$OVH_IP << 'ENDSSH'
  cd /home/ubuntu/myriam
  docker-compose -f docker-compose.prod.yml down -v
  docker-compose -f docker-compose.prod.yml up -d --build
ENDSSH