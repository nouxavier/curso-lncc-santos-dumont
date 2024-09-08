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

## 3. Transferir o scripts para o LNCC

Você precisa transferir seu script Python e qualquer outro arquivo necessário para o sistema do LNCC. Você pode usar o comando scp (secure copy) ou um cliente de FTP seguro como sftp.
Algumas ferramentas são:
* FileZilla
* MobaXterm
* Jupyter Notebooks com JupyterHub
* Open OnDemand
* [**A escolhida neste curso**] VS Code com Extensões SSH e Remote:
  * Como Configurar:
    * Instale as extensões "Remote - SSH" e "Remote - WSL".
    * Conecte-se ao servidor LNCC via SSH dentro do VS Code.
    * Edite scripts, execute comandos e gerencie arquivos com uma interface integrada.
    * [Tutorial de como utilizar essa extensão](https://www.youtube.com/watch?v=LD-EAh9iTGc)


## 4. Configurar o Ambiente Virtual com TensorFlow

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

2. Instalar as Dependências Usando o **requirements.txt**

```bash
pip install -r requirements.txt
```

## 4. Testar Localmente o Script
Antes de enviar o script para execução no LNCC, é uma boa prática testar localmente no ambiente configurado para garantir que ele roda sem erros:

Execute seu script para verificar se ele roda corretamente:

```bash
cd src
python seu_script.py
```

# Submeter o Script à Fila
Para enviar seu script para a fila de execução no supercomputador Santos Dumont (ou em outro sistema de HPC - High-Performance Computing que utilize um gerenciador de filas como o SLURM - Simple Linux Utility for Resource Management), você precisará criar um script de submissão. Esse script define os recursos necessários para o seu trabalho (como tempo de execução, número de CPUs, uso de GPU, etc.) e instrui o sistema a executar seu script Python no ambiente configurado.

1. Crie um Script de Submissão (job.sh)

2. Submeter o Trabalho para a Fila:

Use o comando sbatch para submeter o script à fila:
```bash
sbatch job.sh
```
* Resultado do comando com sucesso: 

```bash
Submitted batch job 11220048
```

3. Monitorar o Status do Job

Para obter detalhes completos sobre o status e o histórico do job específico, utilize o comando ```sacct```. Esse comando fornece informações detalhadas sobre o uso de recursos, status de execução, e possíveis erros:


```bash
sacct -lj <ID JOB>
```

4. Monitorar o Status do Trabalho:
Para verificar o status atual dos seus trabalhos em tempo real enquanto eles estão na fila ou sendo executados, use o comando squeue

```bash
squeue -u seu_usuario
```
