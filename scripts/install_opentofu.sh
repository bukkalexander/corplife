#!/bin/bash

set -e

# Update package list and install necessary tools
echo "Updating package lists and installing prerequisites..."
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg

# Set up OpenTofu repository with error handling for gpg steps
echo "Setting up OpenTofu repository..."

# Create the keyrings directory if it doesn’t exist
KEYRING_DIR="/etc/apt/keyrings"
sudo install -m 0755 -d "$KEYRING_DIR"

# Download and install the main gpg key with error handling
if [ ! -f "$KEYRING_DIR/opentofu.gpg" ]; then
    echo "Downloading opentofu.gpg key..."
    if ! curl -fsSL https://get.opentofu.org/opentofu.gpg | sudo tee "$KEYRING_DIR/opentofu.gpg" >/dev/null; then
        echo "Error: Failed to download opentofu.gpg key." >&2
        exit 1
    fi
else
    echo "opentofu.gpg key already exists, skipping download."
fi

# Download and dearmor the repository gpg key with error handling
if [ ! -f "$KEYRING_DIR/opentofu-repo.gpg" ]; then
    echo "Downloading and dearmoring opentofu repository gpg key..."
    if ! curl -fsSL https://packages.opentofu.org/opentofu/tofu/gpgkey | sudo gpg --no-tty --batch --dearmor -o "$KEYRING_DIR/opentofu-repo.gpg" >/dev/null; then
        echo "Error: Failed to download or dearmor opentofu repository gpg key." >&2
        exit 1
    fi
else
    echo "opentofu-repo.gpg key already exists, skipping dearmoring."
fi

# Ensure permissions are correct
sudo chmod a+r "$KEYRING_DIR/opentofu.gpg" "$KEYRING_DIR/opentofu-repo.gpg"

# Add OpenTofu source list, handling any potential errors
echo "Adding OpenTofu to sources list..."
if ! echo \
    "deb [signed-by=$KEYRING_DIR/opentofu.gpg,$KEYRING_DIR/opentofu-repo.gpg] https://packages.opentofu.org/opentofu/tofu/any/ any main
deb-src [signed-by=$KEYRING_DIR/opentofu.gpg,$KEYRING_DIR/opentofu-repo.gpg] https://packages.opentofu.org/opentofu/tofu/any/ any main" | \
    sudo tee /etc/apt/sources.list.d/opentofu.list > /dev/null; then
    echo "Error: Failed to add OpenTofu to sources list." >&2
    exit 1
fi

sudo chmod a+r /etc/apt/sources.list.d/opentofu.list

# Install OpenTofu
echo "Installing OpenTofu..."
sudo apt-get update
if ! sudo apt-get install -y tofu; then
    echo "Error: Failed to install OpenTofu." >&2
    exit 1
fi

echo "OpenTofu installation complete."
 