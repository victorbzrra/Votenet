# Step 0
Install conda or miniconda.
https://docs.anaconda.com/miniconda/

Install Cuda 11.8 
https://developer.nvidia.com/cuda-11-8-0-download-archive

# Step 1
conda create --name openmmlab python=3.8
conda activate openmmlab

# Step 2
conda install pytorch==2.0.0 torchvision==0.15.0 torchaudio==2.0.0 pytorch-cuda=11.8 -c pytorch -c nvidia

# Step 3
pip install openmim
mim install "mmengine" "mmcv>=2.0.0rc4" "mmdet>=3.0.0"

# Step 4 
git clone https://github.com/open-mmlab/mmdetection3d.git -b dev-1.x
cd mmdetection3d
pip install -v -e .