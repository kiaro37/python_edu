import requests

def test_get_example():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")   #отправляет get запрос
    assert response.status_code == 200                                        #проверяет статус код
    data = response.json()                                                    #преобразует json ответ в python словарь
    assert data["id"] == 1                                                    #проверяет ожидаемое значение
