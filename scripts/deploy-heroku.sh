#!/bin/bash

# Deploy to Heroku Script
# Usage: ./scripts/deploy-heroku.sh [app-name]

set -e

APP_NAME=${1:-trading-strategy-app}

echo "🚀 Deploying to Heroku..."
echo "=========================="

# Check if Heroku CLI is installed
if ! command -v heroku &> /dev/null; then
    echo "❌ Heroku CLI not found. Installing..."
    curl https://cli-assets.heroku.com/install.sh | sh
fi

# Login to Heroku
echo "📝 Logging in to Heroku..."
heroku login

# Check if app exists, if not create it
if heroku apps:info --app $APP_NAME &> /dev/null; then
    echo "✓ App '$APP_NAME' already exists"
else
    echo "📦 Creating new Heroku app: $APP_NAME"
    heroku create $APP_NAME
fi

# Set buildpack
echo "🔧 Setting buildpack..."
heroku buildpacks:set heroku/python --app $APP_NAME

# Deploy
echo "🚢 Deploying application..."
git push heroku $(git branch --show-current):main

# Scale dyno
echo "📊 Scaling dyno..."
heroku ps:scale web=1 --app $APP_NAME

# Get app URL
APP_URL=$(heroku apps:info --app $APP_NAME | grep "Web URL" | awk '{print $3}')

echo ""
echo "✅ Deployment successful!"
echo "=========================="
echo "App URL: $APP_URL"
echo ""
echo "View logs: heroku logs --tail --app $APP_NAME"
echo "Open app:  heroku open --app $APP_NAME"
