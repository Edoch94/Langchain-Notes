FROM python:3.11
LABEL Name=langchainnotes

ARG DEBIAN_FRONTEND=noninteractive
ARG USERNAME=nonroot
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN apt update && \
    apt install -y sudo && \
    addgroup --gid $USER_GID $USERNAME && \
    adduser --uid $USER_UID --gid $USER_GID --disabled-password --gecos "" $USERNAME && \
    echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME &&\
    chmod 0440 /etc/sudoers.d/$USERNAME

# [Optional] Set the default user. Omit if you want to keep the default as root.
# USER $USERNAME