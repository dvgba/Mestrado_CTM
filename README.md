# Simulador de Ruído Rosa e Análise de Reverberação

No campo da acústica arquitetônica, a compreensão das características do som, como o ruído rosa e a reverberação, é fundamental para o design de ambientes internos que atendam a critérios específicos de qualidade de som. Este capítulo descreve o desenvolvimento e a implementação de uma ferramenta de simulação acústica em Python que gera ruído rosa e analisa o tempo de reverberação em diferentes frequências para um ambiente definido. O objetivo é fornecer uma ferramenta para a análise acústica que possa auxiliar em estudos e projetos arquitetônicos.
O ruído rosa foi gerado aplicando um filtro passa-baixa a um sinal de ruído branco. Os coeficientes do filtro foram definidos com base em Long(2006), garantindo uma distribuição de energia uniforme por oitava. O algoritmo implementado em Python normaliza o sinal de áudio para garantir a máxima amplitude sem distorção.
Para a análise de reverberação, foi aplicada a fórmula de Sabine, adaptada para levar em conta a absorção por frequência, considerando as características específicas do piso e das paredes do ambiente. As dimensões do ambiente e os coeficientes de absorção de materiais específicos foram utilizados para calcular o tempo de reverberação em várias frequências (125 Hz, 250 Hz, 500 Hz, 1000 Hz, 2000 Hz, 4000 Hz).
A ferramenta de simulação desenvolvida fornece insights valiosos sobre as características acústicas de ambientes internos, sendo uma contribuição importante para o campo da acústica arquitetônica. A capacidade de analisar o tempo de reverberação em diferentes frequências permite uma compreensão mais profunda de como o som se comporta em um determinado espaço, o que é essencial para o design acústico eficiente de salas de concerto, teatros, salas de aula e outros espaços fechados.


## Como Usar

Para executar o simulador, você precisará ter Python instalado, juntamente com as seguintes bibliotecas: `numpy`, `matplotlib`, `seaborn`, `sounddevice`, e `pandas`.
