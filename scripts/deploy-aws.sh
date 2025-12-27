#!/bin/bash

# AWS EC2 Deployment Script
# Usage: ./scripts/deploy-aws.sh [ec2-instance-ip] [key-file.pem]

set -e

EC2_IP=$1
KEY_FILE=$2

if [ -z "$EC2_IP" ] || [ -z "$KEY_FILE" ]; then
    echo "Usage: ./scripts/deploy-aws.sh [ec2-instance-ip] [key-file.pem]"
    exit 1
fi

echo "☁️  Deploying to AWS EC2..."
echo "=========================="

# Copy files to EC2
echo "📤 Copying files to EC2..."
scp -i $KEY_FILE -r . ubuntu@$EC2_IP:~/trading-strategy/

# SSH and deploy
echo "🚀 Deploying on EC2..."
ssh -i $KEY_FILE ubuntu@$EC2_IP << 'EOF'
cd ~/trading-strategy

# Update system
sudo apt update

# Install Docker if not installed
if ! command -v docker &> /dev/null; then
    echo "Installing Docker..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker ubuntu
fi

# Stop existing container
docker stop trading-app 2>/dev/null || true
docker rm trading-app 2>/dev/null || true

# Build and run new container
docker build -t trading-strategy .
docker run -d -p 8501:8501 --name trading-app --restart unless-stopped trading-strategy

echo "✅ Deployment complete!"
echo "Access app at: http://$(curl -s ifconfig.me):8501"
EOF

echo ""
echo "✅ Deployment to AWS EC2 successful!"
echo "===================================="
echo "Access your app at: http://$EC2_IP:8501"
