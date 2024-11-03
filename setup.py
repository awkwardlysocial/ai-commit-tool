from setuptools import setup, find_packages

setup(
    name="ai_commit_tool",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "openai",
        "python-dotenv",
        "colorama",
        "keyring",
    ],
    entry_points={
        "console_scripts": [
            "ai-commit=ai_commit_tool.cli:main",
        ],
    },
    description="A CLI tool that generates AI-based git commit messages.",
    author="awkwardlysocial",
    author_email="shortgrassguy@gmail.com",
    url="https://github.com/awkwardlysocial/ai-commit-tool",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Version Control :: Git",
    ],
    python_requires=">=3.6",
)
