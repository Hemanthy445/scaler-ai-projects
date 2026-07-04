import gradio as gr
from arena import battle

with gr.Blocks(title="LLM Arena") as app:
    gr.Markdown("# ⚔️ LLM Arena — GPT-OSS 120B vs Llama 3.1 8B")
    gr.Markdown("Ask anything. Two models answer. You vote on who did better.")

    with gr.Row():
        prompt_box = gr.Textbox(
            label="Your Prompt",
            placeholder="e.g. Explain recursion in simple terms",
            lines=3,
        )

    battle_btn = gr.Button("⚔️ Battle!", variant="primary")

    with gr.Row():
        with gr.Column():
            gr.Markdown("### 🤖 GPT-OSS 120B")
            output_a = gr.Markdown()
            vote_a = gr.Button("👍 GPT-OSS wins")

        with gr.Column():
            gr.Markdown("### ⚡ Llama 3.1 8B (Fast)")
            output_b = gr.Markdown()
            vote_b = gr.Button("👍 Llama 3.1 8B wins")

    verdict = gr.Markdown()

    battle_btn.click(
        fn=battle,
        inputs=prompt_box,
        outputs=[output_a, output_b],
    )

    vote_a.click(fn=lambda: "🏆 You voted: **GPT-OSS 120B** wins this round!", outputs=verdict)
    vote_b.click(fn=lambda: "🏆 You voted: **Llama 3.1 8B** wins this round!", outputs=verdict)

app.launch(share='True')