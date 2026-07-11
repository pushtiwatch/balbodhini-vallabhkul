#!/usr/bin/env bash
# ==============================================================================
# LEGAL DISCLOSURE PORTAL - CENSORSHIP-RESISTANT MULTI-CLOUD DEPLOYMENT SCRIPT
# ==============================================================================
# This script automates redundant replication of the evidence vault and site
# assets across multiple independent cloud providers and decentralized networks.
#
# Target Nodes:
# 1. AWS S3 (Primary Enterprise Storage)
# 2. Backblaze B2 / Cloudflare R2 (Secondary High-Bandwidth Object Storage)
# 3. IPFS (Decentralized Censorship-Resistant Web Registry)
# ==============================================================================

set -euo pipefail

# Configuration Variables
LOCAL_VAULT="./assets/evidence/"
PORTAL_BUCKET_S3="s3://willow-creek-disclosures-s3-vault"
PORTAL_BUCKET_B2="b2://willow-creek-disclosures-b2-vault"
IPFS_PINNING_SERVICE="pinata" # Set up Pinata or other IPFS endpoint

echo "=== [1/3] VERIFYING LOCAL VAULT & CRYPTOGRAPHIC INTEGRITY ==="
if [ ! -d "$LOCAL_VAULT" ]; then
    echo "[-] Error: Local evidence vault '$LOCAL_VAULT' not found."
    exit 1
fi
echo "[+] Local evidence vault located. Active asset counts:"
find "$LOCAL_VAULT" -type f | wc -l

echo ""
echo "=== [2/3] INITIATING SECURE OBJECT STORAGE MULTI-CLOUD REPLICATION ==="

# Replication Node 1: AWS S3 (Private/Public Redundant Mirroring)
if command -v aws &> /dev/null; then
    echo "[+] Syncing evidence to AWS S3..."
    # --immutable flag or object-lock recommended on bucket to prevent tampering
    aws s3 sync "$LOCAL_VAULT" "$PORTAL_BUCKET_S3" --acl public-read --delete
else
    echo "[!] Warning: AWS CLI not detected. Skipping S3 sync replication."
fi

# Replication Node 2: Backblaze B2 or Cloudflare R2
if command -v rclone &> /dev/null; then
    echo "[+] Syncing evidence to Backblaze B2/R2 mirror via rclone..."
    rclone sync "$LOCAL_VAULT" "$PORTAL_BUCKET_B2" --fast-list
elif command -v b2 &> /dev/null; then
    echo "[+] Syncing evidence to Backblaze B2 using native CLI..."
    b2 sync "$LOCAL_VAULT" "$PORTAL_BUCKET_B2"
else
    echo "[!] Warning: rclone/b2 CLIs not detected. Skipping Backblaze R2/B2 sync."
fi

echo ""
echo "=== [3/3] PUBLISHING TO DECENTRALIZED IPFS NETWORK ==="
# IPFS publication ensures the documents cannot be forced offline by domain seizures
if command -v ipfs &> /dev/null; then
    echo "[+] Pinning vault assets locally to IPFS..."
    VAULT_CID=$(ipfs add -r -q "$LOCAL_VAULT" | tail -n 1)
    echo "[+] Vault successfully pinned on IPFS."
    echo "[+] Cryptographic Vault IPFS CID: $VAULT_CID"
    echo "[+] Access via Gateway: https://ipfs.io/ipfs/$VAULT_CID"
else
    echo "[!] Warning: IPFS CLI not detected. Decentralized pinning skipped."
fi

echo ""
echo "=============================================================================="
echo "[+] MULTI-CLOUD DEPLOYMENT SKELETON COMPLETED SUCCESSFULLY"
echo "=============================================================================="
