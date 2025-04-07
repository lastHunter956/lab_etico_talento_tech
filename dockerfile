# Base image
FROM kalilinux/kali-rolling

# Install basic command-line tools and Metasploit
RUN apt-get update && \
    apt-get install -y nmap metasploit-framework \
    john hydra nikto \
    sqlmap && \
    apt-get clean

# Set working directory
WORKDIR /workspace

# Copy application code
COPY . /workspace

# Default command
CMD ["/bin/bash"]
