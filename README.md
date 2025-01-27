# AI Voice Assistant

An intelligent voice assistant that uses Ollama for processing queries and provides voice responses. The assistant can evaluate the complexity of queries and use different language models accordingly.

## Features

- Voice input recognition using Google Speech Recognition
- Text-to-speech output using Google TTS
- Automatic task complexity evaluation
- Dynamic model selection based on query complexity
- Supports both English and Turkish languages

## Prerequisites

- Docker installed on your system
- Microphone access
- Speaker access

## Quick Start with Docker

1. Clone the repository:

```bash
git clone https://github.com/altintasutku/jarvis
cd jarvis
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Install Ollama Models:

```bash
ollama pull llama3.2:1b # Pull llama3.2:1b model
ollama pull deepseek-r1:8b # Pull deepseek-r1:8b model
```

4. Run the application:

```bash
python main.py
```

## Configuration

You can configure the following in `main.py`:

- Language selection (English/Turkish)
- AI models for different complexity levels
- Speech recognition settings
- Voice output settings

## Models Used

- Simple queries: llama3.2:1b
- Complex queries: deepseek-r1:8b
- Query evaluation: llama3.2:1b

## Contributing

Feel free to open issues and pull requests for any improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Ollama](https://ollama.ai/) for providing the AI models
- Google Speech Recognition for voice input
- Google Text-to-Speech for voice output
