let lastTone = "formal";

async function generate(tone) {
  lastTone = tone;

  const input = document.getElementById("input").value;

  const res = await fetch("http://127.0.0.1:8000/grammar", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      text: input,
      tone: tone
    })
  });

  const data = await res.json();
  document.getElementById("output").value = data.result;
}

document.getElementById("copy").addEventListener("click", () => {
  const text = document.getElementById("output").value;
  navigator.clipboard.writeText(text);
});