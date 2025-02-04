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


RUN echo "HTF{Fake_Flag}" > /home/htfuser/flag10.txt && \
    chmod 644 /home/htfuser/flag10.txt

RUN echo "HTF{Fake_Flag}" > /home/htfuser/flag.txt && \
    chmod 644 /home/htfuser/flag.txt

RUN echo "HTF{Fake_Flag}" > /home/htfuser/real_flag.txt && \
    chmod 644 /home/htfuser/real_flag.txt

# Create the first part of the flag
RUN echo "HTF{ult1m4t3_l1nux_" > /home/htfuser/flag_part1.txt && \
    chmod 644 /home/htfuser/flag_part1.txt

# Create the /var/challenge directory
RUN mkdir -p /var/challenge

# Create the second part of the flag (encrypted)
RUN echo "Y2g0bGwzbmczfQ==" > /var/challenge/flag_part2.txt && \
    chmod 600 /var/challenge/flag_part2.txt

# Add a clue in the home directory
RUN echo "2 Flag?.Seek the hidden, decode the secret, and unite the pieces to claim your prize." > /home/htfuser/README.txt

# Create the /run/sshd directory for SSH
RUN mkdir -p /run/sshd

# Expose SSH port
EXPOSE 22

# Start SSH service
CMD ["/usr/sbin/sshd", "-D"]
