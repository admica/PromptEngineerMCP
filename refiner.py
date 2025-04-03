#!/usr/bin/env python
# File: refiner.py
from models.local_llm import run_model

def refine_prompt(prompt: str, config: dict, context: dict = None) -> str:
    return run_model(prompt, config, context)
