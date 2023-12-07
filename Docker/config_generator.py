import tkinter as tk

from os.path import dirname, abspath
from pprint import pprint
from tkinter import (Label,
                     OptionMenu,
                     StringVar,
                     Button)
from tkinter.ttk import (Separator)

base_run_string = \
"""\
    docker run \\
    --tty \\
    --detach \\
    --privileged \\
    --name ${CONTAINER_NAME} \\
    --volume /tmp/.X11-unix:/tmp/.X11-unix \\
    --env DISPLAY=$DISPLAY \\
"""

else_content_default = \
"""\
    # container already exists...
    # allow UI spawning through X server
    xhost +local:`docker inspect --format='{{ .Config.Hostname }}' ${CONTAINER_ID}`

    # if container exists but is not running, start it
    if [ -z `docker ps -qf "name=^/${CONTAINER_NAME}$"` ]; then
        docker start ${CONTAINER_ID}
    fi

    # enter container
    docker exec -it ${CONTAINER_ID} bash

    # disallow UI spawning through X server
    xhost -local:`docker inspect --format='{{ .Config.Hostname }}' ${CONTAINER_ID}`
"""

else_content_headless = \
"""\
    if [ -z `docker ps -qf "name=^/${CONTAINER_NAME}$"` ]; then
        docker restart ${CONTAINER_ID}
    fi

    echo "Connect to http://localhost:6080/ on your browser to access the container."
"""

# Create the main window
root = tk.Tk()
root.title("Config Generator")

# Row 1: Label (Host OS) and dropdown
os_label = Label(root, text="Host OS")
os_label.grid(row=0, column=0, padx=5, sticky='e')
os_options = ["Ubuntu 22.04", "WSL2 on Windows 11", "MacOS"]
os_selection = tk.StringVar()
os_selection.set(os_options[0])
os_dropdown = OptionMenu(root, os_selection, *os_options)
os_dropdown.config(width=20)
os_dropdown.grid(row=0, column=1, padx=5)

# Row 2: Label (GPU) and dropdown
gpu_label = Label(root, text="GPU")
gpu_label.grid(row=1, column=0, padx=5, sticky='e')
# gpu_options = ["NVIDIA", "AMD", "Intel Iris/HD Graphics"]
gpu_options = ["NVIDIA", "Intel Iris/HD Graphics"]
gpu_selection = tk.StringVar()
gpu_selection.set(gpu_options[0])
gpu_dropdown = OptionMenu(root, gpu_selection, *gpu_options)
gpu_dropdown.config(width=20)
gpu_dropdown.grid(row=1, column=1, padx=5)

# Horizontal separator
separator = Separator(root, orient='horizontal')
separator.grid(row=2, column=0, columnspan=2, sticky='ew', padx=5, pady=5)

