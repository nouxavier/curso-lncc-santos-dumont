# Introdução ao Supercomputador Santos Dumont (SDumont)

O Santos Dumont é um supercomputador dividido em duas principais seções: o **SDumont Base (B700)** e o **SDumont Expansão (BullSequana X)**. Cada seção é composta por diferentes tipos de nós, que são essencialmente computadores interconectados dentro do supercomputador. Vamos entender cada um desses nós:

## 1. SDumont Base (B700)

### 1.1. Nós de Computação B710 (Thin Node)

- **Quantidade**: 504 nós
- **Processadores (CPUs)**: Cada nó tem 2 CPUs Intel Xeon, totalizando 24 núcleos (12 por CPU)
- **Memória (RAM)**: 64GB por nó
- **Total de Núcleos**: 12.096 núcleos no total

### 1.2. Nós de Computação B715 com GPUs K40

- **Quantidade**: 198 nós
- **Processadores**: Semelhantes aos B710, com 2 CPUs Intel Xeon e 24 núcleos por nó
- **Memória**: 64GB por nó
- **GPUs**: Cada nó possui 2 GPUs Nvidia K40, usadas para acelerar tarefas que podem se beneficiar de processamento paralelo, como aprendizado de máquina ou simulações complexas
- **Total de Núcleos**: 4.752 núcleos no total

### 1.3. Nós de Computação B715 com Coprocessadores Xeon Phi

- **Quantidade**: 54 nós
- **Processadores**: 2 CPUs Intel Xeon, 24 núcleos por nó
- **Memória**: 64GB por nó
- **Coprocessadores**: 2 Xeon PHI por nó (atualmente inutilizáveis)
- **Total de Núcleos**: 1.296 núcleos no total

### 1.4. Nó de Computação Bull Sequana com GPUs V100 (para IA)

- **Quantidade**: 1 nó
- **Processadores**: 2 CPUs Skylake, 40 núcleos no total
- **Memória**: 384GB RAM
- **GPUs**: 8 Nvidia V100, com alta capacidade para tarefas de inteligência artificial
- **Conectividade**: 4 portas Infiniband de 100Gbps, que ajudam na comunicação ultra-rápida entre os nós

### 1.5. Nó de Computação MESCA2 (Fat Node) com Memória Compartilhada

- **Quantidade**: 1 nó
- **Processadores**: 16 CPUs Intel Ivy, com 240 núcleos no total
- **Memória**: 6TB RAM, ideal para tarefas que precisam de muita memória

## 2. SDumont Expansão (BullSequana X)

### 2.1. Nós Computacionais Bull Sequana X1120 (CPU)

- **Quantidade**: 246 nós com 2 CPUs Intel Xeon, 48 núcleos por nó e 384GB RAM

### 2.2. Nós Computacionais Bull Sequana X1120 (CPU com Memória Extra)

- **Quantidade**: 36 nós com 2 CPUs Intel Xeon, 48 núcleos por nó e 768GB RAM

### 2.3. Nós Computacionais Bull Sequana X1120 (GPU)

- **Quantidade**: 94 nós
- **Processadores**: 2 CPUs Intel Xeon, 48 núcleos por nó
- **Memória**: 384GB RAM
- **GPUs**: Cada nó possui 4 GPUs Nvidia Volta V100, otimizadas para tarefas de alto desempenho, como deep learning

## Rede de Comunicação

- **Base**: Os nós do SDumont Base são conectados por uma rede Infiniband FDR, com uma velocidade de 56Gb/s.
- **Expansão**: Os nós do SDumont Expansão utilizam uma rede Infiniband EDR, com uma velocidade de 100Gb/s, permitindo uma comunicação ainda mais rápida.

## Resumo

- **Thin Nodes (B710, B715)**: Usados para cálculos que exigem muitos núcleos de CPU, com alguns modelos incluindo GPUs para aceleração extra.
- **Fat Nodes (MESCA2)**: Oferecem grande capacidade de memória, ideal para tarefas que exigem muito espaço de RAM.
- **GPU Nodes (Bull Sequana com V100)**: Especialmente configurados para tarefas de inteligência artificial e aprendizado de máquina.
- **Conectividade Rápida**: Rede Infiniband para comunicação eficiente entre os nós, essencial para sincronização em cálculos distribuídos.
