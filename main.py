#!/usr/bin/env python
# File: main.py
import sys
import json
import argparse
import logging
from config_loader import load_config
from refiner import refine_prompt

# Global runtime context
CURRENT_CONTEXT = {}

def setup_logging(config):
    logging_enabled = config.get("logging", {}).get("enabled", False)
    if logging_enabled:
        log_file = config.get("logging", {}).get("log_file", "mcp_server.log")
        logging.basicConfig(filename=log_file, level=logging.INFO,
                            format="%(asctime)s - %(levelname)s - %(message)s")
    else:
        logging.getLogger().addHandler(logging.NullHandler())

def handle_jsonrpc_request(request, config):
    global CURRENT_CONTEXT

    if request.get("jsonrpc") != "2.0":
        return {
            "jsonrpc": "2.0",
            "id": request.get("id"),
            "error": {"code": -32600, "message": "Invalid JSON-RPC version."}
        }

    method = request.get("method")
    params = request.get("params", {})
    request_id = request.get("id")

    if method == "refinePrompt":
        prompt = params.get("prompt", "")
        if not prompt:
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "error": {"code": -32602, "message": "Missing 'prompt' parameter."}
            }
        # Use context override if provided; otherwise, use the current runtime context.
        local_context = params.get("context")
        if local_context is not None:
            # Merge CURRENT_CONTEXT with provided context (provided fields override)
            merged_context = {**CURRENT_CONTEXT, **local_context}
        else:
            merged_context = CURRENT_CONTEXT

        try:
            refined = refine_prompt(prompt, config, merged_context)
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {"refined_prompt": refined}
            }
        except Exception as e:
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "error": {"code": -32000, "message": str(e)}
            }
    elif method == "setContext":
        # Expecting a 'context' parameter containing the new context data.
        new_context = params.get("context")
        if not new_context or not isinstance(new_context, dict):
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "error": {"code": -32602, "message": "Missing or invalid 'context' parameter."}
            }
        # Replace the runtime context with the new one.
        CURRENT_CONTEXT = new_context
        logging.info("Context updated: %s", CURRENT_CONTEXT)
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": {"context": CURRENT_CONTEXT}
        }
    elif method == "getContext":
        # Return the current context.
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": {"context": CURRENT_CONTEXT}
        }
    else:
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "error": {"code": -32601, "message": "Method not found."}
        }

def run_jsonrpc_mode(config):
    for line in sys.stdin:
        if line.strip() == "":
            continue
        try:
            request = json.loads(line)
            logging.info("Received request: %s", request)
            response = handle_jsonrpc_request(request, config)
            print(json.dumps(response))
            sys.stdout.flush()
        except json.JSONDecodeError:
            error_response = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": "Parse error"}
            }
            print(json.dumps(error_response))
            sys.stdout.flush()

def run_interactive_mode(config):
    # In interactive mode, simply prompt for a refinement. Context will be the runtime context.
    prompt = input("Enter your prompt: ").strip()
    if not prompt:
        print("No prompt provided.")
        return
    refined = refine_prompt(prompt, config, CURRENT_CONTEXT)
    print("\n[Refined Prompt]\n")
    print(refined)

def main():
    global CURRENT_CONTEXT
    parser = argparse.ArgumentParser(description="MCP Prompt Engineer")
    parser.add_argument("--mcp", action="store_true", help="Run in MCP JSON-RPC mode")
    args = parser.parse_args()

    config = load_config()
    setup_logging(config)

    # Initialize CURRENT_CONTEXT with the default context from the config.
    CURRENT_CONTEXT = config.get("default_context", {})

    if args.mcp:
        run_jsonrpc_mode(config)
    else:
        run_interactive_mode(config)

if __name__ == "__main__":
    main()
