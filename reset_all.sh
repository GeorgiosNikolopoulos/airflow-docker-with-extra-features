#!/bin/bash
docker-compose down -v --remove-orphans
rm -r ./grafana/volume/data
rm -r ./prometheus/volume/