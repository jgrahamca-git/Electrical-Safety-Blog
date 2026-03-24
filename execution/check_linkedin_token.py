import os
import sys
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def check_linkedin_token():
    """
    Validates the LinkedIn access token by calling the /v2/userinfo endpoint.
    Exits with code 0 if valid, code 1 if expired/invalid.

    LinkedIn OAuth 2.0 tokens expire after ~60 days.
    If this check fails, generate a new token via the LinkedIn Developer Portal
    and update LINKEDIN_ACCESS_TOKEN in the .env file.
    """
    token = os.getenv("LINKEDIN_ACCESS_TOKEN")
    author_urn = os.getenv("LINKEDIN_AUTHOR_URN")

    if not token or not author_urn:
        print("ERROR: LINKEDIN_ACCESS_TOKEN or LINKEDIN_AUTHOR_URN is missing from .env.")
        print("ACTION: Add both variables to the .env file before posting.")
        sys.exit(1)

    url = "https://api.linkedin.com/v2/userinfo"
    headers = {
        "Authorization": f"Bearer {token}",
        "X-Restli-Protocol-Version": "2.0.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            data = response.json()
            name = data.get("name", "Unknown")
            print(f"SUCCESS: Token is valid. Authenticated as: {name}")
            print(f"Author URN in .env: {author_urn}")
            sys.exit(0)

        elif response.status_code == 401:
            print("ERROR: Token is EXPIRED or INVALID (401 Unauthorized).")
            print()
            print("ACTION — To generate a new token:")
            print("  1. Go to https://www.linkedin.com/developers/apps and open your app.")
            print("  2. Navigate to the 'Auth' tab.")
            print("  3. Under 'OAuth 2.0 tools', click 'Request access token'.")
            print("  4. Select scopes: openid, profile, w_member_social.")
            print("  5. Copy the new access token.")
            print("  6. Update LINKEDIN_ACCESS_TOKEN in your .env file.")
            print("  Note: Tokens expire after ~60 days. Run this check before every posting session.")
            sys.exit(1)

        else:
            print(f"ERROR: Unexpected response {response.status_code}: {response.text}")
            sys.exit(1)

    except requests.exceptions.Timeout:
        print("ERROR: Request timed out. Check your network connection.")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: Unexpected error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    check_linkedin_token()
