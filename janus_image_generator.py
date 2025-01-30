import os
import PIL.Image
import torch
import numpy as np
from transformers import AutoModelForCausalLM
from janus.models import MultiModalityCausalLM, VLChatProcessor

# Model setup
model_path = "deepseek-ai/Janus-Pro-7B"
vl_chat_processor = VLChatProcessor.from_pretrained(model_path)
tokenizer = vl_chat_processor.tokenizer

vl_gpt = AutoModelForCausalLM.from_pretrained(
    model_path, 
    trust_remote_code=True
).to(torch.bfloat16).cuda().eval()

# Custom prompt for Chapter 1 scene
conversation = [
    {
        "role": "<|User|>",
        "content": "A farmer's patched shirt with migrating constellations at dusk, fireflies glowing above rice fields, Seneca corn prophecy patterns emerging in the fabric, traditional Chinese agricultural scene with mystical elements, detailed star charts transforming into corn kernels, muted earth tones with bright celestial accents",
    },
    {"role": "<|Assistant|>", "content": ""},
]

# Prepare generation prompt
sft_format = vl_chat_processor.apply_sft_template_for_multi_turn_prompts(
    conversations=conversation,
    sft_format=vl_chat_processor.sft_format,
    system_prompt="",
)
prompt = sft_format + vl_chat_processor.image_start_tag

# Generation function (keep the original parameters from janus_images.md)
@torch.inference_mode()
def generate(...):  # Keep original function parameters unchanged
    ...  # Keep original function implementation

# Generate and save images
generate(
    vl_gpt,
    vl_chat_processor,
    prompt,
    temperature=0.7,  # Slightly more creative
    cfg_weight=4.5,   # Balance between fidelity and creativity
    parallel_size=4    # Generate 4 variations
) 