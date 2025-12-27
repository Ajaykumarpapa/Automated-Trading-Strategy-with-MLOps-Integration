#!/bin/bash

# Docker Deployment Script
# Usage: ./scripts/deploy-docker.sh [docker-hub-username]

set -e

DOCKER_USERNAME=${1:-yourusername}
IMAGE_NAME="trading-strategy"
VERSION=${2:-latest}

echo "🐳 Building and Deploying Docker Image..."
echo "=========================================="

# Build image
echo "🔨 Building Docker image..."
docker build -t $IMAGE_NAME:$VERSION .

# Tag image
echo "🏷️  Tagging image..."
docker tag $IMAGE_NAME:$VERSION $DOCKER_USERNAME/$IMAGE_NAME:$VERSION
docker tag $IMAGE_NAME:$VERSION $DOCKER_USERNAME/$IMAGE_NAME:latest

# Login to Docker Hub
echo "📝 Logging in to Docker Hub..."
docker login

# Push to Docker Hub
echo "⬆️  Pushing to Docker Hub..."
docker push $DOCKER_USERNAME/$IMAGE_NAME:$VERSION
docker push $DOCKER_USERNAME/$IMAGE_NAME:latest

echo ""
echo "✅ Docker image published successfully!"
echo "========================================"
echo "Image: $DOCKER_USERNAME/$IMAGE_NAME:$VERSION"
echo ""
echo "To pull and run:"
echo "docker pull $DOCKER_USERNAME/$IMAGE_NAME:latest"
echo "docker run -p 8501:8501 $DOCKER_USERNAME/$IMAGE_NAME:latest"
