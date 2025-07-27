from agents import Agent, InputGuardrail, GuardrailFunctionOutput, Runner
from pydantic import BaseModel
import asyncio
import json
import os

# 【一括利用のモデル指定変数】
MODEL_NAME = "gpt-4.1-mini"

# 言語指定
response_language = os.getenv("RESPONSE_LANG", "Japanese")  # 「English」 も可能

# Math Agent
math_tutor_agent = Agent(
    name="Math Tutor",
    handoff_description="数学の質問に特化したAgent",
    instructions=f""
        f"あなたは数学の問題を助けます。"
        f"言語は{response_language}で答えてください。"
        "詳細な説明を行い、反転の例も含めてください。",
    model=MODEL_NAME,
)

# History Agent
history_tutor_agent = Agent(
    name="History Tutor",
    handoff_description="歴史の質問に特化したAgent",
    instructions=f""
        f"あなたは歴史に関する質問を助けます。"
        f"言語は{response_language}で答えてください。"
        "重要な出来事や背景を明確に説明してください。",
    model=MODEL_NAME,
)

# Guardrail Output Type
class HomeworkOutput(BaseModel):
    is_homework: bool
    reasoning: str

# Guardrail Agent
guardrail_agent = Agent(
    name="Guardrail check",
    instructions="ユーザーが宿題について質問しているか確認してください。",
    output_type=HomeworkOutput,
    model=MODEL_NAME,
)

# Guardrail Function
async def homework_guardrail(ctx, agent, input_data):
    result = await Runner.run(guardrail_agent, input_data, context=ctx.context)
    final_output = result.final_output_as(HomeworkOutput)
    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=not final_output.is_homework,
    )

# Triage Agent
triage_agent = Agent(
    name="Triage Agent",
    instructions="ユーザーの質問が宿題に関連するものかを判断し、適切なAgentを選択してください。",
    handoffs=[history_tutor_agent, math_tutor_agent],
    input_guardrails=[InputGuardrail(guardrail_function=homework_guardrail)],
    model=MODEL_NAME,
)

# 心地よく情報を告げる関数

def friendly_guardrail_message():
    if response_language.lower() == "japanese":
        return "ごめんなさい、この質問は宿題として判断されませんでした。もっと学習に関連する質問をしてみましょう。"
    else:
        return "Sorry, your question was not recognized as homework-related. Please try asking something more academic."

# メイン
async def main():
    print("\n教えてほしい質問を入力してください (「exit」で終了)\n")
    while True:
        user_input = input("Question: ")
        if user_input.strip().lower() == "exit":
            print("終了します。")
            break
        try:
            result = await Runner.run(triage_agent, user_input)
            print("Answer:", result.final_output)
        except Exception as e:
            if "Guardrail InputGuardrail triggered tripwire" in str(e):
                print("Answer:", friendly_guardrail_message())
            else:
                print("Error:", e)

# Run
if __name__ == "__main__":
    asyncio.run(main())
