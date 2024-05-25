import gradio as gr
from fastapi import FastAPI
import json

# Generate Markdown history from JSON history
def process_json_history(json_file):
    with open(json_file, "r") as f:
        json_history = json.load(f)
    markdown_history = ""
    for episode in json_history.values():
        markdown_history += f"## Episode {episode['episodeIdx']}\n"
        for history in episode['history']['history']:
            markdown_history += f"### Action: {history['action']}\n"
            markdown_history += f"#### Freelook: {history['freelook']}\n"
            markdown_history += f"#### Inventory: {history['inventory']}\n"
            markdown_history += f"#### Is Completed: {history['isCompleted']}\n"
            markdown_history += f"#### Observation: {history['observation']}\n"
            markdown_history += f"#### Score: {history['score']}\n\n"
    return gr.update(value=markdown_history)

# Create Gradio blocks interface
with gr.Blocks() as demo:
    gr.Markdown("# ScienceWorld Explorer")

    with gr.Row():
        with gr.Column():
            json_file = gr.File(label="History JSON", file_types=["json"], type="filepath")
            submit_button = gr.Button("Submit")

        with gr.Column():
            history_output = gr.Markdown(label="History Markdown", value="")

    submit_button.click(process_json_history, json_file, history_output)

# Create FastAPI app
app = FastAPI()

# Mount Gradio app
app = gr.mount_gradio_app(app, demo, path="/")
