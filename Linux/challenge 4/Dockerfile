# Use a base image (e.g., Ubuntu)
FROM ubuntu:22.04

# Install necessary packages
RUN apt update && apt install -y \
    openssh-server \
    sudo \
    vim \
    findutils \
    coreutils && \  
    rm -rf /var/lib/apt/lists/*

# Create a user for the challenge
RUN useradd -m -s /bin/bash htfuser && \
    echo "htfuser:htfpassword" | chpasswd && \
    usermod -aG sudo htfuser

# Create a hidden directory for the encrypted flag
RUN mkdir -p /var/challenge && \
    echo "SFRGezNuY3J5cHQzZF9mbDRnXzFzXzFudDNyM3N0M2R9" > /var/challenge/encrypted_flag.txt && \
    chmod 600 /var/challenge/encrypted_flag.txt

# Add a clue in the home directory
RUN echo "This challenge same with the previous challenge but it's encrypted." > /home/htfuser/README.txt

# Create the /run/sshd directory for SSH
RUN mkdir -p /run/sshd

# Expose SSH port
EXPOSE 22

# Start SSH service
CMD ["/usr/sbin/sshd", "-D"]
