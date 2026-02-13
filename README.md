# Descrição
Projeto pessoal de plataforma de viagens web que envolve funções como:<br>
• Criar cadastro<br>
• Acessar o cadastro<br>
• Cancelar cadastro<br>
• Alterar informações de cadastro<br>
• Criar reserva<br>
• Listar reservas<br>
• Cancelar reservas<br>
• Listar possíveis destinos

# Tecnologias Utilizadas:
• Python<br>
• MySQL<br>
• Flask(previsto para implementação futura)

## Bibliotecas Utilizadas(Até o momento)

### Bibliotecas Python:
• os(Para variáveis de ambiente - Complementar dotenv)<br>
• datetime(Conversão para objeto data e verificação de datas válidas.)<br>
• re(Validação de formato de email.)<br>
• uuid(Geração de ID aleatório para blacklist de tokens.)

### Bibliotecas Externas
• mysql.connector(Integrar o Python ao banco MySQL)<br>
• dotenv(Ocultar dados sensíveis)<br>
• bcrypt(Hasheamento de senhas e validação para login)<br>
• flask(Para requests e reponses em json, blueprint de rotas.)<br>
• flask-jwt-extended(Para autenticação com JWT e configuração do manager JWT.)<br>
• flask_limiter(Rate limit de requisições das rotas)

# Estrutura do Projeto
Dentro da pasta central app, há a pasta database onde pode se encontrar o script sql para o CRUD de usuários e a criação de tabelas destinations(para destinos) e reservations(para reservas).
A pasta api contém arquivos para ligar o server, definir rotas e configurar JWT.
Interfaces é para fins de teste da ligação com database usando chatbot.py para execução dos testes.
Também há uma pasta de services para aplicar as funções voltadas aos usuários e serviços como um todo.
Além disso possui arquivos utilitários para as necessidades da aplicação.

# Objetivo do Projeto
O objetivo é consolidar na prática conhecimentos de programação e banco de dados por meio do desenvolvimento de um sistema próximo
de uma situação real e desafiadora para meu começo. A aplicação ajuda a entender e executar fundamentos de SQL como CRUD básico, integração MySQL - Python.
Além disso, o projeto serve como base de evolução para atribuição de API utilizando Flask, possibilitando a criação de uma interface Web e 
aprofundando na comunicação entre camadas e manipulação de dados em um contexto mais próximo ao ambiente profissional.
Trata-se de um projeto visando o desenvolvimento pessoal e a possibilidade de dar mais um passo a frente de conseguir
consolidar a minha formação como desenvolvedor.

# Próximos passos
• Novos testes no postman.<br>
• Testes automatizados.<br>
• Melhorar documentação.<br>
• Posteriormente, foco em desenvolvimento frontend.
