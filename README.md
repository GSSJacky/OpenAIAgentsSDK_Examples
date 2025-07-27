Here is a professional `README.md` you can include in your project:

---

````markdown
# 🧠 Homework Assistant with OpenAI Agents SDK

This project demonstrates how to build an intelligent homework assistant using the [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/). It automatically routes user questions to either a math or history expert agent and applies a guardrail to ensure the question is related to homework.

---

## 🚀 Features

- ✏️ Math Tutor Agent – provides step-by-step help on math problems
- 📚 History Tutor Agent – explains historical events and background clearly
- 🛡️ Guardrail Agent – filters out questions that are not related to homework
- 🌐 Supports multi-language output (e.g., Japanese or English)
- 🔁 Interactive command-line interface

---

## 📦 Setup Instructions

### 1. Clone or create the project directory

```bash
mkdir openaiagent_project
cd openaiagent_project
````

### 2. Create and activate a Python virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install the required package

```bash
pip install openai-agents
```

### 4. Set your OpenAI API key

```bash
export OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  # For Mac/Linux
# On Windows:
# set OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 5. Run the application

```bash
python HomeWorkAssistant.py
```

---

## 🧠 How It Works

The app defines four main components using the OpenAI Agents SDK:

### 1. `Math Tutor Agent`

Handles mathematical questions. Provides logical reasoning and worked examples.

### 2. `History Tutor Agent`

Handles history questions. Gives clear explanations of key events and context.

### 3. `Guardrail Agent`

Checks whether the user's question is homework-related. If not, it prevents agent handoff.

### 4. `Triage Agent`

Routes the question to the appropriate agent (`Math` or `History`) only if the guardrail passes.

---

## 🗣️ Language Support

You can change the response language by editing the following line in `HomeWorkAssistant.py`:

```python
response_language = os.getenv("RESPONSE_LANG", "Japanese")  # 「English」 も可能
```

---

## 💬 Sample Usage

```text
Question: Who was the first president of the United States?
Answer: ジョージ・ワシントンはアメリカ合衆国の初代大統領です...

Question: What is 320 + 45?
Answer: 320に45を足すと365になります...

Question: How to spell "test"?
Answer: ごめんなさい、この質問は宿題として判断されませんでした。もっと学習に関連する質問をしてみましょう。
```

To exit the assistant:

```text
Question: exit
終了します。
```

---

以下は、あなたのリクエストに基づいて更新された `README.md` の **Usage セクションの追加例** です。Instana（via Traceloop SDK）へトレース送信する設定を含みます。

---

### 🧪 Advanced Usage: Exporting Traces to Instana via Traceloop

This project supports exporting agent trace data to Instana for full observability using [Traceloop SDK](https://github.com/traceloop/openllmetry).

#### ✅ Step-by-step

```bash
pip install traceloop-sdk
```

Then, set the required environment variables to enable Traceloop → Instana OTLP trace export:

```bash
export TRACELOOP_BASE_URL="https://otlp-XXXX-saas.instana.io:443"
export TRACELOOP_HEADERS="x-instana-key=XXXXXXXXXXXXXXX"
export OTEL_EXPORTER_OTLP_INSECURE=false
```

#### ▶️ Run with Tracing Enabled

```bash
python HomeWorkAssistant_Traceloop.py
```

Upon startup, you should see confirmation like:

```
Traceloop exporting traces to https://otlp-XXXX-saas.instana.io:443, authenticating with custom headers
```

#### 💬 Example Interaction

```text
教えてほしい質問を入力してください (「exit」で終了)

Question: ゆうかさんのクラスの生徒の人数は２５人です。そのうち自転車で通学している生徒の人数はx人です。残りの生徒の人数をy人とするとき，xとyの関係を式に表しなさい。
Answer: ゆうかさんのクラスの生徒は全部で25人です。その中で、自転車で通学している生徒がx人、残りの生徒がy人とします。

自転車で通学している生徒と残りの生徒を合わせると、クラス全体の人数になります。つまり、

\[ x + y = 25 \]

これが、xとyの関係を表す式です。

（以下略）

Question: exit
終了します。
```

---

## 📄 License
This project is provided for educational and prototyping purposes. No license is enforced.
Homework idea comes from the below note:
https://note.com/npaka/n/n4afc430b7be1

