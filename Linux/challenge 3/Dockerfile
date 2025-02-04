# Use a base image (e.g., Ubuntu)
FROM ubuntu:22.04

# Install necessary packages
RUN apt update && apt install -y \
    openssh-server \
    sudo \
    vim \
    findutils \
    && rm -rf /var/lib/apt/lists/*

# Create a user for the challenge
RUN useradd -m -s /bin/bash htfuser && \
    echo "htfuser:htfpassword" | chpasswd && \
    usermod -aG sudo htfuser

# Create a hidden file with the flag
RUN mkdir -p /var/secrets && \
    echo "HTF{h1dd3n_m3554g3}" > /var/secrets/.hidden_message && \
    chmod 600 /var/secrets/.hidden_message

# Add a clue in the home directory
RUN echo "A secret message is hidden somewhere on the system. find the hidden_message text" > /home/htfuser/README.txt

# Create the /run/sshd directory for SSH
RUN mkdir -p /run/sshd

# Expose SSH port
EXPOSE 22

# Start SSH service
CMD ["/usr/sbin/sshd", "-D"]
