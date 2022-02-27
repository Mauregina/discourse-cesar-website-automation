# Automação de Testes 

## Ferramentas
* Pytest 
* Selenium WebDriver

## Automação 1
Estrutura de automação de testes do site https://www.discourse.org/

### Cenários
#### test_1.py
CT-001 – Imprimir título de todos os tópicos fechados.

1. Acessar a página do Discourse (https://www.discourse.org/).
2. Clicar na opção Demo disponível no menu principal.
3. Fazer scroll até o final da página.
4. Imprimir o título de todos os tópicos fechados (são os que tem um cadeado ao lado esquerdo do título).

#### test_2.py
CT-002 – Imprimit quantidade de itens de cada categoria e dos que não possui categoria.

1. Acessar a página do Discourse (https://www.discourse.org/).
2. Clicar na opção Demo disponível no menu principal.
3. Fazer scroll até o final da página.
4. Imprimir quantidade de itens de cada categoria e dos que não possui categoria 

#### test_3.py
CT-003 – Imprimit título do tópico que contém o maior número de views.

1. Acessar a página do Discourse (https://www.discourse.org/).
2. Clicar na opção Demo disponível no menu principal.
3. Fazer scroll até o final da página.
4. Imprimir título do tópico que contém o maior número de views 

## Automação 2
Estrutura de automação de testes do site https://www.cesar.school/

### Cenários
#### test_1.py
CT-001 – Imprimir título e data de publicação do segundo post da página.

1. Acessar a página do Cesar School (https://www.cesar.school/).
2. Abrir o menu “School”.
3. Clicar a opção “Blog”.
4. Ir para a segunda página da lista de posts.
5. Imprimir título do segundo post.
6. Imprimir data de publicação do segundo post.

#### test_2.py
CT-002 – Imprimir título e autor do terceiro post da página.

1. Acessar a página do Cesar School (https://www.cesar.school/).
2. Abrir o menu “School”.
3. Clicar a opção “Blog”.
4. Ir para a segunda página da lista de posts.
5. Imprimir título do terceiro post.
6. Imprimir autor do terceiro post.

#### test_3.py
CT-003 – Imprimir endereço do cesar school.

1. Acessar a página do Cesar School (https://www.cesar.school/).
2. Abrir o menu “School”.
3. Clicar a opção “Blog”.
4. Ir para a segunda página da lista de posts.
5. Ir até o final da página.
6. Imprimir endereço do Cesar School.

