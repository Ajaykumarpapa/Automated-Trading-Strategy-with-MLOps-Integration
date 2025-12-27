#!/bin/bash

# Google Cloud Platform Deployment Script
# Usage: ./scripts/deploy-gcp.sh [project-id]

set -e

PROJECT_ID=${1}

if [ -z "$PROJECT_ID" ]; then
    echo "Usage: ./scripts/deploy-gcp.sh [project-id]"
    exit 1
fi

IMAGE_NAME="trading-strategy"
REGION="us-central1"

echo "☁️  Deploying to Google Cloud Run..."
echo "===================================="

# Set project
echo "🔧 Setting GCP project..."
gcloud config set project $PROJECT_ID

# Build and push to Container Registry
echo "🔨 Building and pushing to GCR..."
gcloud builds submit --tag gcr.io/$PROJECT_ID/$IMAGE_NAME

# Deploy to Cloud Run
echo "🚀 Deploying to Cloud Run..."
gcloud run deploy $IMAGE_NAME \
  --image gcr.io/$PROJECT_ID/$IMAGE_NAME \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated \
  --port 8501 \
  --memory 1Gi \
  --cpu 1

# Get service URL
SERVICE_URL=$(gcloud run services describe $IMAGE_NAME --platform managed --region $REGION --format 'value(status.url)')

echo ""
echo "✅ Deployment to Google Cloud Run successful!"
echo "============================================="
echo "Service URL: $SERVICE_URL"
echo ""
echo "View logs: gcloud logging read 'resource.type=cloud_run_revision AND resource.labels.service_name=$IMAGE_NAME'"
