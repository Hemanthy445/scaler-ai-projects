import gradio as gr
from summarizer import summarize

gr.Interface(
    fn=summarize,
    inputs=gr.Textbox(label="Website URL", placeholder="e.g. https://example.com"),
    outputs=gr.Markdown(label="Summary"),
    title="🔎 AI Website Summarizer",
    description="Enter any website URL and get an AI-generated summary.",
).launch(share=True)