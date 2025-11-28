

def assert_response_time(response):
    response_time = response.elapsed.total_seconds()
    assert response_time<2 ,f"El tiempo de respuesta fue muy alto: {response_time} segundos"