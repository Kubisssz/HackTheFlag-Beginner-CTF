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

# Create the flag file with restricted permissions
RUN echo "HTF{unl0ck_th3_p3rm15510ns}" > /home/htfuser/flag.txt && \
    chmod 600 /home/htfuser/flag.txt

# Add a clue in the home directory
RUN echo "Sometimes, you need to ask for permission, not forgiveness." > /home/htfuser/README.txt

# Allow htfuser to read the flag using sudo
RUN echo "htfuser ALL=(root) NOPASSWD: /bin/cat /home/htfuser/flag.txt" > /etc/sudoers.d/htfuser

# Create the /run/sshd directory for SSH
RUN mkdir -p /run/sshd

# Expose SSH port
EXPOSE 22

# Start SSH service
CMD ["/usr/sbin/sshd", "-D"]
