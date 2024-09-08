#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --ntasks=1
#SBATCH -p sequana_gpu_dev
#SBATCH -J str-101-hcpa
#SBATCH --time=12:00:00


# Carregar os módulos necessários
module load anaconda3/2024.02
module load cuda/11.8
module load cudnn/8.2_cuda-11.4

# Ativar o ambiente Conda
source activate tf_gpu_lncc_2_13

# Criar diretório de logs se não existir
mkdir -p logs

# Executar o script Python
python src/model_cnn_tensorflow.py
