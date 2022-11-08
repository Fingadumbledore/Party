window.onload = function() {
  const username = document.getElementById('userNameEntry').innerHTML;
  const ws = new WebSocket('ws://localhost:5000')
  ws.addEventListener('open', (e) => {
    ws.send(JSON.stringify({
      'user': 'test'
    }))
  })

  function join_chat() {
    ws.send(JSON.stringify({
      'msg_type': 'user_join',
      'username': username
    }))
  } 
}
