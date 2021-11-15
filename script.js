fetch("https://type.fit/api/quotes")
  .then(function(response) {
    return response.json();
  })
  .then(function(data) {
    data = data[Date.now() % data.length];

    var quote = document.getElementById("quote");

    quote.innerHTML = data.text;
  });

function CurrentTime() {
  let date = new Date();

  let h = date.getHours();
  if (h < 10) {
    h = "0" + h;
  }

  let m = date.getMinutes();
  if (m < 10) {
    m = "0" + m;
  }

  let s = date.getSeconds();
  if (s < 10) {
    s = "0" + s;
  }

  document.getElementById("clock").innerHTML = h + ":" + m + ":" + s;

  let t = setTimeout(function() {CurrentTime()}, 1000); 
}

CurrentTime();
