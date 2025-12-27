# Deployment Guide

This guide provides step-by-step instructions for deploying the Automated Trading Strategy application to various platforms.

## Table of Contents

1. [Quick Deploy Options](#quick-deploy-options)
2. [Docker Deployment](#docker-deployment)
3. [Cloud Platforms](#cloud-platforms)
   - [Streamlit Cloud (Easiest)](#streamlit-cloud)
   - [Heroku](#heroku)
   - [AWS EC2](#aws-ec2)
   - [Google Cloud Platform](#google-cloud-platform)
   - [Azure](#azure)
   - [DigitalOcean](#digitalocean)
4. [Kubernetes Deployment](#kubernetes-deployment)
5. [Environment Variables](#environment-variables)
6. [Production Checklist](#production-checklist)

---

## Quick Deploy Options

### Option 1: Streamlit Cloud (Recommended for Beginners)

**Pros:** Free, easiest, automatic HTTPS, no DevOps knowledge needed
**Cons:** Public by default, limited resources

**Steps:**
1. Push your code to GitHub (already done!)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click "New app"
5. Select your repository: `Automated-Trading-Strategy-with-MLOps-Integration`
6. Main file path: `tradingstrategy.py`
7. Click "Deploy"

**Done!** Your app will be live in 2-3 minutes at `https://[your-app].streamlit.app`

### Option 2: Docker + Cloud (Production Ready)

Deploy the Docker container to any cloud platform. See detailed instructions below.

---

## Docker Deployment

### Local Docker Testing

Before deploying, test locally:

```bash
# Build the image
docker build -t trading-strategy .

# Run the container
docker run -p 8501:8501 trading-strategy

# Or use Docker Compose
docker-compose up
```

Access at `http://localhost:8501`

### Docker Hub Registry

Push to Docker Hub for easy deployment:

```bash
# Login to Docker Hub
docker login

# Tag your image
docker tag trading-strategy yourusername/trading-strategy:latest

# Push to Docker Hub
docker push yourusername/trading-strategy:latest
```

Now you can deploy from any cloud platform using:
```bash
docker pull yourusername/trading-strategy:latest
docker run -p 8501:8501 yourusername/trading-strategy:latest
```

---

## Cloud Platforms

### Streamlit Cloud

**Best for:** Quick deployments, demos, MVPs

#### Prerequisites
- GitHub account
- Code pushed to GitHub repository

#### Steps

1. **Prepare `requirements.txt`** ✓ (Already done!)

2. **Go to Streamlit Cloud:**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub

3. **Deploy:**
   - Click "New app"
   - Repository: `Ajaykumarpapa/Automated-Trading-Strategy-with-MLOps-Integration`
   - Branch: `claude/project-setup-PuHWq` or `main`
   - Main file: `tradingstrategy.py`
   - App URL: Choose your custom URL

4. **Advanced Settings (Optional):**
   - Python version: 3.11
   - Secrets: Add API keys if needed

5. **Click "Deploy"**

**Cost:** Free tier includes:
- 1 GB RAM
- 1 CPU core
- Unlimited viewers

---

### Heroku

**Best for:** Small to medium apps, easy scaling

#### Prerequisites
- Heroku account (free tier available)
- Heroku CLI installed

#### Setup Files

1. **Create `Procfile`** (already in this guide)
2. **Create `setup.sh`** (already in this guide)

#### Deployment Steps

```bash
# Install Heroku CLI
curl https://cli-assets.heroku.com/install.sh | sh

# Login to Heroku
heroku login

# Create a new app
heroku create your-trading-strategy-app

# Set buildpack
heroku buildpacks:set heroku/python

# Deploy
git push heroku claude/project-setup-PuHWq:main

# Open your app
heroku open

# View logs
heroku logs --tail
```

#### Scaling

```bash
# Scale to 1 dyno (free tier)
heroku ps:scale web=1

# Upgrade to hobby dyno ($7/month)
heroku dyno:type hobby
```

**Cost:**
- Free tier: 550-1000 dyno hours/month
- Hobby: $7/month
- Standard: $25-50/month

---

### AWS EC2

**Best for:** Full control, custom configurations, enterprise

#### Steps

1. **Launch EC2 Instance:**
   - AMI: Ubuntu 22.04 LTS
   - Instance type: t2.micro (free tier) or t2.small
   - Security group: Open port 8501

2. **Connect to instance:**
```bash
ssh -i your-key.pem ubuntu@your-instance-ip
```

3. **Install dependencies:**
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu

# Logout and login again for Docker permissions
exit
ssh -i your-key.pem ubuntu@your-instance-ip
```

4. **Deploy application:**
```bash
# Clone repository
git clone https://github.com/Ajaykumarpapa/Automated-Trading-Strategy-with-MLOps-Integration.git
cd Automated-Trading-Strategy-with-MLOps-Integration

# Build and run with Docker
docker build -t trading-strategy .
docker run -d -p 8501:8501 --name trading-app trading-strategy

# Or run without Docker
pip3 install -r requirements.txt
streamlit run tradingstrategy.py --server.port=8501 --server.address=0.0.0.0
```

5. **Setup as systemd service** (recommended for production):
```bash
sudo nano /etc/systemd/system/trading-strategy.service
```

Add this content:
```ini
[Unit]
Description=Trading Strategy Streamlit App
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/Automated-Trading-Strategy-with-MLOps-Integration
ExecStart=/usr/local/bin/streamlit run tradingstrategy.py --server.port=8501 --server.address=0.0.0.0
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable trading-strategy
sudo systemctl start trading-strategy
sudo systemctl status trading-strategy
```

6. **Setup domain and SSL (Optional):**
```bash
# Install Nginx
sudo apt install nginx -y

# Install Certbot for SSL
sudo apt install certbot python3-certbot-nginx -y

# Configure Nginx reverse proxy
sudo nano /etc/nginx/sites-available/trading-strategy
```

Add:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Enable and get SSL:
```bash
sudo ln -s /etc/nginx/sites-available/trading-strategy /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
sudo certbot --nginx -d your-domain.com
```

**Cost:**
- t2.micro: Free tier (1 year)
- t2.small: ~$17/month
- t2.medium: ~$34/month

---

### Google Cloud Platform

**Best for:** Enterprise apps, integration with Google services

#### Using Cloud Run (Serverless)

```bash
# Install Google Cloud SDK
curl https://sdk.cloud.google.com | bash
exec -l $SHELL

# Initialize gcloud
gcloud init

# Set project
gcloud config set project YOUR_PROJECT_ID

# Build and push to Container Registry
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/trading-strategy

# Deploy to Cloud Run
gcloud run deploy trading-strategy \
  --image gcr.io/YOUR_PROJECT_ID/trading-strategy \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --port 8501
```

#### Using Compute Engine (VM)

Similar to AWS EC2:
```bash
# Create VM
gcloud compute instances create trading-strategy-vm \
  --zone=us-central1-a \
  --machine-type=e2-small \
  --image-family=ubuntu-2204-lts \
  --image-project=ubuntu-os-cloud

# SSH into VM
gcloud compute ssh trading-strategy-vm

# Follow same Docker deployment steps as AWS
```

**Cost:**
- Cloud Run: Pay per use, ~$0.24/million requests
- e2-micro: Free tier
- e2-small: ~$13/month

---

### Azure

**Best for:** Microsoft ecosystem integration

#### Using Azure Container Instances

```bash
# Install Azure CLI
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Login
az login

# Create resource group
az group create --name trading-strategy-rg --location eastus

# Create container registry
az acr create --resource-group trading-strategy-rg --name tradingstrategyacr --sku Basic

# Login to registry
az acr login --name tradingstrategyacr

# Build and push
docker tag trading-strategy tradingstrategyacr.azurecr.io/trading-strategy:latest
docker push tradingstrategyacr.azurecr.io/trading-strategy:latest

# Deploy container
az container create \
  --resource-group trading-strategy-rg \
  --name trading-strategy-app \
  --image tradingstrategyacr.azurecr.io/trading-strategy:latest \
  --dns-name-label trading-strategy-unique \
  --ports 8501
```

**Cost:**
- Container Instances: ~$0.0000125/second (~$30/month)
- Free tier: $200 credit first 30 days

---

### DigitalOcean

**Best for:** Developer-friendly, simple pricing

#### Using App Platform

1. **Create account at DigitalOcean**

2. **Deploy via UI:**
   - Click "Create" → "Apps"
   - Connect GitHub repository
   - Select branch
   - Detect Dockerfile automatically
   - Choose plan ($5-12/month)
   - Click "Deploy"

#### Using Droplets (VPS)

```bash
# Create droplet via UI or CLI
doctl compute droplet create trading-strategy \
  --size s-1vcpu-1gb \
  --image ubuntu-22-04-x64 \
  --region nyc3

# SSH into droplet
ssh root@your-droplet-ip

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# Deploy
git clone https://github.com/Ajaykumarpapa/Automated-Trading-Strategy-with-MLOps-Integration.git
cd Automated-Trading-Strategy-with-MLOps-Integration
docker-compose up -d
```

**Cost:**
- Basic Droplet: $6/month
- App Platform: $5-12/month

---

## Kubernetes Deployment

For large-scale production deployments.

### Prerequisites
- Kubernetes cluster (GKE, EKS, AKS, or local minikube)
- kubectl configured

### Deployment Files

See `k8s/` directory for full Kubernetes manifests (created below).

```bash
# Apply configurations
kubectl apply -f k8s/

# Check deployment
kubectl get pods
kubectl get services

# Access application
kubectl port-forward service/trading-strategy 8501:8501
```

---

## Environment Variables

Create `.env` file for sensitive data:

```env
# Application Settings
APP_ENV=production
DEBUG=False

# API Keys (if needed in future)
# ALPHA_VANTAGE_API_KEY=your_key_here
# TWELVEDATA_API_KEY=your_key_here

# Database (for future features)
# DATABASE_URL=postgresql://user:pass@host:5432/dbname

# MLOps
# MLFLOW_TRACKING_URI=https://your-mlflow-server.com
# MLFLOW_TRACKING_USERNAME=admin
# MLFLOW_TRACKING_PASSWORD=password

# Monitoring
# PROMETHEUS_ENDPOINT=http://prometheus:9090
```

**Important:** Never commit `.env` to git! (Already in .gitignore)

---

## Production Checklist

Before deploying to production:

### Security
- [ ] Remove debug mode
- [ ] Use environment variables for secrets
- [ ] Enable HTTPS/SSL
- [ ] Setup firewall rules
- [ ] Implement rate limiting
- [ ] Add authentication (if needed)

### Performance
- [ ] Enable caching in Streamlit
- [ ] Optimize Docker image size
- [ ] Setup CDN for static assets
- [ ] Configure auto-scaling
- [ ] Monitor resource usage

### Monitoring
- [ ] Setup error tracking (Sentry)
- [ ] Configure application logs
- [ ] Setup uptime monitoring
- [ ] Create alerts for failures
- [ ] Monitor API rate limits

### Backup & Recovery
- [ ] Regular database backups
- [ ] Document recovery procedures
- [ ] Test disaster recovery
- [ ] Keep code in version control

### Documentation
- [ ] Document deployment process
- [ ] Create runbooks for common issues
- [ ] Document environment variables
- [ ] Keep architecture diagrams updated

---

## Recommended Deployment Strategy

**For Learning/Demo:**
→ Streamlit Cloud (Free, 5 minutes)

**For Small Projects:**
→ Heroku or DigitalOcean App Platform ($5-7/month)

**For Production:**
→ AWS EC2 + Docker or GCP Cloud Run ($15-50/month)

**For Enterprise:**
→ Kubernetes on AWS EKS/GCP GKE ($100+/month)

---

## Troubleshooting

### Common Issues

**Port already in use:**
```bash
# Find process using port 8501
lsof -i :8501
# Kill the process
kill -9 <PID>
```

**Docker container crashes:**
```bash
# Check logs
docker logs <container-id>

# Run interactively for debugging
docker run -it trading-strategy /bin/bash
```

**Out of memory:**
- Upgrade instance size
- Optimize Streamlit caching
- Reduce data processing load

**Dependencies fail to install:**
- Check Python version (3.11 required)
- Clear pip cache: `pip cache purge`
- Use virtual environment

---

## Next Steps

After deployment:

1. **Setup Monitoring:** Integrate with monitoring tools
2. **Configure CI/CD:** Automate deployments from GitHub
3. **Add Analytics:** Track user behavior
4. **Implement Feedback:** Add user feedback mechanism
5. **Scale:** Setup auto-scaling based on traffic

---

## Support

For deployment issues:
- Check application logs
- Review this guide
- Check cloud provider documentation
- Open GitHub issue

Happy Deploying! 🚀
