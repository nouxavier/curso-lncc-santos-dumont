# Partições Disponíveis e suas Usabilidades

## Partições de CPU

- **cpu**: Ideal para tarefas que não requerem GPUs. Use para trabalhos de longa duração que exigem apenas CPU.
- **cpu_dev**: Partição para desenvolvimento e testes rápidos, limitada por tempo. Utilize para testes e desenvolvimento.
- **cpu_small**: Para tarefas menores ou menos intensivas em CPU. Boa para trabalhos pequenos que não requerem muitos recursos.
- **cpu_scal**: Para trabalhos escaláveis em CPU, como simulações que podem se beneficiar de muitos núcleos.
- **cpu_long**: Para trabalhos de CPU de longa duração. Use esta partição para simulações que precisam rodar por muito tempo.
- **cpu_shared**: Partição compartilhada para pequenos trabalhos em CPU. Útil para pequenos testes ou processos paralelos que não requerem muitos recursos dedicados.

## Partições de GPU

- **nvidia**: Para trabalhos que necessitam de GPUs. Ideal para modelos de aprendizado de máquina ou computação acelerada.
- **nvidia_dev**: Partição de desenvolvimento com GPUs, ótima para testes e ajustes rápidos.
- **nvidia_small**: Para trabalhos pequenos que utilizam GPU, como pequenas redes neurais ou processamento leve de dados.
- **nvidia_scal**: Para tarefas escaláveis em GPU, como treinamento de grandes redes neurais ou simulações que requerem múltiplas GPUs.
- **nvidia_long**: Para trabalhos longos que utilizam GPU. Ideal para treinamentos de modelos complexos que exigem tempo prolongado de execução.

## Partições Sequana

- **sequana_cpu**, **sequana_cpu_dev**, **sequana_cpu_long**: Partições dedicadas a tarefas em CPU, incluindo desenvolvimento e tarefas de longa duração no supercomputador Sequana.
- **sequana_gpu**, **sequana_gpu_dev**, **sequana_gpu_long**: Semelhante às partições GPU para tarefas que necessitam de GPUs, com tempo longo ou curto, e para desenvolvimento.

## Partição Heterogênea

- **het_scal**: Partição para tarefas que podem utilizar tanto CPUs quanto GPUs simultaneamente. Ideal para trabalhos que requerem uma combinação de processamento em CPU e GPU.

## Partições de Memória Grande

- **sd_cpu_bigmem**, **sequana_cpu_bigmem**: Para tarefas que requerem grande quantidade de memória RAM. Útil para processamento de grandes volumes de dados ou modelos que consomem muita memória.

## Partições Especializadas

- **mesca2** e **gdl**: Partições especializadas para projetos específicos ou usuários designados. Confirme a disponibilidade e requisitos de uso.
