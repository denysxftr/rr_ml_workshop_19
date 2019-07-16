def test_api_get_health(client):
    response = client.get("/api/v1/health")

    assert response.json == {"status": "ok"}
