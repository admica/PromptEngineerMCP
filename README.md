# PromptEngineerMCP

PromptEngineerMCP is a Model Context Protocol (MCP) server that refines and enhances user prompts for cloud-based Large Language Models (LLMs). It uses a locally run LLM to add details, instructions, and guardrails—ensuring optimal performance from your cloud LLM.

## Description

"PromptEngineerMCP: Enhances LLM prompts with local refinement, adding details and guidance for optimal cloud-based LLM performance."

## Features

- Takes plain user prompts and transforms them into detailed, well-structured inputs.
- Adds custom instructions, warnings, and context using a local LLM.
- Lightweight server design for easy integration with cloud-based LLMs.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/admica/PromptEngineerMCP.git
   ```
2. Navigate to the project directory:
   ```bash
   cd PromptEngineerMCP
   ```
4. Configure your local LLM (e.g., specify model path or API in `config.json`).

## Usage

1. Start the MCP server:
   ```bash
   python server.py
   ```
2. Send a prompt via API or CLI:
   ```bash
   "Write a story about time travel."
   ```
3. Receive an enhanced prompt, e.g.:
   ```json
   {
     "refined_prompt": "Write a detailed 500-word story about a time-traveling scientist, avoiding clichés like evil corporations, and include a hopeful ending."
   }
   ```

## Contributing

Feel free to submit issues or pull requests!

## License

Copyright 2025 admica

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
