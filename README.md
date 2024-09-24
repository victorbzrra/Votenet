# Ambiente de Desenvolvimento para Processamento de Nuvens de Pontos com MMDetection3D

Este projeto documenta o processo de configuração de um ambiente de desenvolvimento para o processamento de nuvens de pontos, utilizando ferramentas como WSL 2.0, Ubuntu, Miniconda, CUDA Toolkit, PyTorch, MMDetection3D, e outras bibliotecas essenciais.

## Índice
1. [Configuração do WSL 2.0 e Ubuntu 22.04.3 LTS](#configuração-do-wsl-20-e-ubuntu-22043-lts)
2. [Instalação e Integração do Visual Studio Code com WSL](#instalação-e-integração-do-visual-studio-code-com-wsl)
3. [Configuração do Ambiente Miniconda](#configuração-do-ambiente-miniconda)
4. [Instalação do CUDA Toolkit e Pacotes Essenciais](#instalação-do-cuda-toolkit-e-pacotes-essenciais)
5. [Instalação e Configuração do MMDetection3D](#instalação-e-configuração-do-mmdetection3d)
6. [Pré-processamento das Nuvens de Pontos](#pré-processamento-das-nuvens-de-pontos)
7. [Detecção e Inferência das Caixas Delimitadoras](#detecção-e-inferência-das-caixas-delimitadoras)
8. [Remoção de Caixas Delimitadoras de Volumes](#remoção-de-caixas-delimitadoras-de-volumes)
9. [Exibição dos Resultados](#exibição-dos-resultados)

## Configuração do WSL 2.0 e Ubuntu 22.04.3 LTS

1. Habilitar o Windows Subsystem for Linux (WSL) executando o comando abaixo no PowerShell:

   ```bash
   wsl --install
   ```

2. Após a reinicialização do sistema, instale o Ubuntu 22.04.3 LTS da Microsoft Store.
3. Configure o Ubuntu criando um usuário e senha conforme solicitado.

## Instalação e Integração do Visual Studio Code com WSL
1. Baixe e instale o Visual Studio Code diretamente do site oficial.
2. Instale a extensão Remote - WSL no Visual Studio Code.
3. Inicie um terminal no ambiente Ubuntu diretamente pelo Visual Studio Code para facilitar a integração.

## Configuração do Ambiente Miniconda
1. Baixe e instale o Miniconda no terminal Ubuntu com os comandos:

    ```bash
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh 
    bash Miniconda3-latest-Linux-x86_64.sh
    ```

2. Crie um ambiente Conda com Python 3.8 e ative-o:

    ```bash
    conda create -n myenv python=3.8
    conda activate myenv
     ```

## Instalação do CUDA Toolkit e Pacotes Essenciais

1. Instale o CUDA Toolkit 11.8 com o comando:
    ```bash
    conda install -c nvidia -c defaults cudatoolkit=11.8
    ```

2. Instale o PyTorch e demais bibliotecas essenciais:
    ```bash
    conda install pytorch=2.0.0 torchvision=0.15.0 torchaudio=2.0.0 pytorch-cuda=11.8 -c pytorch -c nvidia
    ```

3. Instale dependências adicionais no Ubuntu:
    ```bash 
    sudo apt-get install ffmpeg libsm6 libxext6 git ninja-build libglib2.0-0 libsm6 libxrender-dev libxext6
    ```

## Instalação e Configuração do MMDetection3D
1. Clone o repositório MMDetection3D:
    ```bash
    git clone https://github.com/open-mmlab/mmdetection3d.git -b dev-1.x
    cd mmdetection3d
    ```
2. Instale dependências e MMDetection3D:
    ```bash
     pip install mmengine mmcv>=2.0.0rc4 mmdet>=3.0.0
     pip install -e .
    ```

## Referências

- **MMDetection3D**: OpenMMLab. (n.d.). MMDetection3D: Open-source toolbox for 3D object detection. GitHub repository. Disponível em: [https://github.com/open-mmlab/mmdetection3d](https://github.com/open-mmlab/mmdetection3d)
- **CUDA Toolkit**: NVIDIA. (n.d.). CUDA Toolkit Documentation. NVIDIA Developer. Disponível em: [https://developer.nvidia.com/cuda-toolkit](https://developer.nvidia.com/cuda-toolkit)
- **PyTorch**: PyTorch Team. (n.d.). PyTorch: An open-source machine learning framework. Disponível em: [https://pytorch.org/](https://pytorch.org/)
- **Miniconda**: Anaconda Inc. (n.d.). Miniconda - A free minimal installer for conda. Disponível em: [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)
- **Ubuntu**: Canonical Ltd. (n.d.). Ubuntu 22.04 LTS. Disponível em: [https://ubuntu.com/download](https://ubuntu.com/download)
- **WSL 2**: Microsoft. (n.d.). Windows Subsystem for Linux Documentation. Disponível em: [https://learn.microsoft.com/en-us/windows/wsl/](https://learn.microsoft.com/en-us/windows/wsl/)
- **Visual Studio Code**: Microsoft. (n.d.). Visual Studio Code Documentation. Disponível em: [https://code.visualstudio.com/docs](https://code.visualstudio.com/docs)
