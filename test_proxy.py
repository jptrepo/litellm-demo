#!/usr/bin/env python3
"""
Simple test script for LiteLLM proxy
"""

import requests
import json
import sys

def test_litellm_proxy(base_url="http://localhost:4000", api_key="sk-1234"):
    """Test the LiteLLM proxy with a simple chat completion"""
    
    url = f"{base_url}/v1/chat/completions"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    # Test data
    test_cases = [
        {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": "Say hello in one word"}]
        },
        {
            "model": "claude-3-5-haiku", 
            "messages": [{"role": "user", "content": "What's 2+2?"}]
        },
        {
            "model": "gemini-flash",
            "messages": [{"role": "user", "content": "Name one planet"}]
        }
    ]
    
    print("Testing LiteLLM Proxy...")
    print(f"Base URL: {base_url}")
    print("-" * 50)
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest {i}: {test_case['model']}")
        
        try:
            response = requests.post(url, headers=headers, json=test_case, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                content = data['choices'][0]['message']['content']
                print(f"✅ Success: {content}")
            else:
                print(f"❌ Error {response.status_code}: {response.text}")
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Connection error: {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

def check_health(base_url="http://localhost:4000"):
    """Check if the proxy is running"""
    try:
        response = requests.get(f"{base_url}/health", timeout=5)
        if response.status_code == 200:
            print(f"✅ LiteLLM proxy is running at {base_url}")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except requests.exceptions.RequestException:
        print(f"❌ Cannot connect to {base_url}")
        return False

if __name__ == "__main__":
    print("LiteLLM Proxy Test Script")
    print("=" * 50)
    
    # Check if proxy is running
    if not check_health():
        print("\nMake sure LiteLLM proxy is running:")
        print("docker-compose up -d")
        sys.exit(1)
    
    # Run tests
    test_litellm_proxy()
    
    print(f"\n{'='*50}")
    print("Test completed!")
    print("\nTo view API docs: http://localhost:4000/docs")
    print("To view admin UI: http://localhost:4000/ui")
