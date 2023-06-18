# 1. install a version of docker with gpu support (docker-ce >= 19.03)

# 2.  enter the project directory and build the wav2lip image:
# docker build -t wav2lip .

# 3. allow root user to connect to the display
# xhost +local:root

# 4. instantiate the container
# docker run --rm --gpus all -v /tmp/.X11-unix:/tmp/.X11-unix -v $PWD:/workspace/src -e DISPLAY=$DISPLAY --device /dev/dri -ti wav2lip bash

# NOTES:
# export CUDA_VISIBLE_DEVICES="" ## force cpu only

# Based on https://github.com/1adrianb/face-alignment/blob/master/Dockerfile

FROM nvidia/cuda:11.7.0-devel-ubuntu22.04

RUN export DEBIAN_FRONTEND=noninteractive RUNLEVEL=1 ; \
     apt-get update && apt-get install -y --no-install-recommends \
          build-essential cmake git curl ca-certificates \
          vim \
          python3-pip python3-dev python3-wheel \
          libglib2.0-0 libxrender1 python3-soundfile \
          ffmpeg && \
	rm -rf /var/lib/apt/lists/* && \
     pip3 install --upgrade setuptools

RUN sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

RUN sudo apt-get install ffmpeg -y

RUN curl https://pyenv.run | bash

RUN echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc && \
     echo 'eval "$(pyenv init -)"' >> ~/.bashrc && \
     echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

RUN exec $SHELL

RUN pyenv --version

RUN pyenv install 3.6

RUN pyenv install 3.9

# # Install Wav2Lip package
# # NOTE we use the git clone to install the requirements only once
# # (if we use COPY it will invalidate the cache and  reinstall the dependencies for every change in the sources)
WORKDIR /workspace
RUN chmod -R a+w /workspace
RUN git clone https://github.com/iamGeoWat/BerkeleyAIHackathon.git

RUN pyenv local 3.9
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

RUN git clone https://github.com/iamGeoWat/Wav2Lip
WORKDIR /workspace/Wav2Lip
RUN pyenv local 3.6
RUN pip3 install -r requirements.txt
RUN pip install opencv-contrib-python==4.2.0.34

RUN mkdir -p /root/.cache/torch/checkpoints && \
     curl -SL -o /root/.cache/torch/checkpoints/s3fd.pth "https://www.adrianbulat.com/downloads/python-fan/s3fd.pth"

# !!! NOTE !!! nvidia-driver version must match the version installed on the host(/docker server)
RUN export DEBIAN_FRONTEND=noninteractive RUNLEVEL=1 ; \
	apt-get update && apt-get install -y --no-install-recommends \
          nvidia-driver-450 mesa-utils && \
	rm -rf /var/lib/apt/lists/*


WORKDIR /workspace/BerkeleyAIHackathon
RUN python3 main.py

RUN mv ./test_long_output.mp4 ../Wav2Lip/filelists/test_long_output.mp4
RUN mv ./test_long_english.wav ../Wav2Lip/filelists/test_long_english.wav

WORKDIR /workspace/Wav2Lip
RUN python3 inference.py --checkpoint_path ./models/wav2lip.pth --face ./filelists/test_long_output.mp4 --audio ./filelists/test_long_english.wav

RUN sudo docker cp $(sudo docker ps -lq):/workspace/Wav2Lip/results/result_voice.mp4 ~/

