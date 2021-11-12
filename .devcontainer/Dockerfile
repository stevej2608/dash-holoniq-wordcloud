FROM python:3.8-buster

RUN useradd -ms /bin/bash vscode

# Install nodejs 12
# https://computingforgeeks.com/how-to-install-nodejs-on-ubuntu-debian-linux-mint/

RUN apt update && \
    apt -y install curl dirmngr apt-transport-https lsb-release ca-certificates && \
    curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
    apt -y install nodejs

USER vscode

ENV PATH="/home/vscode/.local/bin:${PATH}"
