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

## 3. Configuração do Ambiente

### O que é o comando `module load`?

O comando `module load` faz parte do Environment Modules, uma ferramenta que ajuda os usuários a gerenciar facilmente o ambiente de software em sistemas de computação de alto desempenho (HPC). Esta ferramenta permite que você carregue, descarregue, liste e manipule módulos de software de maneira flexível. Em supercomputadores como o Santos Dumont, isso é especialmente útil porque:

- **Variedade de Software:** Supercomputadores suportam muitos usuários diferentes, cada um com suas próprias necessidades de software. Em vez de ter todos os programas e versões disponíveis ao mesmo tempo, o sistema usa módulos para manter o ambiente limpo e gerenciável.
- **Versões Específicas:** Diferentes projetos podem exigir diferentes versões do mesmo software. Usando módulos, você pode carregar versões específicas de compiladores, bibliotecas, ferramentas e outros softwares necessários para o seu trabalho.
- **Evitar Conflitos:** Carregar e descarregar módulos ajuda a evitar conflitos entre versões de bibliotecas ou ferramentas que podem não ser compatíveis entre si.

### Como usar no LNCC?

1. **Ver Disponibilidade de Módulos:**
   - Antes de carregar um módulo, você pode verificar quais estão disponíveis com o comando:

     ```bash
     module avail
     ```

   - Isso listará todos os módulos disponíveis no sistema.

2. **Carregar um Módulo:**
   - Para carregar um módulo específico, você usa:

     ```bash
     module load nome_do_modulo
     ```

   - Substitua `nome_do_modulo` pelo nome real do módulo que você deseja usar, como `gcc`, `python`, `cuda`, etc.

3. **Verificar Módulos Carregados:**
   - Para ver quais módulos estão atualmente carregados no seu ambiente, use:

     ```bash
     module list
     ```

4. **Descarregar um Módulo:**
   - Se precisar remover um módulo do seu ambiente, você pode usar:

     ```bash
     module unload nome_do_modulo
     ```

5. **Ajuda para um Módulo Específico:**
   - Para obter informações detalhadas sobre um módulo, incluindo variáveis de ambiente que ele define ou caminhos, você pode usar:

     ```bash
     module help nome_do_modulo
     ```

### Exemplos Comuns de Módulos

- **Compiladores:** `gcc`, `intel`, `clang`
- **Bibliotecas Matemáticas:** `openblas`, `mkl`
- **Ambientes de Desenvolvimento:** `python`, `anaconda`, `cuda`
- **Ferramentas de HPC:** `mpi`, `hdf5`

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
