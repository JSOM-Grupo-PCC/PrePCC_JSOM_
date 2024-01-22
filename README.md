<div align="center">
    <img src="https://github.com/JSOM-Grupo-PCC/PrePCC_JSOM_/assets/115905335/131227b4-7103-497e-b8a6-8aa40d70a8d9" alt="Logo JSOM">
</div>
<hr>
<h1 align="center">Projeto de Conclusão de Curso (PCC) - JSOM<h1>
<h3 align="center">Sistema de Gerenciamento de Academia</h3>
<br> 

## Requisitos e Andamento
| Requisito                                                            | Notas de Andamento                                                         | Status           |
| --------------------------------------------------------------------- | -------------------------------------------------------------------------- | ---------------- |
| **1. O sistema dever permitir que o administrador cadastre os novos alunos da academia**             | O sistema permite o cadastro de novos alunos, mas não é o admin que cadastra novos alunos | :large_blue_circle: Em Andamento |
| **2. O sistema deve permitir o login de alunos e do administrador**                                  | O sistema já permite o login de ambos os tipos de usuários | :green_circle: Concluído |
| **3. O sistema deve conceder ao aluno a possibilidade de visualizar e gerenciar o perfil**           | O sistema atualmente permite que somente o admin possa visualizar e gerenciar seu perfil | :yellow_circle: Feito em parte |
| **4. O sistema deve permitir que o administrador gerencie os treinos de cada aluno**                 | O sistema atualmente só está permitindo o admin adicionar, editar, excluir e visualizar os detalhes dos treinos dos alunos | :green_circle: Concluído |
| **5. O sistema deve permitir que o aluno acesse os seus treinos diários**                            | O sistema já permite que o aluno acesse seus treinos por categoria | :green_circle: Concluído |
| **6. O sistema deve possibilitar o administrador personalizar as informações do perfil dos alunos**  | O sistema atualmente só permite que o admin visualize os dados do perfil de cada aluno | :yellow_circle: Feito em parte |

Legendas:  
:green_circle: Concluído  
:yellow_circle: Feito em parte <br>
:large_blue_circle: Em Andamento <br>
:white_circle: Nada Feito 

## Diagrama Caso de Uso
![Caso de Uso](https://github.com/JSOM-Grupo-PCC/PrePCC_JSOM_/assets/115905335/50206489-0ab5-4f2a-b6a5-8d9334d95e3d)

## Diagrama de classe
![Classe](https://github.com/JSOM-Grupo-PCC/PrePCC_JSOM_/assets/115905335/488711c6-453b-42c3-803d-b81362bcd171)

## Diagrama Entidade de Relacionamentos 
![Entidade de Relacionamentos](https://github.com/JSOM-Grupo-PCC/PrePCC_JSOM_/assets/115905335/48cc20b4-b8c1-4b31-b2cd-79c7d5dd93f1)

## Configuração do Ambiente

1. **Pré-requisitos:**
   - Python 3.x
   - Django
   - Outras dependências (verifique o arquivo `requirements.txt`)

2. **Configuração do Ambiente Virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: .\venv\Scripts\activate

3. **Instalação das Dependências:**
    ````bash
   pip install -r requirements.txt
   
4. **Configuração do Banco de Dados:**
    ````bash
   python manage.py makemigrations
   python manage.py migrate
5. **Execução do Servidor de Desenvolvimento:**
    ````bash
   python manage.py runserver

