import os
import sys
import argparse
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def post_to_linkedin(text, article_url=None):
    """
    Posts text and an optional article link to LinkedIn using the UGC Posts API.
    Requires LINKEDIN_ACCESS_TOKEN and LINKEDIN_AUTHOR_URN in .env.
    """
    token = os.getenv("LINKEDIN_ACCESS_TOKEN")
    author_urn = os.getenv("LINKEDIN_AUTHOR_URN")

    if not token or not author_urn:
        print("ERROR: LINKEDIN_ACCESS_TOKEN or LINKEDIN_AUTHOR_URN is missing from the .env file.")
        print("Please obtain these credentials from the LinkedIn Developer Portal and add them.")
        sys.exit(1)

    url = 'https://api.linkedin.com/v2/ugcPosts'
    headers = {
        'Authorization': f'Bearer {token}',
        'X-Restli-Protocol-Version': '2.0.0',
        'Content-Type': 'application/json'
    }

    # Construct the base post object
    post_data = {
        "author": author_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": text
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    # Attach the article URL if provided
    if article_url:
        post_data["specificContent"]["com.linkedin.ugc.ShareContent"]["shareMediaCategory"] = "ARTICLE"
        post_data["specificContent"]["com.linkedin.ugc.ShareContent"]["media"] = [
            {
                "status": "READY",
                "originalUrl": article_url
            }
        ]

    try:
        response = requests.post(url, headers=headers, json=post_data)
        response.raise_for_status()
        result = response.json()
        print("SUCCESS: Post published successfully to LinkedIn!")
        print(f"Post ID: {result.get('id')}")
        return True
        
    except requests.exceptions.HTTPError as e:
        print(f"ERROR: HTTP Request failed with status code {e.response.status_code}")
        print(f"Response Body: {e.response.text}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: An unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deterministic script to post content to LinkedIn.")
    parser.add_argument("--text", required=True, help="The text content of the LinkedIn post.")
    parser.add_argument("--url", required=False, help="An optional URL to attach as a linked article preview.")
    
    args = parser.parse_args()
    
    post_to_linkedin(args.text, args.url)
