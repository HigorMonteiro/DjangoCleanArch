Camadas típicas de uma arquitetura limpa (Clean Architecture). Isso ajudará a entender as responsabilidades e como cada parte interage com o sistema.

### 1. **Camada de Controller**
   - **Descrição**: Esta camada atua como a interface entre as requisições externas (HTTP, APIs, etc.) e o restante do sistema. O papel principal da camada de controller é receber as solicitações dos usuários (ex: uma requisição HTTP via Django Rest Framework), chamar os serviços necessários e retornar as respostas adequadas. Basicamente, ela coordena a comunicação entre o mundo externo e as regras de negócios da aplicação.
   - **Responsabilidades**:
     - Lidar com requisições e respostas.
     - Delegar o processamento de dados para a camada de aplicação.
     - Retornar erros e respostas em um formato adequado.
   - **Exemplo**:
     ```python
     # apps/accounts/controller/user_controller.py

     from rest_framework.response import Response
     from rest_framework.views import APIView
     from apps.accounts.application.services import UserService

     class UserController(APIView):
         def get(self, request, user_id):
             user_data = UserService.get_user_by_id(user_id)
             return Response(user_data)
     ```

### 2. **Camada de Aplicação (Application)**
   - **Descrição**: A camada de aplicação define os casos de uso do sistema. Ela coordena as interações entre as entidades da camada de domínio e outros serviços. Não contém regras de negócio diretamente, mas organiza o fluxo dos dados. Seu objetivo é ser o “cérebro” da aplicação, definindo o que deve ser feito e em que ordem.
   - **Responsabilidades**:
     - Definir casos de uso.
     - Orquestrar a interação entre a camada de domínio e a infraestrutura.
     - Não deve conhecer detalhes da infraestrutura, como bancos de dados.
   - **Exemplo**:
     ```python
     # apps/accounts/application/services.py

     from apps.accounts.domain.models import CustomUser

     class UserService:
         @staticmethod
         def get_user_by_id(user_id):
             return CustomUser.objects.get(id=user_id)
     ```

### 3. **Camada de Domínio (Domain)**
   - **Descrição**: A camada de domínio é onde estão as regras de negócio e lógica central da aplicação. É o coração do sistema e não depende de frameworks ou tecnologias externas. As entidades nesta camada contêm a lógica que garante que o sistema funciona corretamente e seguem as regras do negócio.
   - **Responsabilidades**:
     - Definir as regras de negócio.
     - Modelar as entidades principais do sistema.
     - Ser independente da infraestrutura (banco de dados, frameworks).
   - **Exemplo**:
     ```python
     # apps/accounts/domain/models.py

     from django.db import models
     from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

     class CustomUser(AbstractBaseUser):
         email = models.EmailField(unique=True)
         first_name = models.CharField(max_length=30)
         last_name = models.CharField(max_length=30)
         is_active = models.BooleanField(default=True)
         is_staff = models.BooleanField(default=False)

         USERNAME_FIELD = 'email'
         REQUIRED_FIELDS = ['first_name', 'last_name']
     ```

### 4. **Camada de Infraestrutura (Infrastructure)**
   - **Descrição**: A camada de infraestrutura trata da comunicação com serviços externos, como banco de dados, APIs externas (como LinkedIn, OpenAI), ou outras ferramentas de suporte. Aqui é onde as dependências tecnológicas são gerenciadas. Apesar de estar relacionada com a persistência de dados e outras integrações, ela deve ser acessada apenas através dos serviços da aplicação.
   - **Responsabilidades**:
     - Gerenciar a comunicação com o banco de dados.
     - Interagir com APIs e serviços externos.
     - Fornecer implementações concretas para as abstrações definidas na camada de domínio.
   - **Exemplo**:
     ```python
     # apps/accounts/infrastructure/repositories.py

     from apps.accounts.domain.models import CustomUser

     class UserRepository:
         @staticmethod
         def save_user(user):
             user.save()

         @staticmethod
         def get_user_by_email(email):
             return CustomUser.objects.filter(email=email).first()
     ```

### Estrutura do Projeto Após a Documentação:

```plaintext
├── apps
│   └── accounts
│       ├── __init__.py
│       ├── controller  # Lida com as requisições HTTP (antiga camada de apresentação)
│       │   └── user_controller.py
│       ├── application  # Coordena os casos de uso
│       │   └── services.py
│       ├── domain  # Contém as entidades e regras de negócio
│       │   └── models.py
│       ├── infrastructure  # Comunicação com o banco de dados e APIs externas
│       │   └── repositories.py
│       └── migrations
├── config
│   ├── settings.py
└── manage.py
```

### Benefícios dessa Estrutura:
- **Separa responsabilidades**: Cada camada tem um papel específico, o que facilita a manutenção e o entendimento do código.
- **Facilita testes**: Como cada camada tem uma responsabilidade clara, você pode testar unidades individuais sem se preocupar com as outras.
- **Flexibilidade**: A infraestrutura (bancos de dados, APIs) pode ser trocada sem modificar as regras de negócio.
- **Evolução**: Novos casos de uso ou mudanças de regras de negócio podem ser implementados diretamente na camada de aplicação ou domínio sem impactar a infraestrutura.
