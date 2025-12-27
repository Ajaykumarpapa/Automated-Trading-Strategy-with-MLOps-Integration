# Kubernetes Deployment

This directory contains Kubernetes manifests for deploying the Trading Strategy application.

## Files

- `deployment.yaml` - Main application deployment, service, and HPA
- `ingress.yaml` - Ingress configuration for external access
- `configmap.yaml` - Configuration management (optional)
- `secret.yaml` - Secrets management (optional)

## Prerequisites

- Kubernetes cluster (1.20+)
- kubectl configured
- Ingress controller installed (nginx)
- cert-manager for SSL (optional)

## Quick Deploy

```bash
# Apply all configurations
kubectl apply -f k8s/

# Check status
kubectl get all -l app=trading-strategy

# Get service URL
kubectl get service trading-strategy
```

## Access Application

```bash
# Port forward for local testing
kubectl port-forward service/trading-strategy 8501:80

# Access at http://localhost:8501
```

## Scaling

```bash
# Manual scaling
kubectl scale deployment trading-strategy --replicas=5

# Auto-scaling is configured in deployment.yaml
# HPA will scale between 2-10 replicas based on CPU/memory
```

## Update Image

```bash
# Update image
kubectl set image deployment/trading-strategy trading-strategy=yourusername/trading-strategy:v2

# Rollout status
kubectl rollout status deployment/trading-strategy

# Rollback if needed
kubectl rollout undo deployment/trading-strategy
```

## Monitoring

```bash
# View logs
kubectl logs -l app=trading-strategy -f

# Describe pod
kubectl describe pod <pod-name>

# Get events
kubectl get events --sort-by=.metadata.creationTimestamp
```

## Cleanup

```bash
# Delete all resources
kubectl delete -f k8s/
```
