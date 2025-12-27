# Santa Voice OpenAI - AI Agent Instructions

## Project Overview

A Python script that generates audio of Santa Claus delivering a Christmas message using OpenAI's Text-to-Speech API. The script outputs an MP3 file named `pere-noel.mp3`.

## Architecture & Key Components

### Dependencies

- **OpenAI Python SDK** (`openai`): Required for all API interactions. Installation: `pip install openai`

### Main Flow

1. Initialize OpenAI client (uses `OPENAI_API_KEY` environment variable)
2. Define Santa's message as a French multilingual string
3. Call `client.audio.speech.create()` with:
   - `model="tts-1-hd"` (high-quality TTS model)
   - `voice="onyx"` (deep, warm voice suitable for Santa)
   - `input=text` (the message to synthesize)
   - `speed=0.9` (slower for jovial effect)
4. Write response bytes directly to `pere-noel.mp3`

## Critical Notes for Agents

### Environment Setup

- Requires valid OpenAI API key set as `OPENAI_API_KEY` environment variable
- Model `tts-1-hd` (high quality) or `tts-1` (faster) available
- **Important**: Voice parameter must be one of: alloy, echo, fable, onyx, nova, shimmer, coral, verse, ballad, ash, sage, marin, cedar. No custom "santa" voice exists.

### File Execution

- **Note**: File is named `santa.js` but contains Python code
- Run with: `python3 santa.js` (NOT `node santa.js`)
- Output: Creates `pere-noel.mp3` in the working directory

### Content & Localization

- Message is in French ("Pere Noël" = Father Christmas/Santa Claus)
- Includes traditional Santa vocalization: "Ho ho ho!"
- Production-ready message; preserve tone and language when modifying

## Common Tasks

### Testing

```bash
# Verify dependencies installed
python3 -c "import openai; print(openai.__version__)"

# Test API connectivity and audio generation
python3 santa.js
```

### Extension Examples

- Change voice: Replace `voice="onyx"` with another from supported list above
- Translate message: Modify the text variable
- Speed adjustment: Change `speed=0.9` (0.25 to 4.0 range)
- Output format: API returns MP3 by default; add `response_format="aac"` or `"opus"` for alternatives

## Key Files

- [santa.js](santa.js) - Main entry point (Python script with error handling)
- [README.md](README.md) - Project description

## Patterns & Conventions

- Single-file approach with comprehensive error handling
- Graceful failure messages when dependencies or API key missing
- French cultural context (Pere Noël = Santa)
- Comprehensive voice and parameter validation on error responses
