import os
import openai
import gradio as gr

class ChatGPT:
    def __init__(self):
        # 環境変数からAPIキーを取得してopenaiにセット
        openai.api_type = "azure"
        openai.api_base = os.getenv("OPENAI_API_HOST")
        openai.api_version = os.getenv("OPENAI_API_VERSION")
        openai.api_key = os.getenv("OPENAI_API_KEY")

        self.engine = os.getenv("AZURE_DEPLOYMENT_ID")
        system_prompt = os.getenv("OPENAI_DEFAULT_SYSTEM_PROMPT")

        self.system_prompt_msg = {
            "role": "system",
            "content": system_prompt,
        }

        # 会話履歴用リスト型変数
        self.message_history = []

    def chat(self, user_msg):
        # ユーザの会話を履歴に追加
        self.message_history.append({
            "role": "user",
            "content": user_msg
        })

        # システムプロンプトを設定
        messages = [self.system_prompt_msg]
        messages.extend(self.message_history)

        # ChatGPT APIコール
        res = openai.ChatCompletion.create(
            engine=self.engine,
            messages=messages,
        )

        # AIの回答を履歴に追加
        assistant_msg = res.choices[0].message.content
        self.message_history.append({
            "role": "assistant",
            "content": assistant_msg
        })

        # 全会話履歴をChatbot用タプル・リストに変換して返す
        return [(self.message_history[i]["content"], self.message_history[i+1]["content"]) for i in range(0, len(self.message_history)-1, 2)]

    def clear_history(self):
        self.message_history.clear()

def run_gradio():
    with gr.Blocks() as demo:
        chatbot = gr.Chatbot()
        input_box = gr.Textbox(show_label=False, placeholder="メッセージを入力してね").style(container=False)

        chat_gpt = ChatGPT()
        
        input_box.submit(fn=chat_gpt.chat, inputs=input_box, outputs=chatbot) # メッセージ送信されたら、AIと会話してチャット欄に全会話内容を表示
        input_box.submit(fn=lambda: "", inputs=None, outputs=input_box) # （上記に加えて）入力欄をクリア

        clear = gr.Button("Clear")
        clear.click(fn=chat_gpt.clear_history, inputs=None, outputs=chatbot, queue=False)

    demo.launch()

if __name__ == "__main__":
    run_gradio()
