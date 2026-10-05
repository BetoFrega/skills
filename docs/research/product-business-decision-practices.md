# Pesquisa: documentação canônica de produto e negócio em AIFSD

Pesquisa realizada em **4 de outubro de 2026**. Escopo: práticas para preservar decisões, justificativas e regras vigentes de produto e negócio; implicações para as skills deste repositório. A pesquisa não altera skills, configuração, instalações ou registros de projetos.

O [modelo acordado na entrevista de product owner](../design/product-documentation-model.md) registra as decisões posteriores a esta pesquisa, incluindo catálogo adaptável, valor e custo separados e manutenção por agentes dos estados de deployment, release e flags.

A recomendação é organizar **um processo comum para decisões significativas**, associado a contratos explícitos e padronizados que mostram a direção e as regras atuais. Classificar decisões como produto, negócio e arquitetura ajuda a encontrá-las; criar três sistemas independentes de registros pode dificultar sua manutenção. Os nomes PDR e BDR podem ser convenções locais, mas esta seleção de fontes não sustenta tratá-los como padrões universais.

**Requisito explícito do usuário para AIFSD:** desenvolver com agentes exige mais documentação de produto e mais padronização do que depender do contexto tácito de uma equipe tradicional. Nesta proposta, proporcionalidade ajusta a profundidade da deliberação e a governança; não autoriza omitir contratos vigentes, comportamentos proibidos ou exceções. Um conjunto de notas breves de decisão não cobre sozinho essa necessidade.

O conteúdo e o ciclo de vida devem ser independentes da ferramenta. Cada projeto escolhe seu destino canônico e a representação adequada: documento, página, registro de base de dados, arquivo ou outro objeto suportado. **Esta nota Markdown é o resultado da pesquisa; não estabelece onde futuras decisões devem morar.**

## Evidência e limites

Foram lidas fontes primárias de autores de métodos e handbooks das organizações que os praticam. As fontes combinam prescrições profissionais e relatos de implementação; não constituem um estudo comparativo que demonstre uma única prática superior para todos os produtos. Publicações históricas foram identificadas como tais. Páginas de handbook e templates podem mudar depois da consulta.

Distingo abaixo:

- **Afirmação da fonte:** o que o autor ou a organização recomenda explicitamente.
- **Implementação observada:** a forma como a organização descreve seu próprio processo.
- **Síntese proposta:** nossa adaptação ao trabalho de agentes e às preferências deste projeto.

Não foi adotada a alegação promocional de aumento percentual de sucesso presente na página DACI: esta pesquisa não verificou sua base empírica. Também não se presume que GitLab, Basecamp ou qualquer ferramenta imponha o destino dos nossos registros.

## Fontes primárias e suas contribuições

