async function loadCountries() {
   const res = await fetch("/api/countries");
  const countries = await res.json();

  const select = document.getElementById("countrySelect");
  countries.sort((a, b) => a.name.localeCompare(b.name)).forEach(country => {
    const option = document.createElement("option");
    option.value = country.name;
    option.textContent = country.name;
    select.appendChild(option);
  });
}

async function loadStations() {
  const country = document.getElementById("countrySelect").value;
   const res = await fetch(`/api/stations?country=${encodeURIComponent(country)}`);
  const stations = await res.json();
  console.log(stations);

  const list = document.getElementById("stationsList");
  list.innerHTML = "";

  stations.slice(0,50).forEach(station => {
    const btn = document.createElement("button");
    btn.textContent = station.name;
    btn.onclick = () => playStation(station.url_resolved);
    list.appendChild(btn);
  });
}

function playStation(url) {
  const audio = document.getElementById("player");
  audio.src = url;
  audio.play();
}

loadCountries();
