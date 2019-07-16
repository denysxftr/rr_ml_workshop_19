def test_api_get_prediction(client):
    response = client.get(
        "/api/v1/predict?top=1&url=https://cdn1.medicalnewstoday.com/content/images/articles/322/322868/golden-retriever-puppy.jpg"
    )

    assert response.json == {"predictions": ["golden_retriever"]}
