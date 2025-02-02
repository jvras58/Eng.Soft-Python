
from commands.commands import CreateTaskCommand, UpdateTaskStatusCommand
from queries.queries import ListTasksQuery

def main():
    # Criação de tarefas
    cmd1 = CreateTaskCommand("Estudar padrões de projeto", urgent=True)
    task1 = cmd1.execute()

    cmd2 = CreateTaskCommand("Implementar testes unitários")
    task2 = cmd2.execute()

    # Listar tarefas
    tasks = ListTasksQuery().execute()
    print("Tarefas atuais:")
    for t in tasks:
        print(t)

    # Atualizar status de uma tarefa
    update_cmd = UpdateTaskStatusCommand(task_id=task1.id)
    update_cmd.execute()

    # Listar novamente para ver a alteração
    tasks = ListTasksQuery().execute()
    print("Após atualização:")
    for t in tasks:
        print(t)

if __name__ == "__main__":
    main()
