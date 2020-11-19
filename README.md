# Bash-News

 Projeto da disciplina de sistemas operacionais (CC6270)
 Centro Universitário FEI - 2º Semestre 2020
- Stela Fernandes de Almeida	22.118.120-9
- Vinicius de Andrade Silva	22.117.050-9
- Vitor Zamignani Maluf	22.118.077-1
- Anderson Simão da Silva	22.118.031-8

## DESCRIÇÃO

Com a correria das nossas rotinas diárias, é preciso gastar um tempinho para pesquisar sobre notícias na internet e muitos acabam por não pesquisarem muito sobre as notícias e ficam "desligados" do que está acontecendo. Assim, com o intuito de automatizar essa tarefa para que seja possível ganhar tempo para outras, desenvolveremos um sistema capaz de pesquisar notícias diárias por você e organizá-las de acordo com sua necessidade ou desejo. 

O sistema conta com uma busca de notícias em um intervalo de datas, podendo ser diárias ou até mesmo de anos. Será possível fazer isso com apenas um comando no terminal do sistema operacional. As notícias serão baixadas para o HD e convertidas para um PDF em qualquer pasta qualquer de interesse.

## REQUISITOS

>* Python 3
>* PIP

## INSTALAÇÃO


```
python3 pip install -r requirements.txt
```

## EXECUÇÃO

Para executar o script basta digitar o seguinte comando:

```
python3 main.py --keyword name --pages n
```
> * --keyword
>    * Após o parâmetro --keyword digite a palavra-chave que você procura
>
> * --pages
>    * Após o parâmetro --pages digite o número de páginas que devem ser buscadas no google. Obs.: Cada página retorna 10 itens de pesquisa.

Após a execução do script as noticias estarão salvas na pasta *news* dentro da pasta do projeto.