# 部署

## Docker

```bash
docker build -t memcore:latest .
docker run -p 8080:8080 -v memcore-data:/data memcore:latest
```

## Kubernetes

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/
```

## Helm

```bash
helm install memcore ./helm
```
