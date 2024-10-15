#!/bin/bash

set -e

DOCKER_COMPOSE_FILE="docker-compose.yml"
SERVICES=("playwright-chromium-desktop" "playwright-firefox-desktop" "playwright-webkit-desktop" 
          "playwright-chromium-mobile" "playwright-firefox-mobile" "playwright-webkit-mobile")

echo "Starting Playwright tests using Docker Compose..."
docker-compose -f $DOCKER_COMPOSE_FILE up --build "${SERVICES[@]}"

echo "Playwright tests completed. Collecting logs and artifacts..."

for SERVICE in "${SERVICES[@]}"; do
  docker cp "${SERVICE}:/app/test_results/" "./test_results/${SERVICE}/"
  docker logs "${SERVICE}" > "./logs/${SERVICE}.log"
done

echo "Cleaning up containers..."
docker-compose -f $DOCKER_COMPOSE_FILE down
