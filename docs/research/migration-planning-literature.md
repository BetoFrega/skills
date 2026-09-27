# Pesquisa para migration-planning

Pesquisa realizada em 26 de setembro de 2026. Escopo: identificar referências sobre modernização de legado e contribuições para a skill existente. Nenhuma alteração na skill faz parte desta pesquisa.

## Evidência e limites

Foram consultados materiais primários: páginas dos autores e editoras, sumários e previews oficiais, um capítulo autorizado de *Software Architecture: The Hard Parts*, entrevistas dos autores e artigos dos responsáveis pelos padrões. Isso permite verificar os temas e aprofundar o capítulo disponível; não equivale à leitura integral dos livros. As propostas para a skill abaixo são uma síntese, não prescrições atribuídas literalmente aos autores.

## Referências principais para este método

Esta é uma seleção por pertinência ao método discutido, não um ranking universal de vendas ou influência.

| Referência | Contribuição para a migração |
| --- | --- |
| [Monolith to Microservices — Sam Newman](https://samnewman.io/books/monolith-to-microservices/) | Referência diretamente voltada à transição incremental: decidir se migrar, escolher por onde começar, substituir partes, separar dados e enfrentar as consequências operacionais. Inclui Strangler Fig, Branch by Abstraction e Parallel Run. |
| [Architecture Modernization — Nick Tune, com Jean-Georges Perrin](https://www.manning.com/books/architecture-modernization) | Relaciona arquitetura, necessidades do negócio e organização. Útil para escolher fronteiras, resultados e responsabilidades, além de trocar tecnologia. |
| [Software Architecture: The Hard Parts — Neal Ford, Mark Richards, Pramod Sadalage e Zhamak Dehghani](https://www.oreilly.com/library/view/software-architecture-the/9781492086888/) | Fundamenta decisões de decomposição: acoplamento, granularidade, dados, contratos, workflows e transações distribuídas. |
| [Working Effectively with Legacy Code — Michael Feathers](https://www.informit.com/store/working-effectively-with-legacy-code-9780132931779) | Oferece técnicas para criar testes e pontos de substituição em código difícil de alterar, permitindo proteger comportamento antes da mudança. |
| [Re-Engineering Legacy Software — Chris Birchall](https://www.manning.com/books/re-engineering-legacy-software) | Visão prática da recuperação de sistemas legados, combinando entendimento, testes, melhoria e decisões sobre reengenharia. |
| [Refactoring Databases — Scott W. Ambler e Pramod J. Sadalage](https://www.pearson.com/en-us/subject-catalog/p/refactoring-databases-evolutionary-database-design/P200000009235) | Evolução incremental do banco, incluindo mudanças estruturais que preservam comportamento e situações em que várias aplicações dependem dos dados. |
| [Building Evolutionary Architectures, segunda edição — Neal Ford, Rebecca Parsons, Patrick Kua e Pramod Sadalage](https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/) | Usa fitness functions e automação para verificar propriedades arquiteturais durante a evolução. Complementa testes de jornadas e resultados funcionais. |

Uma referência gratuita especialmente próxima da skill é a série [Patterns of Legacy Displacement, de Ian Cartwright, Rob Horn e James Lewis](https://martinfowler.com/articles/patterns-legacy-displacement/). É uma série de artigos, não um livro.

## O que The Hard Parts acrescenta

O livro trata das decisões difíceis ao decompor sistemas e coordenar suas partes. Seus autores apresentam a análise contextual de trade-offs como instrumento central: uma escolha que melhora uma propriedade pode piorar outra. Isso combina com a interação exigida pela skill: explicar consequências e alternativas no caso concreto. Fonte: [entrevista dos autores](https://www.thoughtworks.com/insights/podcasts/technology-podcasts/the-hard-parts-of-software-architecture).

O capítulo 7, disponível integralmente em um [PDF autorizado](https://www.thoughtworks.com/content/dam/thoughtworks/documents/books/bk_software_architecture_hard_parts_ch7_en.pdf), confronta forças para separar e para manter componentes juntos:

- **Separar:** coesão e escopo funcional, frequência de mudanças, escala e throughput, tolerância a falhas, segurança e extensibilidade.
- **Manter juntos:** transações de banco, coordenação do workflow, código compartilhado e relações entre dados.

Exemplo aplicado: extrair estoque pode permitir escala e evolução próprias. Se cada compra continuar exigindo várias chamadas síncronas e uma transação envolvendo compra, pagamento e estoque, a separação também introduz falhas parciais e coordenação. A recomendação precisa avaliar os dois lados. Essa aplicação é minha síntese do capítulo.

O [sumário oficial](https://www.oreilly.com/library/view/software-architecture-the/9781492086888/) também explicita a separação dos dados operacionais, ownership, acesso distribuído, orquestração/coreografia, sagas e contratos. Esses temas ajudam a investigar o que atravessa cada fronteira proposta. Eles não tornam microserviços, sagas ou um determinado mecanismo de rollout obrigatórios.

## Inclusões recomendadas

### 1. Benefício esperado e escolha do primeiro recorte

A skill já pergunta o motivo da migração, mas pode pedir um resultado verificável e usá-lo para priorizar recortes: autonomia de deploy, custo, capacidade, confiabilidade ou tempo de mudança. Comparar valor, risco e dependências ajuda a escolher o primeiro passo. Essa proposta deriva dos temas de objetivos e priorização em [Newman](https://samnewman.io/books/monolith-to-microservices/) e do alinhamento organizacional em [Architecture Modernization](https://www.manning.com/books/architecture-modernization).

Também explicitar o comportamento que precisa ser preservado e o que pode desaparecer ou mudar por decisão consciente. Migrar não exige reproduzir automaticamente todas as funcionalidades históricas. Fonte: [Feature Parity](https://martinfowler.com/articles/patterns-legacy-displacement/feature-parity.html).

### 2. Justificar a fronteira e o acoplamento restante

A skill já identifica contratos e dependências; falta exigir a avaliação dos motivos para separar e manter juntos. Para decomposição, perguntar quais dependências permanecem em dados, execução e deploy, e se impedem a autonomia desejada. A separação pode exigir passos preparatórios ou uma fronteira diferente. Base: [capítulo 7 de The Hard Parts](https://www.thoughtworks.com/content/dam/thoughtworks/documents/books/bk_software_architecture_hard_parts_ch7_en.pdf).

### 3. Projetar a arquitetura temporária

A skill prevê remover adaptadores ao final, mas pode tornar explícita sua escolha: o que será construído apenas para viabilizar a transição, seu custo, responsável e condição de retirada. Adaptadores, roteadores e tradução de modelos podem ser investimentos temporários úteis. Fonte: [Transitional Architecture](https://martinfowler.com/articles/patterns-legacy-displacement/transitional-architecture.html).

Considerar **Branch by Abstraction** quando a substituição pode ocorrer dentro do mesmo processo: introduzir uma interface que permita escolher entre implementações durante a transição. Não exige extrair um serviço. Fonte: [descrição de Sam Newman](https://samnewman.io/patterns/architectural/branch-by-abstraction/).

### 4. Detalhar estados intermediários de contratos e dados

A skill já cobre leituras compatíveis, transferência histórica e captura de mudanças. A inclusão é tornar os estados verificáveis: **expandir**, suportando contratos antigos e novos; **migrar**, transferindo consumidores e dados; **contrair**, removendo o antigo após comprovar a transição. Fonte: [Parallel Change, de Danilo Sato](https://martinfowler.com/bliki/ParallelChange.html).

Aplicação proposta para dados: matriz de compatibilidade de leitores/escritores por estado, retomada de backfill após falha, sincronização pendente e condição de transferência da autoridade. Isso detalha requisitos existentes; não é uma lacuna completa.

### 5. Separar retorno técnico de compensação de negócio

Se uma fronteira dividir uma transação, discutir quais invariantes ainda precisam ser atômicas, quais resultados parciais são aceitáveis e como tratar ações já confirmadas. Devolver tráfego ao legado não desfaz uma cobrança. Compensar uma operação de negócio tem regras próprias e pode falhar. A necessidade de estudar isso vem dos capítulos de transações, workflows e sagas no [sumário de The Hard Parts](https://www.oreilly.com/library/view/software-architecture-the/9781492086888/); esta distinção operacional é uma aplicação proposta para a skill.

### 6. Verificar a arquitetura pretendida

Além das jornadas automatizadas já previstas, escolher verificações dos benefícios arquiteturais relevantes: deploy independente, restrições de dependências, compatibilidade de contratos ou limites de latência entre componentes. Essas verificações devem proteger objetivos acordados, sem impor ferramentas específicas. Base: [Building Evolutionary Architectures, segunda edição](https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/).

### 7. Preparar a mudança no código e na operação

Quando faltarem testes, caracterizar comportamentos relevantes antes de substituí-los e criar pontos seguros de intervenção. Isso complementa TDD e shadow testing; não exige editar a skill de implementação. Base: [Working Effectively with Legacy Code](https://www.informit.com/store/working-effectively-with-legacy-code-9780132931779).

Definir também quem opera o destino e quem sustenta a coexistência. Atribuir ownership de consumidores, já previsto na skill, não resolve sozinho responsabilidade operacional e capacidade dos times. Essa proposta aplica a perspectiva de [Architecture Modernization](https://www.manning.com/books/architecture-modernization).

## Como incorporar sem sobrecarregar o fluxo

Minha recomendação é acrescentar ao fluxo principal resultado esperado, justificativa da fronteira, arquitetura temporária e verificação dos objetivos arquiteturais. Detalhes de dados, transações e caracterização podem ficar em referências acionadas pelo contexto. Preservar a conversa sobre impacto e estratégia como centro do método, as preferências já acordadas e as convenções do repositório para issue tracking.

Não há motivo para repetir os procedimentos existentes de canário, afinidade, autoridade única, sombra, recuperação e inventário. A contribuição desta pesquisa é aprofundar decisões anteriores à exposição e critérios de sucesso posteriores à troca.
