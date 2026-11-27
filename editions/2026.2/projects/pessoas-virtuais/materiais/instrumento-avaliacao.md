# Instrumento de Avaliação e Protocolo de Consolidação

Este documento descreve a estrutura dos formulários pré-oficina e pós-oficina consolidada na segunda aplicação do projeto, permitindo sua reutilização e a interpretação padronizada dos indicadores.

## Modo de Aplicação

- **Formato recomendado para público 60+:** folha impressa com fonte legível (tamanho mínimo 14 pt), canetas disponibilizadas pela equipe e leitura coletiva das instruções iniciais.
- **Pareamento anônimo:** identificar os pares pré e pós-oficina apenas por código sequencial (`P1`, `P2`, ..., `Pn`), sem coletar nome, telefone, CPF ou e-mail na folha de avaliação.
- **Momento de coleta:**
  - **Pré-oficina (5 min):** antes da contextualização inicial, contendo os itens `Q1` a `Q6`.
  - **Pós-oficina (5 min):** imediatamente após a síntese de boas práticas e antes da entrega dos fascículos e do encerramento, contendo os itens `Q1` a `Q8`.

## Estrutura dos Itens Avaliados

### Bloco A: Percepção Subjetiva e Autoconfiança (Escala Likert de 1 a 5)

Aplicado antes e depois da oficina (`1 = muito baixa / discordo totalmente` até `5 = muito alta / concordo totalmente`):

| Código | Dimensão avaliada | O que observa | Cuidado na interpretação |
| --- | --- | --- | --- |
| `Q1` | Confiança geral para lidar com tentativas de golpe digital | Segurança subjetiva percebida pelo participante no cotidiano digital | Mede percepção de autoeficácia, não substitui teste prático |
| `Q2` | Capacidade percebida de identificar conteúdo gerado por IA apenas "no olho" (inspeção visual ou auditiva) | Percepção sobre quão fácil seria notar sozinho uma voz ou imagem falsa | Notas menores ou moderadas no pós-oficina podem refletir ganho de prudência ao perceber o realismo do deepfake |
| `Q3` | Clareza sobre como confirmar um pedido suspeito por outro canal | Conhecimento percebido do procedimento de verificação independente | Deve ser lido em conjunto com as decisões nos cenários práticos |

### Bloco B: Julgamento em Cenários Práticos (Múltipla Escolha, Opções 1 a 3)

Aplicado antes e depois da oficina. Cada item apresenta uma situação curta com três condutas possíveis, sendo a **opção 3** a conduta segura esperada (interromper o fluxo imposto pelo contato suspeito e verificar por canal oficial ou independente):

| Código | Cenário avaliado | Conduta segura esperada (Gabarito = Opção 3) | Limitação observada na prática |
| --- | --- | --- | --- |
| `Q4` | Pedido urgente por WhatsApp simulando conhecido ou familiar | Não transferir valores e ligar para o número antigo já conhecido do familiar | Em grupos já atentos ao tema, pode ocorrer efeito teto parcial já no pré-teste |
| `Q5` | Contato de falsa central bancária relatando compra suspeita e pedindo dados | Encerrar a conversa sem informar dados do cartão e consultar o app oficial ou número no verso do cartão | Na segunda oficina houve 100% de acerto já no pré-teste, sugerindo criar alternativas mais sutis em edições futuras |
| `Q6` | Recebimento de link ou boleto com cobrança ou vantagem inesperada | Não clicar no link nem pagar sem conferir a origem diretamente no emissor oficial | Também apresentou efeito teto (100% no pré e pós-teste) |

**Nota sobre reutilização:** a planilha consolidada da segunda aplicação documenta integralmente as dimensões, escalas, gabaritos e respostas codificadas de `Q1` a `Q8` ([dados anonimizados em CSV](../evidencias/metricas-segunda-oficina.csv)). Como o arquivo editável original da diagramação impressa não foi arquivado separadamente no repositório, novas equipes devem redigir os enunciados mantendo exatamente estas dimensões e ampliar o grau de sutileza das opções incorretas em `Q4` a `Q6` para reduzir o efeito teto.

### Bloco C: Avaliação das Dinâmicas (Escala Likert de 1 a 5, exclusivo do Pós-Oficina)

| Código | Aspecto avaliado | Finalidade |
| --- | --- | --- |
| `Q7` | Impacto percebido da dinâmica de Inteligência Artificial (deepfake) | Verificar utilidade e clareza percebidas na demonstração do golpe familiar |
| `Q8` | Impacto percebido da simulação do falso banco (capturas sequenciais) | Verificar utilidade e clareza percebidas na análise pausada do golpe corporativo |

## Consolidação dos Resultados

1. **Contagens e denominadores:** registrar sempre quantos participantes estavam presentes e quantos responderam validamente aos dois momentos (`n` de `N`), evitando extrapolar resultados para não respondentes.
2. **Estatísticas descritivas:** calcular média e desvio-padrão amostral para `Q1`, `Q2`, `Q3`, `Q7` e `Q8`, além da proporção de acertos (`n/N`) em `Q4`, `Q5` e `Q6` e do escore prático global (soma de acertos de `0` a `3`).
3. **Ganho normalizado de Hake adaptado à escala de 1 a 5:** para comparar o avanço relativo das médias em `Q1` a `Q3`, utilizar:

$$
g = \frac{\bar{x}_{\text{depois}} - \bar{x}_{\text{antes}}}{5 - \bar{x}_{\text{antes}}}
$$

O índice expressa a fração do avanço máximo possível obtida pela turma em cada dimensão subjetiva, devendo sempre ser interpretado separadamente dos indicadores objetivos de decisão (`Q4` a `Q6`).
