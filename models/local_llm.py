#!/usr/bin/env python
# File: models/local_llm.py
import requests

def run_model(prompt: str, config: dict, context: dict = None) -> str:
    url = config["model_url"]
    model_name = config["model_name"]
    settings = config.get("default_prompt_settings", {})

    # Merge default context with any provided context (request overrides default)
    default_context = config.get("default_context", {})
    merged_context = {**default_context, **(context or {})}

    # Format merged context as a string for the system prompt
    context_str = ""
    if merged_context:
        context_items = [f"{key}: {value}" for key, value in merged_context.items()]
        context_str = "; ".join(context_items)

    # Build a detailed system prompt that uses the context
    SYSTEM_PROMPT_TEMPLATE = (
        "You are a prompt refinement assistant that takes generic software development requests and turns them into detailed, high-quality, context-aware prompts for a code generation AI.\n"
        "When refining a prompt, use the following technical context if provided: {context_str}.\n"
        "Requirements:\n"
        "- Return only ONE refined prompt.\n"
        "- Do not include any explanations, options, or internal reasoning.\n"
        "- Be concise, yet include critical technical details (e.g., persistence, UI behavior, edge case handling).\n"
        "- Do not make changes outside the scope of the request.\n"
        "Your output will be passed to a code generation model, so clarity, specificity, and relevance are critical. Your output must be ONLY the refined prompt."
    )
    system_prompt = SYSTEM_PROMPT_TEMPLATE.format(context_str=context_str)

    headers = {
        "Content-Type": "application/json"
    }

    body = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": settings.get("temperature", 0.7),
        "max_tokens": settings.get("max_tokens", 1024)
    }

    response = requests.post(url, json=body, headers=headers)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
