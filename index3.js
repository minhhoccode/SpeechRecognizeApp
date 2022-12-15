const SpeechRecognition =
  window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();
recognition.lang = "en-US";
const server = "http://127.0.0.1:5000/api/";
function ChangeLanguage() {
  if (recognition.lang == "vi-VN") {
    recognition.lang = "en-US";
    document.getElementById("progress-section").innerHTML =
      "<p>Your current language is English</p>";
  } else {
    recognition.lang = "vi-VN";
    document.getElementById("progress-section").innerHTML =
      "<p>Ngôn ngữ hiện tại của bạn là tiếng Việt</p>";
  }
}

function Speak() {
  const synth = window.speechSynthesis;
  //   set language to vn
  const text = document.querySelector(".terminal_input").value;
  var utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = recognition.lang;
  synth.speak(utterance);
}

function Reg() {
  axios = window.axios;
  recognition.start();
  var element = document.getElementById("micro");
  element.classList.remove("cl-btn");
  element.classList.toggle("recording");
  recognition.onresult = (e) => {
    const current = e.resultIndex;
    const transcript = e.results[current][0].transcript;
    document.querySelector(".terminal_input").value = transcript + "\nroot@localhost:~$";
    send2server(transcript);
    var element = document.getElementById("micro");
    element.classList.remove("recording");
    element.classList.toggle("cl-btn");
  };
}
function send2server(text) {
  axios
    .post(server, {
      text: text,
      language: recognition.lang,
    })
    .then((res) => {
      console.log(res);
      document.querySelector(".terminal_input").value += ">" + res.data + "\nroot@localhost:~$";
    })
    .catch((err) => {
      console.log(err);
    });
}
function Micro() {
  element = document.getElementById("micro");
  if (element.classList.contains("recording")) {
    Stop();
  } else {
    Reg();
  }
}
function Stop() {
  recognition.stop();
}
function onTestChange() {
  var key = window.event.keyCode;

  if (key === 13) {
    document.getElementById("terminal_input").value =
      document.getElementById("terminal_input").value + "";
      console.log(document.getElementById("terminal_input").value);
    var lastLine = getLastline();
    send2server(lastLine);
    return false;
  } else {
    return true;
  }
function getLastline(){
  var text = document.getElementById("terminal_input").value;
  var lines = text.split("\n");
  let i = 1;
  var lastLine = lines[lines.length - i];
  // if last line is empty, do nothing
  while (lastLine == "") {
    i++;
    lastLine = lines[lines.length - i];
  }
  return lastLine;
}
}