| Fonte | Data ou recorte consultado | Contribuição verificável e limite |
| --- | --- | --- |
| [Teresa Torres — Product Discovery Basics](https://www.producttalk.org/product-discovery/) | Publicado em 18/08/2021; versão consultada em 04/10/2026. | Discovery é um processo de decisão contínuo: conectar resultados desejados, oportunidades e soluções; envolver clientes e testar hipóteses. Distingue resultados de negócio e comportamentos no produto. Não prescreve um sistema PDR/BDR. |
| [Marty Cagan / SVPG — Product Leadership Is Hard](https://www.svpg.com/product-leadership-is-hard/) | 19/11/2020. | Liderança fornece contexto estratégico: missão, visão, princípios, estratégia e objetivos. Princípios orientam escolhas entre valores concorrentes; objetivos expressam problemas de cliente ou negócio a resolver. Não é um template de registro histórico de decisão. |
| [GitLab — Making Decisions](https://handbook.gitlab.com/handbook/leadership/making-decisions/) | Handbook consultado em 04/10/2026; última modificação exibida: 01/12/2025. | Define DRI, coleta de contribuições e proposta breve com alcance, tempo, pessoas, alternativas, escolha e justificativa. Reconhece julgamentos com dados limitados, desde que explícitos. A proposta pode estar numa agenda, issue ou Google Doc. |
| [Atlassian — DACI Decision-Making Framework](https://www.atlassian.com/team-playbook/plays/daci) | Playbook vivo consultado em 04/10/2026. | Separa Driver, um Approver, Contributors e Informed. Recomenda reunir contexto, dados, critérios e opções; registrar e compartilhar a decisão final para leitores futuros. Seu processo completo é mais pertinente a decisões complexas e relevantes do que a toda escolha cotidiana. |
| [GitLab — Handbook Usage](https://handbook.gitlab.com/handbook/about/handbook-usage/) | Última modificação exibida: 28/07/2026; consulta em 04/10/2026. | Distingue sistema autoritativo de fonte única e recomenda eliminar repetição, vincular conteúdos relacionados e atribuir localização e responsável. As preferências de ferramentas do handbook são da GitLab, não requisitos para o nosso setup. |
| [Jeff Bezos / Amazon — 2016 Letter to Shareholders](https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders) | Carta referente a 2016; versão institucional consultada em 04/10/2026. | Rejeita um processo único para todas as decisões: escolhas reversíveis comportam processo leve; correção rápida e escalada de desalinhamentos importam. A referência a aproximadamente 70% da informação é uma orientação contextual, não um limiar mensurável a impor na skill. |
| [Ryan Singer / Basecamp — The Betting Table, Shape Up](https://basecamp.com/shapeup/2.2-chapter-08) | Capítulo da edição online consultado em 04/10/2026. | Descreve decisões de investimento em trabalho: opções são pitches; a aposta compromete capacidade e limita a perda. Existe um mecanismo de interrupção e reconsideração. Não equivale a uma política permanente e não demonstra que um log separado seja sempre necessário. |
| [Michael Nygard — Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) | 15/11/2011. | Registros pequenos preservam uma decisão significativa, contexto e consequências; quando substituída, a decisão antiga permanece ligada à sucessora. O método original trata arquitetura; sua aplicação a produto e negócio é uma adaptação nossa. |
| [MADR — site e template dos mantenedores](https://adr.github.io/madr/) | Site consultado em 04/10/2026; anuncia MADR 4.0.0 em 17/09/2024; template exibido é identificado como versão de desenvolvimento. | Oferece versões mínimas e completas, status inclusive rejected, participantes, alternativas, confirmação e referências. Aceita uso para outras decisões importantes, mantendo foco em arquitetura. Não impõe uma organização universal dos registros. |
| [GitLab — Confidentiality Levels](https://handbook.gitlab.com/handbook/communication/confidentiality-levels/) | Última modificação exibida: 12/03/2026; consulta em 04/10/2026. | Distingue informação pública, interna e de acesso limitado. Estratégia, dados pessoais, negociação e pricing podem demandar públicos diferentes. Demonstra que um registro canônico de negócio não precisa ser acessível a todos, nem que um handbook interno seja proteção suficiente para todo conteúdo. |
| [Business Rules Group — Business Rules Manifesto](https://www.businessrulesgroup.org/brmanifesto.htm) | Versão 2.0, 01/11/2003, editada por Ronald G. Ross; página consultada em 04/10/2026. | Diferencia termos, fatos e regras; exige regras explícitas, coesas e consistentes, formuladas para validação por negócio. Distingue regra de sua implementação e representa exceções por regras. É um manifesto histórico, não prova empírica de AIFSD nem recomendação automática de rules engine. |
| [OpenAI — Harness engineering](https://openai.com/index/harness-engineering/) | Relato de Ryan Lopopolo sobre cinco meses de desenvolvimento com agentes; consulta em 04/10/2026. | Relata uma base estruturada com documentos de produto, índice curto, verificações de estrutura e atualização. Informação acessível ao agente e manutenção contínua são centrais. Usar Git foi uma escolha daquele ambiente; o relato não prova que todo projeto deva usar o mesmo destino ou fluxo. |
| [GitHub Spec Kit — Spec Persistence Models](https://github.github.com/spec-kit/concepts/spec-persistence.html) | Documentação dos mantenedores consultada em 04/10/2026. | Distingue histórico de mudanças, reconciliação entre artefatos e contrato vivo com planos/tarefas derivados. A escolha precisa ser explícita. Descartar derivados pode perder justificativas, que precisam ser preservadas em outro lugar. Não há modelo obrigatório nem configuração universal de CLI. |
| [Birgitta Böckeler — Understanding Spec-Driven-Development](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) | Avaliação prática de três ferramentas publicada em 2025; consulta em 04/10/2026. | Distingue spec-first, spec-anchored e spec-as-source. Questiona manutenção, duplicação, sobrecarga de revisão e confiança indevida em instruções. É análise de ferramentas daquele momento; não substitui verificação das capacidades atuais nem invalida o requisito de documentar mais produto. |

## O que a evidência muda na proposta inicial

### 1. Histórico de decisões e orientações atuais têm funções diferentes

Visão, estratégia e princípios proporcionam contexto para futuras escolhas na abordagem da [SVPG](https://www.svpg.com/product-leadership-is-hard/). O [formato de Nygard](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) preserva por que uma escolha particular foi feita e por que deixou de valer. São necessidades complementares.

**Síntese proposta:** uma pessoa ou agente precisa conseguir responder tanto “por que decidimos assim?” quanto “qual regra devo aplicar agora?”. O histórico pode ser um conjunto de registros; a visão atual pode ser uma política, um documento estratégico ou uma consulta filtrada da própria base. Não é obrigatório criar uma cópia resumida separada. Se houver consolidação, seu responsável e a relação com os registros devem estar definidos.

Um exemplo hipotético: a decisão de permitir anúncios por empresas explica a escolha e as alternativas; a política vigente de anunciante estabelece elegibilidade, poderes e exceções; a spec descreve a mudança de comportamento; os tickets distribuem o trabalho. Publicar uma implementação não determina, por si, qual regra foi aprovada.

### Regras vigentes precisam de um contrato próprio

O [Business Rules Manifesto](https://www.businessrulesgroup.org/brmanifesto.htm), artigos 2 a 5, separa conceitos, fatos e regras e exige que as regras sejam explícitas e consistentes. Regras atravessam processos; sua validade não depende de estarem transcritas num fluxo ou numa implementação. Exceções também precisam ser expressas.

**Síntese proposta:** manter três funções identificáveis: contexto estratégico vigente, contrato normativo vigente de produto/negócio e histórico das escolhas. Um PDR/BDR explica a origem de uma política, mas não substitui automaticamente um contrato completo do que é permitido, obrigatório ou proibido agora. O contrato pode ser uma vista estruturada dos mesmos registros se for suficientemente completo e inequívoco; não precisa ser um documento duplicado.

Neste repositório, [domain-modeling](../../skills/domain-modeling/SKILL.md) define expressamente `CONTEXT.md` como um glossário. Seu [formato](../../skills/domain-modeling/CONTEXT-FORMAT.md) contém termos e definições; não é uma referência completa de direitos, estados, exceções e regras de negócio. Ampliar documentação de produto requer acrescentar esse contrato na configuração, sem transformar silenciosamente o glossário em outro objeto.

### 2. Classificação ajuda; novos acrônimos não resolvem autoridade

Na [GitLab](https://handbook.gitlab.com/handbook/leadership/making-decisions/), decisões de alcances diferentes usam um processo comum. O [MADR](https://adr.github.io/madr/) permite registrar decisões importantes além de arquitetura. Nesta amostra, não apareceu uma taxonomia comum obrigatória ADR/PDR/BDR.

**Síntese proposta:** começar com um registro comum e um campo ou classificação de domínio: produto, negócio, arquitetura, operação ou combinação relevante. ADR continua útil quando o objeto é uma decisão arquitetural e o projeto já tem essa convenção. PDR/BDR só justificam formatos próprios quando diferirem materialmente em conteúdo, autoridade, visibilidade ou ciclo de vida.

Uma decisão de monetização pode afetar experiência, operação e tecnologia. Sua justificativa não deve ser copiada para três registros. Decisões derivadas distintas podem ter seus próprios registros com links; uma decisão única atravessando domínios mantém uma identidade canônica.

### 3. Decidir é diferente de aprovar a execução e de comprovar um resultado

O [DACI da Atlassian](https://www.atlassian.com/team-playbook/plays/daci) distingue participação da autoridade final; o [DRI da GitLab](https://handbook.gitlab.com/handbook/leadership/making-decisions/) consulta e decide dentro do próprio alcance. Os modelos diferem, mas ambos tornam explícito quem pode decidir.

**Síntese proposta:** registrar quem decidiu, em qual alcance, quando e com qual evidência. Uma aprovação já dada na conversa pode bastar conforme a governança do projeto; não há razão para repetir a pergunta automaticamente. Aceitação de uma proposta, autorização para executar, implantação e resultado observado são informações separadas. A skill não ganha autoridade de produto ou negócio apenas por ser agent-callable.

### 4. Evidência precisa continuar ligada ao aprendizado

[Torres](https://www.producttalk.org/product-discovery/) liga decisões a resultados, oportunidades de cliente e testes de hipóteses. [Shape Up](https://basecamp.com/shapeup/2.2-chapter-08) apresenta uma aposta como compromisso limitado, sujeito a reconsideração, e não como certeza de sucesso.

**Síntese proposta:** a decisão deve indicar o resultado pretendido e as hipóteses materiais, com links para pesquisas e testes. Aprovar um experimento não comprova a hipótese nem estabelece automaticamente uma política permanente. Evidência posterior pode confirmar uma expectativa, contrariá-la ou ser inconclusiva; cada caso deve conservar sua data e limites.

## Objetos que o processo deve reconhecer

Esta divisão é uma proposta funcional, não uma lista de documentos que todo projeto deve criar.

| Objeto | Pergunta principal | Como participa da autoridade |
| --- | --- | --- |
| Estratégia, visão e princípios | Para quem criamos valor, que resultado buscamos e quais escolhas priorizamos? | Contexto vigente para decisões futuras; uma estratégia pode ter horizonte próprio. |
| Política ou contrato de domínio | Quais regras, direitos, limites e exceções valem agora? | Referência normativa para o comportamento atual, com responsáveis e vigência definidos. |
| Registro de decisão | O que escolhemos, por quem, quando e por quê? | Preserva a escolha, sua justificativa e seu ciclo de vida; pode também ser a referência direta da regra vigente. |
| Evidência e experimentos | O que sabemos, o que supomos e o que aprendemos? | Sustenta o raciocínio; uma observação ou hipótese não é uma decisão aprovada. |
| Spec de mudança | Que comportamento e critérios concretos este trabalho deve satisfazer? | Deriva das decisões aplicáveis; descreve um incremento e não muda silenciosamente uma regra de produto ou negócio. |
| Ticket | Que trabalho executar e verificar? | Rastreia execução, dependências e evidência de conclusão. |

Mais de uma função pode caber no mesmo objeto nativo. Separar funções conceituais não obriga a multiplicar arquivos, páginas ou bases.

## Formato comum de um registro de decisão, independente de destino

Os campos abaixo são nossa síntese para autoria por agentes. O projeto pode mapeá-los para propriedades nativas, seções de texto ou uma combinação. Exigir informação não exige que todo campo vire uma seção vazia.

| Informação | Conteúdo esperado |
| --- | --- |
| Identidade e pergunta | Título específico e identidade ou referência estável; a escolha que está sendo resolvida. |
| Alcance | Produto, domínio, público, cenário e fronteiras a que se aplica; exclusões relevantes. |
| Estado e tempo | Proposta, aceita, rejeitada, substituída ou retirada; datas conhecidas e vigência quando diferente da aceitação. |
| Autoridade | Quem pode decidir, quem decidiu e evidência da aceitação; responsáveis diferentes por manutenção e execução quando necessário. |
| Contexto | Problema, restrições, decisões vigentes relacionadas e fatos relevantes daquele momento. |
| Escolha e justificativa | Resposta concreta, alternativas realmente consideradas e critérios que explicam a preferência. |
| Evidência e incerteza | Fontes datadas; hipóteses, limitações e questões abertas. Não inventar pesquisa para completar um template. |
| Consequências | Benefícios esperados, compromissos, custos, riscos e limitações; resultados observados claramente separados. |
| Reconsideração | Mudança de contexto, hipótese invalidada, sinal operacional ou fim de uma aposta que justifique revisão; responsável quando isso exigir acompanhamento. |
| Relações e visibilidade | Registros que complementa ou substitui; regras atuais, evidência, specs e tickets relacionados; público autorizado. |

Não exigir KPI quantitativo para toda decisão. Algumas escolhas estabelecem direitos, princípios ou consistência, e precisam de critérios compatíveis. Tampouco inventar alternativas que nunca foram examinadas. Uma decisão simples pode registrar todo esse conteúdo aplicável em poucos parágrafos. Isso reduz o tamanho do histórico da deliberação; não reduz a cobertura exigida do contrato atual de produto.

## AIFSD: documentação de produto completa e padronizada

Esta seção é uma **síntese para o requisito explícito do usuário**, baseada nas distinções de negócio e produto acima e nas fontes de desenvolvimento com agentes. Não existe aqui demonstração experimental de que um pacote específico de artefatos torne AIFSD eficaz.

No [relato da OpenAI](https://openai.com/index/harness-engineering/), o conhecimento é organizado em fontes aprofundadas, documentos de produto e um índice curto; estrutura, links e atualização recebem verificações. A equipe identifica contexto inacessível como uma limitação dos agentes. **Nossa adaptação:** o requisito é acesso confiável ao conteúdo canônico configurado. Um destino externo com integração verificável pode satisfazê-lo. Não importamos a escolha daquele time de colocar todo conhecimento no repositório.

O [Spec Kit](https://github.github.com/spec-kit/concepts/spec-persistence.html) distingue um contrato vivo de um histórico de diretórios por mudança. Isso esclarece a terminologia: **spec de mudança**, usada para realizar um incremento, e **contrato de produto mantido**, que alguns autores chamam de living spec, têm ciclos de vida diferentes. A organização aqui proposta preserva essa diferença sem impor o nome spec ao registro canônico pedido pelo usuário. Decisões continuam conservando justificativas que se perderiam ao regenerar planos e tarefas.

O agente precisa recuperar sem inferir de conversas antigas: a intenção do produto, as regras atuais, a origem aceita dessas regras e o que executar. Padronização deve definir conteúdo, semântica, relações e verificação; o destino escolhido determina sua representação. Uma base de dados e um documento podem expressar o mesmo contrato.

A direção vigente também precisa de conteúdo próprio: públicos e problemas atendidos, proposta de valor, limites do produto, posicionamento e escolhas estratégicas, princípios para resolver conflitos, objetivos e critérios de resultado. Modelo econômico, política comercial e compromissos operacionais entram quando determinam o produto. Essa cobertura é nossa adaptação do contexto estratégico da SVPG; não obriga a preencher um canvas universal antes de cada mudança.

| Parte do contrato vigente | Informação que precisa estar explícita |
| --- | --- |
| Identidade e autoridade | Identidades estáveis para regras e cenários, localização autoritativa, responsáveis, versão ou histórico e vigência; origem em decisão aceita ou outra autoridade já válida. |
| Atores e direitos | Quem pode fazer o quê, sobre quais objetos e em que condição; distinção entre identidade de negócio, papel e credencial técnica quando pertinente. |
| Termos e fatos do domínio | Referência ao glossário e às relações relevantes; evitar definir o mesmo conceito com sentidos diferentes. |
| Estados e transições | Estados de negócio, eventos, pré-condições, transições permitidas/proibidas e resultados relevantes. Não basta um desenho apenas do caminho feliz. |
| Invariantes e limites | O que deve permanecer verdadeiro; limites de escopo, disponibilidade, elegibilidade, valores ou prazos quando fazem parte da regra. |
| Exceções e caminhos negativos | Regra geral, exceções aprovadas, precedência, recusas, ausência de dados, falhas relevantes e efeitos que não podem ocorrer. |
| Linguagem normativa | Distinguir obrigação, proibição, permissão, expectativa e hipótese; usar termos normativos com significado definido e consistente no projeto. |
| Cenários verificáveis | Exemplos que demonstram a regra e a exceção, incluindo casos adversos; resultados esperados e observações necessárias para avaliar conformidade. |
| Rastreabilidade | Ligações entre regra vigente, decisão/proveniência, evidência, spec, ticket e cenário/teste quando existir. Não é necessário copiar conteúdo entre esses objetos. |
| Questões abertas | Lacunas materiais identificadas como não decididas; sem preenchê-las com convenções supostas pelo agente. |

Exemplo inteiramente hipotético: uma regra com identidade `RULE-MOD-001` afirma que uma pessoa sem papel de moderador não pode ocultar conteúdo de terceiros. Seu cenário negativo verifica tentativa, resultado de recusa e manutenção do estado do conteúdo. A regra liga à decisão que aprovou o limite; uma spec detalha o trabalho necessário e testes podem comprovar a implementação. O exemplo não estabelece uma política de moderação para um projeto real.

Um teste passa ou falha em relação a uma expectativa documentada; não decide sozinho se aquela expectativa é a política desejada. Quando código divergir da regra, investigar a divergência e sua autoridade antes de editar o contrato para acomodar a implementação. Uma reconstrução a partir de código ou tickets antigos deve identificar o que foi observado e o que ainda não tem aprovação comprovada.

**Norma e entrega possuem informações distintas:** registrar a regra aprovada, sua vigência e mudanças futuras já aceitas; vincular separadamente a evidência de implementação, rollout e observação em produção. Uma regra com vigência futura não substitui antecipadamente a regra atual. Uma diferença entre política efetiva e produto entregue precisa aparecer como divergência, com alcance conhecido, em vez de ser escondida pela última edição do documento.

Mais documentação significa cobrir conhecimento que antes dependia da memória da equipe. Mais padronização significa que produtor e consumidor sabem quais informações procurar, como interpretá-las e como preservar a autoridade. Progressão por camadas continua útil: índice e visão atual para orientação, contratos completos por domínio e referências históricas para aprofundamento. Essa navegação não dispensa a cobertura do conteúdo.

### Padrão de manutenção e consumo por agentes

**Síntese proposta:** antes de executar um incremento, o agente consulta os contratos aplicáveis e identifica lacunas relevantes para aquele trabalho. Não precisa modelar antecipadamente todo produto, mas não pode transformar uma lacuna material em uma política suposta. Identidades, estados e vocabulário têm significado definido; exemplos ajudam a demonstrar aplicação e limites das regras.

Uma alteração aprovada de produto deve deixar rastreáveis: a decisão, o contrato afetado, a mudança proposta no contrato e o trabalho derivado. Quando houver histórico separado, o raciocínio original permanece. Quando tudo couber em um objeto nativo, suas versões ou seções devem permitir recuperar tanto a orientação atual quanto sua origem. Antes de declarar o registro concluído, verificar a gravação e os vínculos no destino.

As verificações podem cobrir campos exigidos para cada objeto, referências quebradas, estados incompatíveis, lacunas no domínio alterado e cenários relevantes. Onde houver automação, exigir somente capacidades verificadas; onde não houver, usar revisão explícita. Um teste demonstra comportamentos específicos, não a completude de toda documentação.

A crítica de [Böckeler](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) à duplicação e ao volume gerado ajuda a formular o critério de qualidade: aumentar cobertura e precisão, manter informação por domínio e revisar mudanças concretas. Ter mais texto ou mais arquivos não comprova consistência. Informação fora de alcance, conflito não resolvido e hipótese não validada devem permanecer identificáveis.

## Setup: destino arbitrário, representação adequada e capacidades verificadas

**Este é um requisito explícito do usuário:** assim como os tickets, decisões não devem ser obrigadas a morar em Git, Notion, Confluence ou qualquer provedor particular. O setup deve perguntar onde o projeto quer mantê-las e configurar a representação apropriada.

Antes de perguntar, ler instruções e referências já existentes; não reabrir escolhas assentadas. Quando houver uma lacuna, resolver:

1. **Destino e alcance:** qual sistema e localização concreta são autoritativos; quais classes de registro estão incluídas; se os documentos com regras atuais ficam no mesmo lugar ou possuem referências próprias.
2. **Representação nativa:** qual objeto usar, como representar conteúdo e metadados, identidade, estados, links, busca, histórico e substituições. Não enviar Markdown bruto presumindo que todo destino interpreta Markdown.
3. **Governança:** quem decide, convenção de aprovação, responsável por manutenção, vigência e relação com as regras atuais. Respeitar governança já estabelecida.
4. **Visibilidade:** público dos registros, anexos e evidências; restrições reais de produto ou negócio. Destinos diferentes por classe podem ser legítimos, mas a mesma informação deve ter autoridade definida.
5. **Operações disponíveis:** verificar como localizar, ler, criar, atualizar e ler de volta no destino escolhido. Verificar links e histórico disponíveis antes de prometer busca global, relações nativas, versionamento ou substituição automática.
6. **Limitações e recuperação:** quando não houver integração, preparar uma proposta no formato solicitado e identificar o passo manual necessário. Um rascunho temporário não se torna canônico por ter sido escrito no workspace.

Configuração pode ser um documento de instruções que aponta para sistemas externos; não deve introduzir um segundo catálogo autoritativo por conveniência do agente. A exigência de não duplicar conteúdos aplica a prática de [fonte única da GitLab](https://handbook.gitlab.com/handbook/about/handbook-usage/) sem importar sua preferência de armazenamento.

Prescrever o formato significa definir um mapeamento concreto para o destino escolhido. Exemplos de representações possíveis, a verificar no setup:

| Representação escolhida | Padronização a configurar |
| --- | --- |
| Página ou documento | Modelo de seções, localização, metadados suportados, links, histórico e índice ou navegação. |
| Registro em base ou tabela | Propriedades, estados, corpo do registro, identidade, relações disponíveis e vistas para conteúdo vigente. |
| Arquivo versionado | Caminhos relativos, nome, metadados e corpo, convenção de alterações e navegação. |
| Outro objeto nativo | Equivalência explícita das informações necessárias; limitações registradas e ações manuais definidas. |

Esses são exemplos de adaptação, sem lista fechada de provedores. Uma projeção ou cópia usada para fornecer contexto ao agente deve indicar origem e versão/data de leitura e continuar subordinada à fonte autoritativa; não ganha autoridade pelo local onde foi salva.

Quando uma gravação tiver resultado desconhecido, procurar e ler antes de repetir a criação. Quando uma atualização envolver registro e política em objetos diferentes, não presumir atomicidade: verificar cada efeito e informar inconsistências ou execução parcial. Esses cuidados são propostas operacionais para agentes, não capacidades comprovadas de um conector.

## Fluxo recomendado

1. **Localizar a autoridade:** consultar o setup e os registros relevantes; buscar a mesma proposta antes de criar outro registro. Resultado vazio de uma busca limitada não prova inexistência.
2. **Escolher a proporção:** identificar relevância durável, alcance, efeito entre áreas e custo de reversão. Uma decisão cotidiana pode dispensar um registro histórico separado, mas mudanças em regra, ator, estado, exceção ou fronteira de produto precisam atualizar o contrato canônico correspondente. A proporcionalidade da [Amazon](https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders) se aplica aqui à deliberação e às aprovações, sem reduzir a documentação explícita exigida para AIFSD.
3. **Preparar ou recuperar a decisão:** distinguir proposta de escolha já tomada. Escrever a menor explicação suficiente, com incertezas explícitas e conflitos com regras vigentes identificados.
4. **Registrar o estado real:** usar a evidência de autorização existente no alcance correspondente. Uma ausência de consenso não significa ausência de autoridade; uma recomendação do agente não significa aceitação.
5. **Salvar e verificar:** escrever no destino configurado, ler de volta e validar estado, vínculos e identidade. Atualizar a referência atual quando houver uma mudança normativa já aceita e vigente; specs e tickets apontam para ela.
6. **Revisar quando houver motivo:** manter a justificativa histórica. Correções editoriais podem ocorrer no mesmo registro; alteração substantiva exige histórico de mudança ou registro sucessor conforme a capacidade e convenção do destino. Uma proposta de substituição ainda não invalida a decisão anterior.

Estados devem ser mapeados ao vocabulário nativo do projeto. Uma decisão rejeitada pode valer a pena preservar para evitar reabrir uma opção sem informação nova; uma ideia abandonada sem relevância durável não precisa necessariamente de registro formal. Uma data de revisão vencida solicita reconsideração, não revoga sozinha a decisão. A vigência futura de uma sucessora precisa ser representada sem sugerir que a predecessora já deixou de valer.

## Privacidade e acesso em decisões de negócio

A [implementação da GitLab](https://handbook.gitlab.com/handbook/communication/confidentiality-levels/) mostra que informações de negócio podem exigir acesso limitado mesmo dentro da organização. **Síntese proposta:** o setup define o público adequado, e o agente respeita essa escolha ao gravar o registro, citar anexos e criar referências. Resumos e títulos também podem revelar informação sensível. Não copiar evidência de clientes ou negociações para um destino com acesso mais amplo apenas para completar o registro. Ao mesmo tempo, evitar tornar todo o sistema confidencial quando só uma parte exige restrição.

Isso não recomenda coleta adicional de dados pessoais nem impõe o modelo de transparência da GitLab. Um registro pode apontar para evidência restrita sem reproduzi-la, desde que o público autorizado consiga acessar o que precisa.

## Implicações para este repositório

Inspeção atual: [record-decision](../../skills/record-decision/SKILL.md) atualiza o documento canônico da tarefa e, se ele não existe, cria uma nota local. [write-adr](../../skills/write-adr/SKILL.md) já preserva justificativa, aprovação e substituições, mas fornece um destino Markdown local quando não encontra convenção. [setup-beto-frega-skills](../../skills/setup-beto-frega-skills/SKILL.md) configura um tracker adaptável e pede verificação de integrações; a seção de domínio presume documentos locais. Essas constatações são sobre os arquivos lidos nesta pesquisa, não sobre disponibilidade de conectores.

Recomendação de evolução:

1. **Definir a documentação canônica e seus formatos**: direção estratégica, contrato vigente por domínio/jornada, regras de negócio, evidência e registros históricos. Padronizar atores, direitos, estados, exceções, caminhos negativos, limites, cenários e proveniência. O glossário continua cuidando dos termos; histórico de decisões continua cuidando da justificativa.
2. **Estender o setup** com destino canônico escolhido pelo usuário, contrato de autoridade e representação nativa. Mapear as regras já existentes; perguntar somente pelas lacunas. Tratar explicitamente os fallbacks locais atuais para que não contraponham a escolha do projeto. Configurar onde consultar e manter cada função documental.
3. **Fortalecer record-decision** como entrada comum agent-callable: localizar decisões e contratos vigentes, recuperar aprovação, escolher conteúdo adequado, escrever no destino configurado e verificar o resultado. Declarar o que ainda é rascunho e quais regras atuais são afetadas.
4. **Reutilizar write-adr** para decisões arquiteturais, preservando as regras de conteúdo e ciclo de vida e obedecendo ao destino acordado. Não duplicar essas regras em outras skills.
5. **Criar referências de produto e negócio** com diferenças relevantes: problema e valor ao cliente, direitos e regras de experiência, modelo econômico, políticas, compromissos e evidência. Uma nova skill por acrônimo só entra se houver um fluxo próprio demonstrável.
6. **Integrar consumidores:** modelagem, discovery, specs e tickets precisam consultar a autoridade configurada e apontar para decisões e regras aplicáveis. Um conflito substantivo deve ser levado ao responsável, sem resolver pela data da última edição em qualquer sistema.

Nenhuma dessas mudanças foi feita nesta pesquisa. As constatações e propostas foram registradas somente nesta nota.

## Skills encontradas e conteúdo efetivamente inspecionado

Foram consultados o [catálogo skills.sh](https://skills.sh/), buscas via `npx skills find` e arquivos `SKILL.md` dos repositórios originais. Instalações abaixo são contagens aproximadas exibidas pelo catálogo em 04/10/2026; estrelas foram verificadas via API do GitHub nessa data. Ambos são sinais de adoção, não avaliação de eficácia. Conteúdo e licenças foram lidos sem instalar ou executar os candidatos.

| Candidato e fonte | Adoção observada | Utilidade e limite para esta proposta |
| --- | --- | --- |
| [phuryn — product-strategy](https://github.com/phuryn/pm-skills/blob/main/pm-product-strategy/skills/product-strategy/SKILL.md) | 3 mil instalações; repositório com 26.768 estrelas, MIT. | Canvas de estratégia com visão, segmentos, valor, trade-offs, métricas, capacidades e modelo econômico. Ajuda a produzir direção vigente. Seu formato fixo de nove partes e cadências não devem virar obrigação para toda decisão. Não implementa o ciclo de vida de um registro canônico. |
| [phuryn — opportunity-solution-tree](https://github.com/phuryn/pm-skills/blob/main/pm-product-discovery/skills/opportunity-solution-tree/SKILL.md) | 2,8 mil instalações; mesmo repositório. | Liga resultado, oportunidades, soluções e experimentos. Útil para manter o raciocínio de discovery e as hipóteses. Quantidades mínimas de soluções e rotinas precisam ser adaptadas. Não determina autoridade nem mantém políticas vigentes. A obra original de Torres continua sendo a referência metodológica. |
| [phuryn — prioritize-assumptions](https://github.com/phuryn/pm-skills/blob/main/pm-product-discovery/skills/prioritize-assumptions/SKILL.md) | 2,6 mil instalações; mesmo repositório. | Ajuda a explicitar hipóteses de impacto e risco e desenhar testes. Não adotar automaticamente sua classificação de rejeitar/implementar. A escala de confiança de 1–10 e a fórmula posterior com `1 - Confidence` precisam de interpretação/normalização que o texto não torna inequívoca. Bom repertório, inadequado como regra automática de negócio. |
| [Anthropic — product-brainstorming](https://github.com/anthropics/knowledge-work-plugins/blob/main/product-management/skills/product-brainstorming/SKILL.md) | 5,4 mil instalações; repositório com 26.085 estrelas, Apache-2.0. | Orienta enquadramento do problema, exploração, opções e hipóteses; distingue ideação de decisão. Útil antes da escolha. Não resolve sozinho canonização, autoridade, atualização do produto ou vigência. Quantidades e heurísticas do brainstorming precisam ser proporcionais à questão. |
| [Anthropic — stakeholder-update, seção Decision Documentation](https://github.com/anthropics/knowledge-work-plugins/blob/main/product-management/skills/stakeholder-update/SKILL.md) | Contagem individual de instalações não verificada; mesmo repositório. | Usa o padrão ADR também para decisões estratégicas de produto e escolhas que restringem opções futuras. Preserva contexto, alternativas, consequências, responsáveis e substituição. Reforça a possibilidade de um processo comum; a skill completa tem escopo amplo de comunicação e reuniões. Não importar esse escopo apenas para registrar decisões. |
| [Sky Mavis — decision-records](https://github.com/skymavis/skills/blob/main/skills/decision-records/SKILL.md) | 5,4 mil instalações no catálogo; repositório com 0 estrelas, MIT. | Categorias abertas e manutenção de referências são ideias úteis. O fluxo impõe `docs/decisions/`, IDs globais, scripts e hooks; promoção depende de autorização no turno atual. Conflita com destino arbitrário e autorização persistente da sessão. Não recomendo importar sem redesenhar essas partes. |

**Seleção proposta:** aproveitar ou adaptar estratégia, descoberta e explicitação de hipóteses; manter a governança canônica como responsabilidade própria deste repositório. Não importar um pacote inteiro para obter três funções. Os plugins de knowledge work da Anthropic se apresentam principalmente para Claude Cowork/Claude Code; conteúdo Markdown inspecionado não comprova compatibilidade de todo pacote com o catálogo de plugins do Codex.

Comandos de descoberta/instalação dos candidatos úteis, **não executados para instalar**:

```sh
npx skills add phuryn/pm-skills@product-strategy
npx skills add phuryn/pm-skills@opportunity-solution-tree
npx skills add phuryn/pm-skills@prioritize-assumptions
npx skills add anthropics/knowledge-work-plugins@product-brainstorming
```

Se adotados posteriormente, preservar variantes já existentes, revisar o conteúdo e manter a edição na árvore canônica `skills/`, com referências portáveis. Encontrar uma entrada no catálogo não basta: a busca também exibiu `mattpocock/skills@decision-mapping`, mas esse arquivo não apareceu na árvore atual verificada do repositório; não foi tratado como candidato disponível.

## Plugin Management: opções de integração, sem escolher o destino

Consultas ao catálogo instalado de Plugin Management em 04/10/2026 usaram termos como `Notion Confluence`, `product management` e `decision records`. Os resultados descritos aqui são evidência dessa consulta, não documentação pública de APIs nem testes autenticados. O catálogo retornou:

- **Notion, Atlassian e Coda:** opções para bases de conhecimento, páginas e documentos; Atlassian descreve Confluence e Jira. Todos apareceram disponíveis e não instalados.
- **Linear:** disponível e não instalado; orientado a trabalho, projetos e planejamento. A presença de um tracker não o torna automaticamente a fonte das regras de produto.
- **PostHog:** apareceu instalado; útil como fonte de métricas e experimentos. Autenticação e operações particulares não foram testadas nesta pesquisa.
- **Granola:** disponível e não instalado; pode fornecer discussões e evidência de reuniões. Uma transcrição não estabelece por si só que uma decisão foi aceita.

Nessas consultas não apareceu um plugin específico que resolvesse todo o sistema de governança canônica proposto. A busca é limitada e não prova inexistência. Nenhuma instalação, conexão ou sugestão de provedor foi disparada.

**Conclusão operacional:** escolher o destino no setup; depois descobrir e verificar a integração pertinente. Plugins dão acesso ao armazenamento ou à evidência; as skills definem conteúdo, semântica, autoridade, manutenção e verificação. A existência de um plugin no catálogo não comprova que leitura, busca, escrita ou histórico estejam disponíveis para o projeto.

## Riscos de exagerar a estrutura

- **Multiplicação de siglas:** obrigar uma escolha entre PDR/BDR/ADR pode produzir registros duplicados para uma decisão atravessando áreas. Classificar primeiro; separar quando responsabilidade e significado exigirem.
- **Histórico sem regra atual:** uma lista de decisões não ajuda quem precisa agir se vigência, substituição e alcance estiverem ocultos. Uma vista atual e vínculos explícitos resolvem melhor que um novo tipo de documento.
- **Regra atual sem justificativa:** editar uma política apagando o raciocínio dificulta reconsideração e cria leitura retrospectiva falsa. Preservar o histórico relevante.
- **Burocracia para escolhas reversíveis:** adaptar profundidade da justificativa e participantes à importância da escolha, sem deixar implícitas as regras que orientarão agentes.
- **Confundir aceite com validação:** uma decisão pode estar aceita e sua hipótese continuar incerta; um experimento pode estar concluído sem apoiar a política permanente.
- **Dois sistemas canônicos:** copiar regras para docs, tracker e base externa gera divergência. Manter autoridade por informação e usar referências ou projeções identificadas.
- **Template rígido:** campos vazios, métricas inventadas e alternativas fictícias deixam o documento mais completo visualmente e menos fiel à decisão.
- **Dependência de conector:** um desenho que exige campos relacionais, histórico ou transações que o destino não oferece é uma promessa impossível. Definir conteúdo primeiro e verificar representação e operações depois.

O primeiro passo concreto é definir **a documentação canônica de produto/negócio e seus formatos padronizados**, seguido do setup de autoridade e destino e do fluxo agent-callable que registra decisões e mantém os contratos afetados. A criação de famílias novas de skills deve decorrer de diferenças reais de conteúdo e manutenção.
