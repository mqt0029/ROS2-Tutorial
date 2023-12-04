# Automated Run Script Generation

> :warning: You **DO NOT** need to build images manually, images are already pre-built and
> available on Docker Hub. Only rebuild when it is absolutely necessary.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Post-Installation Steps](https://docs.docker.com/engine/install/linux-postinstall/) if you
  are on Linux
- Python 3
- Python 3 `tkinter` module

```console
user@host:~$ python3 -m pip install tkinter
```

## Usage

```console
user@host:~$ python3 config_generator.py
```

This will show you a UI window to select your Host OS and GPU vendor. After selecting, click
"Generate" to generate the appropriate run script for your system.

<!-- Image placeholder -->
<!-- ![]() -->
