# Guia de Uso do Supercomputador Santos Dumont - LNCC

## 1. Preparar o Ambiente

1. **Receber Credenciais:**
   - Após a aprovação, você receberá suas credenciais de acesso e informações sobre como conectar-se ao sistema.

2. **Instalar Ferramentas de Acesso:**
   - Instale ferramentas necessárias para o acesso remoto, como um cliente SSH.

## 2. Conectar-se ao Santos Dumont

1. **Ative sua VPN:**
   - As conexões externas deverão obrigatoriamente ser feitas através da VPN do LNCC.

1. **Acesso via SSH:**
   - Use um cliente SSH para conectar ao supercomputador:

     ```bash
     ssh username@hostname
     ```

2. **Configuração do Ambiente:**
   - Após o login, configure seu ambiente conforme necessário:

     ```bash
     module load nome_do_modulo
     ```

## 3. Submeter Tarefas

1. **Escrever Jobs:**
   - Prepare scripts de submissão de jobs. Um exemplo básico de script SLURM é:

     ```bash
     #!/bin/bash
     #SBATCH --job-name=meu_job
     #SBATCH --output=meu_job_output.log
     #SBATCH --ntasks=1
     #SBATCH --time=01:00:00
     
     module load python/3.8
     srun python meu_script.py
     ```

2. **Submeter o Job:**
   - Submeta o script de job com:

     ```bash
     sbatch meu_script.sh
     ```

## 4. Monitorar e Gerenciar Jobs

1. **Verificar Status:**
   - Verifique o status dos seus jobs com:

     ```bash
     squeue -u username
     ```

2. **Consultar Logs:**
   - Verifique os logs de saída e erro dos seus jobs para monitorar o progresso e depurar problemas.

## 6. Consultar a Documentação e Suporte

- **Documentação:**
  - Consulte a [documentação fornecida pelo LNCC](https://www.lncc.br/) para detalhes específicos sobre configuração do ambiente, módulos disponíveis e melhores práticas.

- **Suporte:**
  - Para assistência, entre em contato com a equipe de suporte do LNCC através do canal de suporte técnico disponível no site.
