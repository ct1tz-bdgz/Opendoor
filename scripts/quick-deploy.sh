#!/bin/bash

# Quick deployment script for MCP Server
set -e

echo "🚀 Quick Deploy: Opendoor MCP to GCP"
echo "===================================="

# Make scripts executable
chmod +x scripts/*.sh

# Install and authenticate with GCP
echo "Step 1: Setting up Google Cloud CLI..."
./scripts/install-gcloud.sh

# Deploy everything
echo "Step 2: Deploying to GCP..."
./scripts/deploy.sh

echo ""
echo "🎉 Quick deployment completed!"
echo "Your Opendoor MCP platform with beautiful documentation is now live on GCP!"
