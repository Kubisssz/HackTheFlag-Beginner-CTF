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

# Create the real flag in the user's home directory
RUN echo "HTF{Fake_flag}" > /home/htfuser/flag.txt && \
    chmod 644 /home/htfuser/flag.txt

# Create fake flags in the user's home directory
RUN echo "HTF{Fake_Flag}" > /home/htfuser/flag1.txt && \
    chmod 644 /home/htfuser/flag1.txt

# Create fake flags in the user's home directory
RUN echo "HTF{Fake_Flag}" > /home/htfuser/flag2.txt && \
    chmod 644 /home/htfuser/flag1.txt

# Create fake flags in the user's home directory
RUN echo "HTF{Fake_Flag}" > /home/htfuser/fl4g1.txt && \
    chmod 644 /home/htfuser/flag1.txt

RUN echo "HTF{HTF{l1nux_ski115_4re_fun}" > /home/htfuser/flag3.txt && \
    chmod 644 /home/htfuser/flag3.txt


# Create the /run/sshd directory for SSH
RUN mkdir -p /run/sshd

# Expose SSH port
EXPOSE 22

# Start SSH service
CMD ["/usr/sbin/sshd", "-D"]
