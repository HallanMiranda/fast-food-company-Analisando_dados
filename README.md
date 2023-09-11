# KILL-YOUR-HANGRE
# 1. Contexto do Problema de Negócio
Parabéns! Você acaba de ser contratado como Cientista de Dados da empresa Kill my Hunger, e a sua principal tarefa nesse momento é ajudar o CEO Kleiton Guerra a identificar pontos chaves da empresa, respondendo às perguntas que ele fizer utilizando dados! 
A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core Business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da KKill my Hunger, que disponibiliza informações como endereço, tipo de culinária a ser servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações. 


# 2. O Desafio
O CEO Guerra também foi recém contratado e precisa entender melhor o negócio para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a Empresa, e para isso, ele precisa que seja feita uma análise nos dados da empresa e que sejam gerados dashboard para a visualisacoes da métricas e  a partir dessas análises feitas  para responder às seguintes perguntas: 



# 2.1 Visão Geral
1. Quantos restaurantes únicos estão registrados?
2. Quantos países únicos estão registrados?
3. Quantas cidades únicas estão registradas?
4. Qual o total de avaliações feitas?
5. Qual o total de tipos de culinária registrados?
6. Uma visão geral da distribuição dos restaurantes e suas principais métricas.

# 2.2 Visão Pais
1. Qual a quantidade de restaurantes por pais?
2. Qual a quantidade de cidades avaliadas por pais?
3. Quantidade de Avaliações feitas por pais?
4. Qual a média de preço por um prato para duas pessoas
5. Quais são os países que possuem as melhores médias de avaliações
6. Quais são os países que possuem os piores médias de avaliações

# 2.3 Visão Cidades
1. Quais são as cidades que mais possuem restaurantes?
2. Quais são as cidades que tem sua avaliação média acima de 4?
3. Quais são as cidades que tem sua avaliação média menor que 2.?
4. Quais são as cidades que tem a maior quantidade de culinárias?

# 2.4 Visão Culinária
1. Quais são os melhores restaurantes dos principais tipos de culinárias?
2. Quais são os melhores restaurantes?
3. Quais são os melhores tipos de culinárias?
4. Quais são os piores tipos de culinárias?

# 3. Premissas assumidas para a análise
1. Desconsiderado notas iguais a zero
2. Desconsiderado valor médio por prato para duas pessoas iguais a zero
3. Esta sendo considerado que todos os clientes votaram para o calculo de receitas.
4. O painel estratégico foi desenvolvido utilizando as métricas que refletem as 4 principais visões do modelo de negócio da empresa:



# 4. Os Dados 
O conjunto de dados que representam o contexto está disponível na plataforma do Kaggle. O link para acesso aos dados : 
https://www.kaggle.com/datasets/akashram/zomato-restaurants-autoupdated-datase t?resource=download&select=zomato.csv 

# 5. O Ferramental da Solução 
* Vscode Jupyter,  para prototipar e  auxiliar no desenvolvimento da solução.
* Streamlit para possibilitar a criação do dashboard. 

# 6. O produto Final do Projeto
Painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet.
O painel pode ser acessado através desse link: https://hallanmiranda-kill-your-hangre-home-n2nbjy.streamlit.app

# 7. Conclusões
O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO.
Da visão Geral podemos ver que o principal mercado da Empresa está localizado nos Estados Unidos e Índia.

# 8. Próximo Passos
1. Calcular a receita gerada por cada Pais
2. Criar novos filtros para melhor entender o Negocio
3. Validar algumas Hipóteses 

