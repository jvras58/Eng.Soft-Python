
def test_criar_task_api(client):
    """Testa a criação de tarefa via API"""
    response = client.post(
        "/task/tasks/",
        json={
            "description": "Tarefa via API",
            "audit_user_ip": "127.0.0.1",
            "audit_user_login": "test_user"
        }
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["description"] == "Tarefa via API"
    assert data["status"] == "Pendente"

def test_atualizar_task_api(client, task):
    """Testa a atualização de tarefa via API"""
    response = client.put(
        f"/task/tasks/{task.id}"
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "Concluída"

def test_listar_tasks(client, task):
    """Testa listagem de tarefas"""
    response = client.get("/task/get_all_tasks")
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
