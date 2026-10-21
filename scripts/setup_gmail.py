#!/usr/bin/env python3
"""Setup script for Gmail integration."""

import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
GMAIL_DIR = REPO / ".local-workspace/gmail"
CREDENTIALS_PATH = GMAIL_DIR / "credentials.json"


def main():
    print("=" * 60)
    print("Career Ops - Gmail Integration Setup")
    print("=" * 60)

    if CREDENTIALS_PATH.exists():
        print(f"\n✓ Credentials found at {CREDENTIALS_PATH}")
        with CREDENTIALS_PATH.open() as f:
            creds = json.load(f)
        client_id = creds.get("installed", {}).get("client_id", "unknown")
        print(f"  Client ID: {client_id}")
    else:
        print(f"\n✗ Credentials NOT found at {CREDENTIALS_PATH}")
        print("\nTo set up Gmail API access:")
        print("1. Go to https://console.cloud.google.com/")
        print("2. Create/select project 'Career Ops'")
        print("3. Enable Gmail API: APIs & Services > Library > Gmail API")
        print("4. Create OAuth2 credentials: APIs & Services > Credentials > Create > OAuth client ID")
        print("   - Application type: Desktop app")
        print("   - Name: Career Ops Gmail Monitor")
        print("5. Download JSON and save as:")
        print(f"   {CREDENTIALS_PATH}")
        print("\n6. Configure OAuth consent screen:")
        print("   - User Type: External")
        print("   - Scopes: gmail.readonly, gmail.metadata")
        print("   - Test users: Add your Gmail address")

    # Check token
    token_path = GMAIL_DIR / "token.json"
    if token_path.exists():
        print(f"\n✓ Token found at {token_path}")
        with token_path.open() as f:
            token = json.load(f)
        print(f"  Email: {token.get('client_id', 'unknown')}")
        print(f"  Expires: {token.get('expiry', 'unknown')}")
    else:
        print(f"\n✗ No token found - run authentication after adding credentials")

    print("\n" + "=" * 60)
    print("Next steps:")
    print("1. Add credentials.json to .local-workspace/gmail/")
    print("2. Run: python3 -m workspace_app.gmail_integration --auth")
    print("3. Test sync: python3 -m workspace_app.gmail_integration --sync")
    print("4. Start monitor: python3 -m workspace_app.gmail_integration --monitor")
    print("=" * 60)


if __name__ == "__main__":
    main()