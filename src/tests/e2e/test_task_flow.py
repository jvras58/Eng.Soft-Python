def test_fluxo_completo_task(client):
    """Testa o fluxo completo de uma tarefa"""
    criar_response = client.post(
        "task/tasks/",
        json={
            "description": "Tarefa E2E",
            "audit_user_ip": "127.0.0.1",
            "audit_user_login": "test_user"
        }
    )
    assert criar_response.status_code == 200
    task_id = criar_response.json()["id"]
    
    atualizar_response = client.put(
        f"/task/tasks/{task_id}",
    )
    
    assert atualizar_response.status_code == 200
    assert atualizar_response.json()["status"] == "Concluída"
