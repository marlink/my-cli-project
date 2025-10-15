import os
import argparse
import google.generativeai as genai
from dotenv import load_dotenv

def main():
    """Main function to run the Gemini AI script."""
    parser = argparse.ArgumentParser(description="Generate content using Google Gemini AI.")
    parser.add_argument("prompt", nargs="?", default="Explain how AI works in a few words", help="The prompt to send to the AI model.")
    args = parser.parse_args()

    # Load environment variables from a .env file
    load_dotenv()

    print("Python 3 detected:", os.sys.version)

    # Roo or AI Studio integration goes here

    # --- AI Studio Integration ---
    try:
        # For security, it's best to use an environment variable for your API key.
        # You can set it in your terminal like this:
        # export GOOGLE_API_KEY="YOUR_API_KEY"
        api_key = os.environ.get("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable not set.")

        genai.configure(api_key=api_key)

        # Using gemini-1.5-flash, a fast and versatile model.
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(args.prompt)

        print("\n--- Gemini Response ---")
        print(response.text)
        print("-----------------------\n")

    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
