
function setDogImage () {
  axios.get(
    'get_dog_pic'
  )
    .then((res) => {
      let resData = res.data;
      document.getElementById('dog_image').src = resData['img_url'];
    })
    .catch((error) => {
      console.log(error.response);
    })
}

function setClockTime () {
  const timeNow = new Date();
  let month = timeNow.getMonth() + 1;
  let date = timeNow.getDate();
  let hour = timeNow.getHours();
  let minute = timeNow.getMinutes();
  let amPM = ' am';
  if (hour >= 12) { amPM = ' pm';}
  if (hour > 12) {hour = hour - 12;}
  if (hour === 0) { hour = 12;}
  if (minute < 10) {minute = '0' + minute;}
  let timeString = hour + ':' + minute + amPM + ' on ' + month + '/' + date;
  document.getElementById('clock_time').innerHTML = timeString;
}

function setWeather () {
    axios.get(
    'get_weather'
  )
    .then((res) => {
      let resData = res.data;
      document.getElementById('current_temp').innerHTML = resData['temperature']['temp'];
      document.getElementById('min_temp').innerHTML = resData['temperature']['temp_min'];
      document.getElementById('max_temp').innerHTML = resData['temperature']['temp_max'];
      document.getElementById('detailed_status').innerHTML = resData['detailed_status'];
      document.getElementById('sunset').innerHTML = resData['sunset'];
      document.getElementById('wind').innerHTML = resData['wind'] + ' m/s';
    })
    .catch((error) => {
      console.log(error.response.data.msg);
    })
}


function setEvents () {
    axios.get(
    'get_historic_events'
  )
    .then((res) => {
      const resData = res.data;
      document.getElementById('event1').innerHTML = resData['events'][0];
      document.getElementById('event2').innerHTML = resData['events'][1];
      document.getElementById('event3').innerHTML = resData['events'][2];
    })
    .catch((error) => {
      const errorMessage = error.response.data;
      console.log(errorMessage);
    })
}

async function init() {
  await Promise.all([
    setClockTime(),
    setDogImage(),
    setWeather(),
    setEvents(),
  ]);
  setInterval(setClockTime, 1000 * 60);
  setInterval(setWeather, 1000 * 60 * 30);
  setInterval(setEvents, 1000 * 60 * 24);
}

