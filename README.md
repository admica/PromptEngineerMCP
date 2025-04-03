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

5. Update the config.json to include your URL to reach the local LLM, and your tech stack.

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
     "refined_prompt": "Generate a React 19.1 component with TypeScript 5.4.3 using shadcn/ui
     for a web application built with Vite 5.2.6 that displays a chronological timeline of events
     from a user-provided text input describing a time traveler's journey. The timeline should
     render as a horizontal scrollable list of cards, each card representing an event with a
     title and short description. Implement Zustand 4.5.2 for state management to store the parsed
     events. The component should handle empty input gracefully by displaying a placeholder message.
     Include error handling for invalid text input formats, displaying user-friendly messages.
     Persist the timeline data in PostgreSQL 17.4 using Node.js 21.7.1 and TailwindCSS 4.1.1 for
     styling. The time traveler's journey should be parsed into events based on date/time markers
     within the input text; assume a simple 'YYYY-MM-DD' format. Allow users to filter the timeline
     by year using a dropdown menu, dynamically updating the displayed events."
   }
   ```

## Contributing

Feel free to submit issues or pull requests!

## License

Copyright 2025 admica

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
