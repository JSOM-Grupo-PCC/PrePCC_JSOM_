<div align="center">
    <img src="https://github.com/JSOM-Grupo-PCC/PrePCC_JSOM_/assets/115905335/f215246a-a4a2-44cc-826e-ceda69ef84a5" alt="Logo JSOM" width="50%">
</div>
<hr>
<h1 align="center">Projeto de Conclusão de Curso (PCC) - JSOM<h1>
<h3 align="center">Sistema de Gerenciamento de Academia</h3>
<br> 

## Requisitos e Andamento
| Requisito                                                            | Notas de Andamento                                                         | Status           |
| --------------------------------------------------------------------- | -------------------------------------------------------------------------- | ---------------- |
| **1. O sistema dever permitir que o administrador cadastre os novos alunos da academia**             | O sistema permite o cadastro de novos alunos pelo admin | :green_circle: Concluído  |
| **2. O sistema deve permitir o login de alunos e do administrador**                                  | O sistema já permite o login de ambos os tipos de usuários | :green_circle: Concluído |
| **3. O sistema deve permitir a recuperação de senha dos aluno**                                      |  | :white_circle: Nada Feito  |
| **4. O sistema deve permitir que o administrador visualize a senha do aluno**                        |  | :white_circle: Nada Feito  |
| **5. O sistema deve conceder ao aluno a possibilidade de visualizar e gerenciar o perfil**           | O sistema já permite o aluno vizualizar e atualizar dados como peso, altura e data de nascimento | :green_circle: Concluído  |
| **6. O sistema deve permitir que o administrador gerencie os treinos de cada aluno**                 | O sistema já permite o admin adicionar, editar, excluir e visualizar os detalhes dos treinos dos alunos | :green_circle: Concluído |
| **7. O sistema deve permitir que o aluno acesse os seus treinos diários**                            | O sistema já permite que o aluno acesse seus treinos por categoria | :green_circle: Concluído |
| **8. O sistema deve fornecer uma funcionalidade de conclusão dos exercícios agendados aos alunos no respectivo dia**                                                           |  | :yellow_circle: Em Andamento  |
| **9. O sistema deve possibilitar o administrador personalizar as informações do perfil dos alunos**  | O sistema já permite que o admin atualizar todas as informações do Aluno   | :green_circle: Concluído |
| **10. O sistema deve integrar balança inteligente de bioimpedância para o preenchimento automático de dados corporais do aluno**                                               |  | :white_circle: Nada Feito  |
| **11. O sistema deve notificar mensalmente ao aluno a possibilidade de atualização das informações**                                                                           |  | :white_circle: Nada Feito  |
| **12. O sistema deve apresentar de forma clara e acessível às estatísticas detalhadas sobre as métricas corporais e o desempenho semanal de cada aluno na página dashboard**   |  | :white_circle: Nada Feito  |
| **13. O sistema deve possibilitar a transição entre os modos claro e escuro**                                                                                                  | O sistema possibilita a utilização do dark mode | :green_circle: Concluído  | 
| **14. Sistema deve notificar o admin para cadastrar os treinos de novos alunos caso não exista nenhum cadastrado**                                                             |  | :white_circle: Nada Feito  | 
Legendas:  
:green_circle: Concluído  
:large_blue_circle: Feito em parte <br>
:yellow_circle: Em Andamento <br>
:white_circle: Nada Feito 

## Diagrama Caso de Uso
![Caso de Uso](https://github.com/JSOM-Grupo-PCC/PrePCC_JSOM_/assets/115905335/50206489-0ab5-4f2a-b6a5-8d9334d95e3d)

## Diagrama de classe
![Classe](https://github.com/JSOM-Grupo-PCC/PrePCC_JSOM_/assets/115905335/488711c6-453b-42c3-803d-b81362bcd171)

## Diagrama Entidade de Relacionamentos 
![Entidade de Relacionamentos](https://github.com/JSOM-Grupo-PCC/PrePCC_JSOM_/assets/115905335/db2f5622-ccba-4ad3-ae5f-b3a58fa8722c)

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

