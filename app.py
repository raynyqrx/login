from flask import Flask, request, render_template_string
app = Flask(__name__)
HTML = """
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>Login</title>
<style>
body {
    font-family: Arial, sans-serif;
    background: #f5f5f5;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}
.login-box {
    background: white;
    width: 320px;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}
h2 {
    text-align: center;
}
.notice {
    font-size: 13px;
    background: #fff3cd;
    padding: 10px;
    border-radius: 6px;
    margin-bottom: 15px;
}
input {
    width: 100%;
    box-sizing: border-box;
    padding: 12px;
    margin: 8px 0;
    border: 1px solid #ccc;
    border-radius: 5px;
}
button {
    width: 100%;
    padding: 12px;
    margin-top: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}
.result {
    margin-top: 20px;
    padding: 12px;
    background: #f0f0f0;
    border-radius: 5px;
}
</style>
</head>
<body>
<div class="login-box">
<h2>Security </h2>
</div>
<form method="POST">
<input
    name="username"
    placeholder="ユーザー名"
    required
>
<input
    name="demo_code"
    maxlength="20"
    placeholder="パスワード"
    required
>
<button type="submit">
送信
</button>
</form>
{% if submitted %}
<div class="result">
<strong>データを受信しました</strong>
<br><br>
Username：{{ username }}
<br>
Demo Code：{{ demo_code }}
</div>
{% endif %}
</div>
</body>
</html>
"""
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username", "")
        demo_code = request.form.get("demo_code", "")
        print("")
        print("=== データを受信 ===")
        print("Username:", username)
        print("Demo Code:", demo_code)
        print("========================")
        print("")
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
    port=5000
)