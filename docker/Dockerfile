########## Pull ##########
FROM ubuntu:20.04
########## Non-interactive ##########
ENV DEBIAN_FRONTEND=noninteractive
########## Common tools ##########
RUN apt-get update && \
    apt-get install -y \
	    vim \
    	wget \
    	unzip \
    	git \
		python3-tk
########## Cache busting ##########
ARG CACHEBUST=1
########## plot_pc_data ##########
RUN apt-get update && \
    apt-get install -y \
		libgl1-mesa-dev \
	    python3-pip && \
	pip3 install \
		open3d \
		matplotlib && \
	cd ~/ && \
	git clone https://github.com/ozakiryota/plot_pc_data.git
########## Initial position ##########
WORKDIR /root/plot_pc_data