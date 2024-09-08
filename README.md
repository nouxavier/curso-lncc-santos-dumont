Aqui está o README ajustado e organizado para servir como um guia abrangente para o seu curso:

---

# Explorando o Poder dos Supercomputadores: Treinamento de Modelos com GPUs no Santos Dumont

Este curso oferece um passo a passo detalhado para submeter trabalhos (jobs) no supercomputador Santos Dumont utilizando recursos de GPU. Vamos explorar diferentes estratégias de submissão, incluindo o uso de uma GPU única, múltiplas GPUs e técnicas avançadas para otimização do uso dos recursos disponíveis. Além disso, abordaremos a configuração de ambientes, monitoramento de jobs e análise de resultados.

## Índice

1. [Introdução](#introdução)
2. [Pré-requisitos](#pré-requisitos)
3. [Configuração do Ambiente](#configuração-do-ambiente)
   - [Carregar Módulos Necessários](#carregar-módulos-necessários)
   - [Configuração de Ambientes Virtuais com Anaconda](#configuração-de-ambientes-virtuais-com-anaconda)
   - [Carregar CUDA e cuDNN](#carregar-cuda-e-cudnn)
4. [Transferência de Scripts para o LNCC](#transferência-de-scripts-para-o-lncc)
   - [Testar Localmente o Script](#testar-localmente-o-script)
5. [Submissão de Jobs](#submissão-de-jobs)
   - [Usando uma GPU](#usando-uma-gpu)
   - [Usando Múltiplas GPUs](#usando-múltiplas-gpus)
   - [Submissão de Jobs Paralelos](#submissão-de-jobs-paralelos)
6. [Monitoramento e Controle de Jobs](#monitoramento-e-controle-de-jobs)
   - [Comandos Úteis do SLURM](#comandos-úteis-do-slurm)
   - [Análise de Logs e Resultados](#análise-de-logs-e-resultados)
7. [Dicas de Otimização](#dicas-de-otimização)
   - [Gerenciamento de Recursos](#gerenciamento-de-recursos)
   - [Balanceamento de Carga](#balanceamento-de-carga)
8. [Exemplos de Scripts de Submissão](#exemplos-de-scripts-de-submissão)
9. [Resolução de Problemas Comuns](#resolução-de-problemas-comuns)
10. [Referências e Recursos Adicionais](#referências-e-recursos-adicionais)

## Introdução

Este curso foi criado para guiar alunos de mestrado e doutorado no uso do supercomputador Santos Dumont para tarefas que requerem processamento pesado, como o treinamento de modelos de aprendizado de máquina com GPUs. O objetivo é fornecer conhecimento prático sobre como configurar, submeter e monitorar jobs, além de otimizar o uso dos recursos disponíveis.

## Pré-requisitos

Antes de começar, certifique-se de que você tem acesso ao supercomputador Santos Dumont e que está familiarizado com os conceitos básicos de Linux e de submissão de jobs com o SLURM.

- Acesso ao supercomputador Santos Dumont
- Conhecimento básico de Linux
- Conhecimento básico de Python e bibliotecas de machine learning (TensorFlow, PyTorch, etc.)

## Configuração do Ambiente

### Carregar Módulos Necessários

Antes de submeter um job, você precisa carregar os módulos apropriados no SDumont, como Anaconda, CUDA e cuDNN. Use o comando abaixo para carregar a versão mais recente do Anaconda:

```bash
module load anaconda3/2024.02
```

### Configuração de Ambientes Virtuais com Anaconda

Para isolar as dependências do seu projeto e evitar conflitos entre pacotes, é recomendável criar um ambiente virtual com Python 3.9, compatível com a versão mais recente do TensorFlow:

```bash
conda create -n tf_gpu_lncc_2_13 python=3.9
conda activate tf_gpu_lncc_2_13
```

Se ocorrer o erro **CondaError: Run 'conda init' before 'conda activate'**, siga os passos:

```bash
conda init
source ~/.bashrc
conda activate tf_gpu_lncc_2_13
```

### Carregar CUDA e cuDNN

Para aproveitar a aceleração por GPU no TensorFlow, carregue as bibliotecas CUDA e cuDNN:

```bash
module load cuda/11.8
module load cudnn/8.2_cuda-11.4
```

Verifique se os módulos foram carregados corretamente com:

```bash
module list
```

## Transferência de Scripts para o LNCC

Para transferir seus scripts para o LNCC, você pode utilizar ferramentas como:

- **FileZilla**
- **MobaXterm**
- **VS Code com Extensões SSH e Remote**: Este curso recomenda o uso do VS Code com as extensões "Remote - SSH" e "Remote - WSL" para uma integração mais suave. Confira o [tutorial](https://www.youtube.com/watch?v=LD-EAh9iTGc) para configuração.

### Testar Localmente o Script

Antes de submeter o script para execução no LNCC, teste-o localmente no ambiente configurado:

```bash
pip install -r requirements.txt
cd src
python seu_script.py
```

## Submissão de Jobs

### Usando uma GPU

Para submeter um job utilizando uma única GPU, utilize o script de submissão (`job_gpu.sh`):

```bash
#!/bin/bash
#SBATCH --job-name=meu_job_gpu
#SBATCH --partition=sequana_gpu
#SBATCH --gres=gpu:1
#SBATCH --time=01:00:00
#SBATCH --output=logs/%x-%j.out

module load anaconda3/2024.02
conda activate tf_gpu_lncc_2_13
python src/model_cnn_tensorflow.py
```

Submeta o script com:

```bash
sbatch job_gpu.sh
```

### Usando Múltiplas GPUs

Para usar mais de uma GPU, ajuste o parâmetro `--gres`:

```bash
#!/bin/bash
#SBATCH --job-name=meu_job_multi_gpu
#SBATCH --partition=sequana_gpu
#SBATCH --gres=gpu:4
#SBATCH --time=02:00:00
#SBATCH --output=logs/%x-%j.out

module load anaconda3/2024.02
conda activate tf_gpu_lncc_2_13
python src/model_cnn_tensorflow.py
```

Submeta o script com:

```bash
sbatch job_multi_gpu.sh
```

### Submissão de Jobs Paralelos

Para aproveitar os recursos de paralelismo, utilize MPI ou o MirroredStrategy do TensorFlow para distribuir o treinamento entre múltiplas GPUs.

## Monitoramento e Controle de Jobs

### Comandos Úteis do SLURM

- **Verificar status dos jobs:**

```bash
squeue -u seu_usuario
```

- **Monitorar detalhes de um job específico:**

```bash
sacct -lj <job_id>
```

- **Cancelar um job:**

```bash
scancel <job_id>
```

### Análise de Logs e Resultados

Os resultados dos jobs, incluindo logs e mensagens de erro, são salvos no diretório especificado com o parâmetro `--output`. Revise esses arquivos para ajustar e depurar seu código.

## Dicas de Otimização

### Gerenciamento de Recursos

Ajuste a alocação de CPUs, GPUs e memória para evitar o uso excessivo de recursos e minimizar o tempo de espera na fila.

### Balanceamento de Carga

Divida o trabalho em tarefas menores para uma melhor distribuição do processamento, garantindo um uso eficiente dos recursos.

## Exemplos de Scripts de Submissão

- **[Modelo TensorFlow 2.13 Básico](https://github.com/nouxavier/curso-lncc-santos-dumont/blob/main/src/model_cnn_tensorflor.py)**

## Resolução de Problemas Comuns

Esta seção ajuda a diagnosticar problemas comuns, como falhas na submissão de jobs, erros de memória ou configurações de ambiente incorretas.

## Referências e Recursos Adicionais

- [Documentação do SLURM](https://slurm.schedmd.com/documentation.html)
- [Tutoriais de TensorFlow](https://www.tensorflow.org/tutorials)
- [Guias do Santos Dumont](https://sdumont.lncc.br/)