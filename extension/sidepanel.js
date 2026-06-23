const input = document.getElementById("input");
const output = document.getElementById("output");

async function generate(tone) {

    const response = await fetch(
        "http://127.0.0.1:8000/grammar_fix",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text: input.value,
                tone: tone
            })
        }
    );

    const data = await response.json();

    output.value = data.result;
}

document
    .getElementById("formal")
    .addEventListener(
        "click",
        () => generate("formal")
    );

document
    .getElementById("casual")
    .addEventListener(
        "click",
        () => generate("casual")
    );

document
    .getElementById("copy")
    .addEventListener(
        "click",
        () => {
            navigator.clipboard.writeText(
                output.value
            );
        }
    );