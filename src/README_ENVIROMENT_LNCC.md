# Passo a Passo: Configuração do Ambiente para TensorFlow no Santos Dumont

Este guia explica como configurar um ambiente para rodar modelos de aprendizado de máquina com TensorFlow utilizando as GPUs disponíveis no supercomputador Santos Dumont. Vamos configurar o ambiente utilizando Anaconda, CUDA e cuDNN, garantindo compatibilidade e estabilidade com a versão mais recente do TensorFlow.

## 1. Carregar o Ambiente Anaconda

Para começar, carregue a versão mais recente do Anaconda disponível no sistema. Anaconda é uma plataforma que facilita o gerenciamento de ambientes Python e a instalação de pacotes necessários para o desenvolvimento de projetos de aprendizado de máquina.

 **Comando:**

```bash
module load anaconda3/2024.02
```

* Para identificar se o carregamento foi executado com sucesso, aplique o seguinte comando:

```bash
module list
```

* Resultado esperado do comando ```module list```:

```bash
Currently Loaded Modulefiles:
  1) anaconda3/2024.02
```

* Para verificar qual versão do conda foi instalada:

```bash
conda --version
```

* Resultado esperado do comando ```conda --version```:

```bash
conda 24.1.2
```

## 2. Carregar CUDA e cuDNN

Para aproveitar a aceleração por GPU no TensorFlow, é necessário ter as bibliotecas CUDA (Compute Unified Device Architecture) e cuDNN (CUDA Deep Neural Network library). Essas bibliotecas permitem que o TensorFlow utilize o poder de processamento paralelo das GPUs.

Vamos utilizar as versões mais recentes disponíveis, que são compatíveis com o TensorFlow 2.13:

* **CUDA:** `cuda/11.8`
* **cuDNN:** `cudnn/8.2_cuda-11.4`

Comandos para carregar os módulos CUDA e cuDNN:

```bash
module load cuda/11.8
module load cudnn/8.2_cuda-11.4
```

* Resultado esperado do comando ```module list```:

```bash
Currently Loaded Modulefiles:
  1) anaconda3/2024.02     3) cuda/11.2
  2) cuda/11.8             4) cudnn/8.2_cuda-11.4
```

## 3. Configurar o Ambiente Virtual com TensorFlow

É recomendável criar um ambiente virtual para isolar as dependências do seu projeto e evitar conflitos entre pacotes. Crie um ambiente virtual com Python 3.9, que seja compatível com a versão mais recente do TensorFlow.

Passos:

1. Criar um Ambiente Virtual com Anaconda:

Crie um ambiente virtual com Python 3.9. Use o comando abaixo para criar e ativar um ambiente virtual chamado tensorflow_env:

```bash
conda create -n tf_gpu_lncc_2_13 python=3.9
conda activate tf_gpu_lncc_2_13
```

* Resultado esperado do comando ```create -n tf_gpu_lncc_2_13 python=3.9```:

```bash
Downloading and Extracting Packages:
                                                                                
Preparing transaction: done                                                     
Verifying transaction: done                                                     
Executing transaction: done                                                     
#                                                                               
# To activate this environment, use                                             
#                                                                               
#     $ conda activate tf_gpu_lncc_2_13                                         
#                                                                               
# To deactivate an active environment, use                                      
#                                                                               
#     $ conda deactivate  
```

* Se ao rodar ```conda activate tf_gpu_lncc_2_13```  **CondaError: Run 'conda init' before 'conda activate'** execute os passos abaixo:

* Configure seu terminal atual para usar o Conda corretamente.

```bash
conda init
```

* Após executar o ```conda init```, você precisará fechar e reabrir o terminal que está usando, ou rode o comando abaixo para recarregar o terminal:

```bash
source ~/.bashrc
```

* Ative o ambiente conda novamente:

```bash
conda activate tf_gpu_lncc_2_13
```

2. Instalar a Versão Específica do TensorFlow com Suporte a GPU:

Após ativar o ambiente virtual, instale o TensorFlow 2.13, que é compatível com CUDA 11.8 e cuDNN 8.2:

 ```bash
pip install tensorflow==2.13
```

Especificar a versão exata do TensorFlow garante que você esteja usando uma versão estável e compatível com as bibliotecas CUDA e cuDNN carregadas.