# 'Generate' button
# Function to handle button click event
def on_generate_click(os, gpu):
    file_content = None
    destination = dirname(abspath(__file__)) + '/run_container.sh'
    source = dirname(abspath(__file__)) + '/Dockerfiles/script_template.sh'
    with open(source, 'r') as source_content:
        file_content = source_content.readlines()
        # pprint([(idx, line) for (idx, line) in (enumerate(file_content))])

    # replaces the run settings per OS and GPU selection
    file_content[9] = base_run_string

    if os == 'Ubuntu 22.04':
        file_content[6] = ''
        if gpu == 'NVIDIA':
            file_content[9] += '    --gpus all \\\n'
            file_content[9] += '    --runtime nvidia \\\n'
            file_content[9] += '    ${IMAGE_NAME}:ubuntu_nvidia\n'
        elif gpu == 'AMD':
            raise NotImplementedError("Ubuntu 22.04 with AMD GPU is not supported yet. Requires ROCm-docker. See https://github.com/RadeonOpenCompute/ROCm-docker/blob/master/quick-start.md")
            # file_content[9] += '    --cap-add SYS_PTRACE \\\n'
            # file_content[9] += '    --ipc host \\\n'
            # file_content[9] += '    --security-opt seccomp=unconfined \\\n'
            # file_content[9] += '    --device=/dev/dri \\\n'
            # file_content[9] += '    --device=/dev/kfd \\\n'
            # file_content[9] += '    --group-add video \\\n'
            # file_content[9] += '    ${IMAGE_NAME}:ubuntu_amd\n'
        elif gpu == 'Intel Iris/HD Graphics':
            file_content[9] += '    --gpus all \\\n'
            file_content[9] += '    --device=/dev/dri \\\n'
            file_content[9] += '    ${IMAGE_NAME}:ubuntu_intel\n'
    elif os == 'WSL2 on Windows 11':
        if gpu == 'NVIDIA':
            file_content[6] = 'export MESA_D3D12_DEFAULT_ADAPTER_NAME=NVIDIA\n'
            file_content[9] += '    --device /dev/dxg \\\n'
            file_content[9] += '    --device /dev/dri/card0 \\\n'
            file_content[9] += '    --device /dev/dri/renderD128 \\\n'
            file_content[9] += '    --volume /mnt/wslg:/mnt/wslg \\\n'
            file_content[9] += '    --volume /usr/lib/wsl:/usr/lib/wsl \\\n'
            file_content[9] += '    --env WAYLAND_DISPLAY=$WAYLAND_DISPLAY \\\n'
            file_content[9] += '    --env XDG_RUNTIME_DIR=$XDG_RUNTIME_DIR \\\n'
            file_content[9] += '    --env PULSE_SERVER=$PULSE_SERVER \\\n'
            file_content[9] += '    ${IMAGE_NAME}:wsl2_nvidia\n'
        elif gpu == 'AMD':
            raise NotImplementedError("WSL2 on Windows 11 with AMD GPU is not supported yet.")
        elif gpu == 'Intel Iris/HD Graphics':
            file_content[6] = 'export MESA_D3D12_DEFAULT_ADAPTER_NAME=Intel\n'
            file_content[9] += '    --device /dev/dxg \\\n'
            file_content[9] += '    --device /dev/dri/card0 \\\n'
            file_content[9] += '    --device /dev/dri/renderD128 \\\n'
            file_content[9] += '    --volume /mnt/wslg:/mnt/wslg \\\n'
            file_content[9] += '    --volume /usr/lib/wsl:/usr/lib/wsl \\\n'
            file_content[9] += '    --env WAYLAND_DISPLAY=$WAYLAND_DISPLAY \\\n'
            file_content[9] += '    --env XDG_RUNTIME_DIR=$XDG_RUNTIME_DIR \\\n'
            file_content[9] += '    --env PULSE_SERVER=$PULSE_SERVER \\\n'
            file_content[9] += '    ${IMAGE_NAME}:wsl2_intel\n'
    elif os == 'MacOS':
        file_content[6] = ''
        file_content[9] += '    --publish 6080:80 \\\n'
        file_content[9] += '    ${IMAGE_NAME}:macos\n'
        # if gpu == 'NVIDIA':
        #     raise NotImplementedError("This setup doesn't exist anymore. :)")
        # elif gpu == 'AMD':
        #     raise NotImplementedError("MacOS with AMD GPU is not supported yet.")
        # elif gpu == 'Intel Iris/HD Graphics':
        #     pass

    # replaces the container startup/restart and attach commands
    if os == 'Ubuntu 22.04' or os == 'WSL2 on Windows 11':
        file_content[11] = else_content_default
    else:
        file_content[11] = else_content_headless

    # write run script
    with open(destination, 'w') as dest:
        dest.writelines(file_content)

    result_label.config(text=f"Generated config for {os} with {gpu} GPU")

generate_button = Button(root, text="Generate", command=lambda: on_generate_click(os_selection.get(), gpu_selection.get()))
generate_button.grid(row=3, column=0, columnspan=2, pady=2)

# Modifiable result label
result_label = Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, sticky='w', padx=2, pady=2)

# Prevent resizing
root.resizable(False, False)

# Start the GUI event loop
root.mainloop()
