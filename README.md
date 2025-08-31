# LiteLLM Docker Setup

This setup uses Docker Compose to run LiteLLM proxy server with multiple LLM providers.

## Quick Start

### 1. Set up your API keys

Copy the example environment file and add your API keys:

```bash
cp env.example .env
```

Edit `.env` file with your actual API keys:
- OpenAI API key from https://platform.openai.com/api-keys
- Anthropic API key from https://console.anthropic.com/
- Google API key from https://aistudio.google.com/app/apikey
- Azure OpenAI credentials (if using Azure)
- AWS credentials (if using Bedrock)

### 2. Start the LiteLLM proxy

```bash
docker-compose up -d
```

This will:
- Pull the latest LiteLLM Docker image
- Start the proxy server on port 4000
- Mount your configuration file
- Load your API keys from environment variables

### 3. Test the setup

Test with curl:
```bash
curl -X POST 'http://localhost:4000/v1/chat/completions' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer sk-1234' \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

Or test with Python:
```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-1234",  # Your master key from config
    base_url="http://localhost:4000"
)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

### 4. Access the UI

Open your browser and go to:
- API Documentation: http://localhost:4000/docs
- Admin UI: http://localhost:4000/ui

## Available Models

The current configuration includes:
- **OpenAI**: gpt-4o, gpt-4o-mini, gpt-3.5-turbo
- **Anthropic**: claude-3-5-sonnet, claude-3-5-haiku
- **Google**: gemini-pro, gemini-flash

## Configuration

### Modify Models
Edit `litellm-config.yaml` to add/remove models or change configurations.

### Change Master Key
Update the `master_key` in `litellm-config.yaml` for security.

### Add Database
Uncomment and configure the `database_url` in `litellm-config.yaml` for persistent key management.

## Commands

```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Restart services
docker-compose restart

# Update to latest image
docker-compose pull && docker-compose up -d
```

## Troubleshooting

1. **Port already in use**: Change the port mapping in `docker-compose.yml`
2. **API key errors**: Verify your API keys in the `.env` file
3. **Configuration errors**: Check the syntax of `litellm-config.yaml`

## Security Notes

- Change the default master key (`sk-1234`) to something secure
- Keep your `.env` file private and don't commit it to version control
- Consider using a database for production deployments
