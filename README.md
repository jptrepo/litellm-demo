# LiteLLM Docker Setup

This setup uses Docker Compose to run LiteLM proxy server with multiple LLM providers.

## 📁 Project Files

This workspace contains:

- [`docker-compose.yml`](docker-compose.yml) - Docker Compose configuration
- [`litellm-config.yaml`](litellm-config.yaml) - LiteLLM model configuration
- [`env.example`](env.example) - Template for environment variables
- [`.env`](.env) - Your actual API keys (git-ignored)
- [`test_proxy.py`](test_proxy.py) - Test script for the proxy
- [`.gitignore`](.gitignore) - Protects sensitive files from git

## 🚀 Quick Start

### 1. Set up your API keys

**⚠️ The `.env` file already exists but needs your actual API keys!**

Edit the existing `.env` file with your actual API keys:

```bash
# Edit your .env file
code .env
# or
nano .env
```

Add your API keys:

- OpenAI API key from <https://platform.openai.com/api-keys>
- Anthropic API key from <https://console.anthropic.com/>
- Google API key from <https://aistudio.google.com/app/apikey>
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

### 4. Test with the provided script

Run the included test script:

```bash
python test_proxy.py
```

This script will:

- Check if the proxy is running
- Test multiple models (OpenAI, Anthropic, Google)
- Show you exactly what's working

### 5. Access the UI

Open your browser and go to:

- API Documentation: <http://localhost:4000/docs>
- Admin UI: <http://localhost:4000/ui>

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

- **Never commit `.env` files** - They contain sensitive API keys (protected by `.gitignore`)
- Change the default master key (`sk-1234`) to something secure in `litellm-config.yaml`
- The `.gitignore` file ensures `.env` won't be tracked by git
- Consider using a database for production deployments

## 🎯 What's Next?

Your workspace is ready! The next logical steps are:

1. **Create a feature branch**: `git checkout -b feature/litellm-docker-setup`
2. **Add your API keys** to the `.env` file
3. **Start the Docker setup**: `docker-compose up -d`
4. **Test with the script**: `python test_proxy.py`
5. **Commit your working setup** when everything works
