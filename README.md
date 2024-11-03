# AI Commit Tool

A CLI tool that generates AI-powered git commit messages.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Install via pip](#install-via-pip)
- [Setup](#setup)
  - [OpenAI API Key](#openai-api-key)
    - [First-Time Setup](#first-time-setup)
    - [Alternative Methods](#alternative-methods)
- [Usage](#usage)
  - [Basic Usage](#basic-usage)
  - [Updating the API Key](#updating-the-api-key)
- [Examples](#examples)
  - [Example 1: Accepting the AI-Generated Message](#example-1-accepting-the-ai-generated-message)
  - [Example 2: Entering a Custom Message](#example-2-entering-a-custom-message)
- [Contributing](#contributing)
  - [Guidelines](#guidelines)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

I was tired of always typing commits so why not build a tool that makes it so I dont have to. Also AI is cool right now. Please let me know your feedback! As I continue to learn Python I thought this would be a cool project to put my skills to the test and collaborate with others!

## Features

- **AI-Powered Commit Messages**: Generates commit messages using OpenAI's GPT models based on the diff of your staged changes.
- **Secure API Key Storage**: Stores your OpenAI API key securely using your operating system's keyring.
- **Flexible Configuration**: Supports custom commit messages and optional key updates.
- **Language Support**: Works with multiple programming languages by analyzing code file types.

## How It Works

The tool processes changes in code files by analyzing the `git diff` output, focusing specifically on code additions and deletions. It then uses AI to generate commit messages based on these changes. Non-code-related changes, such as package updates, are ignored to prevent overwhelming the AI API and ensure the focus remains on meaningful code changes.

## Installation

### Prerequisites

- Python 3.6 or higher
- `pip` (Python package installer)
- Git installed and configured

### Install via pip

```bash
pip install ai-commit-tool
```

## Setup

### OpenAI API Key

This tool requires an OpenAI API key to function. 

### Projects using git

This only works on projects that you have initalized with git

#### First-Time Setup

Run the tool:

```bash
ai-commit
```
Enter your OpenAI API key here:

```bash
Enter your OpenAI API key: your-api-key-here
```

Save the API key securely:

- The tool will ask if you want to save the API key securely for future use.
- Your API key will be stored in your operating system's keyring.
- Security: The API key remains on your local machine and is never transmitted or shared.

**Alternative Method**
Environment Variable:

Windows:

1. Search for "Environment Variables" in the Start menu.
2. Click "Edit the system environment variables."
3. Click "Environment Variables."
4. Under "User variables," click "New."
5. Enter OPENAI_API_KEY as the variable name and your API key as the value.
6. Click "OK" to save.

## Update API Key (if needed)

if you need to update API key:

```bash
ai-commit --update-key
```

Follow prompts to enter and save new key.

## Usage

Stage your changes in git:

```bash
git add .
```

Run the AI Commit Tool:

```bash
ai-commit
```

Follow the prompts:

- It will show you a list of changes
- Then generates an commit message based on changes
- You choose to confirm, decline, or edit the commit message

Example output:

```bash
---- GENERATED COMMIT MESSAGE ----
"Refactor: Improved performance of data processing module."

Do you want to commit using this message? (y/n/c):
```

- `y` commits the message
- `n` cancels the commit
- `c` custom commit message

## Contributing

Contributions are welcome! Heres how:

1. Fork the repository on GitHub.

2. Clone your fork locally:

```bash
git clone https://github.com/awkwardlysocial/ai-commit-tool.git
```

3. Create a new branch for your feature or bug fix:

```bash
git checkout -b feature/your-feature-name
```

4. Make your changes and commit them:

```bash
ai-commit
```

 or

```bash
git commit -m "Description of your changes"
```

5. Push to your fork:

```bash
git push origin feature/your-feature-name
```

6. Submit a pull request to the main repository.

## Guidelines

- Follow the existing coding style.
- Include comments where appropriate.
- Update the README.md if your changes affect usage or setup.
- Ensure that your code passes any existing tests.

## License

This project is licensed under the terms of the MIT License.