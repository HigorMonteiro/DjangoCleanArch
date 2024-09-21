import os
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Cria um novo app com a estrutura de Clean Architecture'

    def add_arguments(self, parser):
        parser.add_argument('app_name', type=str, help='Nome do novo app a ser criado')

    def handle(self, *args, **kwargs):
        app_name = kwargs['app_name']
        base_dir = os.path.join('apps', app_name)
        
        directories = [
            os.path.join(base_dir, 'controller'),
            os.path.join(base_dir, 'application'),
            os.path.join(base_dir, 'domain'),
            os.path.join(base_dir, 'infrastructure'),
            os.path.join(base_dir, 'migrations'),
        ]

        # Verifica se o app já existe
        if os.path.exists(base_dir):
            raise CommandError(f"O app '{app_name}' já existe!")

        # Cria as pastas necessárias
        for directory in directories:
            os.makedirs(directory)

        # Cria arquivos __init__.py em cada diretório
        for directory in directories:
            with open(os.path.join(directory, '__init__.py'), 'w') as f:
                f.write(f'# {directory.split("/")[-1]} module\n')

        # Criando o arquivo models.py dentro de 'domain'
        with open(os.path.join(base_dir, 'domain', 'models.py'), 'w') as f:
            f.write(f'# {app_name} models\n')

        # Criando o arquivo services.py dentro de 'application'
        with open(os.path.join(base_dir, 'application', 'services.py'), 'w') as f:
            f.write(f'# {app_name} services\n')

        # Criando o arquivo user_controller.py dentro de 'controller'
        with open(os.path.join(base_dir, 'controller', f'controller.py'), 'w') as f:
            f.write(f'# {app_name} controller\n')

        # Criando o arquivo repositories.py dentro de 'infrastructure'
        with open(os.path.join(base_dir, 'infrastructure', 'repositories.py'), 'w') as f:
            f.write(f'# {app_name} repositories\n')

        # Finalizando com uma mensagem de sucesso
        self.stdout.write(self.style.SUCCESS(f'Sucesso: O app "{app_name}" foi criado com a estrutura Clean Architecture!'))
