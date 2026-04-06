# Add professional README
cat > README.md << 'EOF'
# 💱 Currency Converter - Docker + Kubernetes

**Production-ready currency converter** with **responsive UI** deployed on **Kubernetes NodePort 30000**.

## 🎬 Live Demo



## 🚀 Quick Deploy
```bash
# Docker
docker build -t currency-converter .
docker run -p 3000:5000 currency-converter

# Kubernetes  
kubectl apply -f deployment.yaml -f service.yaml

