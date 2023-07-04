from test import client

def test_api(client):
    endpoints = [("/api", "GET"),
        ("/api/mate", "GET"),
        ("/api/mate/status", "GET"),
        ("/api/mate/trinken", "POST"),
        ("/api/chat/", "GET"),
        ("/api/chat/messages/:count", "GET"),
        ("/api/chat/new_message", "POST"),
        ("/api/music", "GET"),
        ("/api/music/skip", "POST"),
        ("/api/music/queue", "GET"),
        ("/api/music/add_song", "POST")
    ]
    response = client.get('/api')

    for endpoint in endpoints:
        if endpoint[1] == "GET":
            response = client.get(endpoint[0])
        elif endpoint[1] == "POST":
            response = client.post(endpoint[0])
    assert response.status_code == 200
