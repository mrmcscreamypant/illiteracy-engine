function request(query,callback) {
  const xhttp = new XMLHttpRequest();
  xhttp.onload = callback
  xhttp.open("GET", "query/"+query, true);
  xhttp.send();
}