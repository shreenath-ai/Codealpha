import os
import shutil
import re

# ============================================
#   TASK AUTOMATION WITH PYTHON SCRIPTS
#   CodeAlpha Internship Task 3
#   Author: Python Intern
# ============================================


# ─────────────────────────────────────────
#  TASK A: Move all .jpg files to a new folder
# ─────────────────────────────────────────
def move_jpg_files(source_folder=".", destination_folder="jpg_files"):
    """Move all .jpg files from source folder to destination folder."""
    print("\n" + "=" * 50)
    print("  📁 JPG FILE MOVER")
    print("=" * 50)

    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"  ✅ Created folder: '{destination_folder}'")

    # Find and move all .jpg files
    jpg_files = [f for f in os.listdir(source_folder)
                 if f.lower().endswith(".jpg")]

    if not jpg_files:
        print(f"  ⚠️  No .jpg files found in '{source_folder}'")
        return

    moved = 0
    for filename in jpg_files:
        src = os.path.join(source_folder, filename)
        dst = os.path.join(destination_folder, filename)
        shutil.move(src, dst)
        print(f"  📸 Moved: {filename} → {destination_folder}/")
        moved += 1

    print(f"\n  ✅ Done! Moved {moved} .jpg file(s) to '{destination_folder}/'")


# ─────────────────────────────────────────
#  TASK B: Extract email addresses from a .txt file
# ─────────────────────────────────────────
def extract_emails(input_file="emails_input.txt", output_file="extracted_emails.txt"):
    """Extract all email addresses from a txt file and save to another file."""
    print("\n" + "=" * 50)
    print("  📧 EMAIL EXTRACTOR")
    print("=" * 50)

    # Create a sample input file if it doesn't exist (for demo purposes)
    if not os.path.exists(input_file):
        sample_text = """
        Hello, please contact us at support@codealpha.tech for help.
        You can also reach john.doe@gmail.com or jane_smith@yahoo.com.
        Our sales team is at sales@company.org and info@business.net.
        Invalid emails like @nodomain or noatsign.com are ignored.
        Another valid one: intern2024@python.dev
        """
        with open(input_file, "w") as f:
            f.write(sample_text)
        print(f"  📄 Sample file created: '{input_file}'")

    # Read the input file
    with open(input_file, "r") as f:
        content = f.read()

    # Regex pattern to find emails
    email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    emails = re.findall(email_pattern, content)

    if not emails:
        print("  ⚠️  No email addresses found.")
        return

    # Remove duplicates and sort
    unique_emails = sorted(set(emails))

    # Save to output file
    with open(output_file, "w") as f:
        f.write("Extracted Email Addresses\n")
        f.write("=" * 30 + "\n")
        for email in unique_emails:
            f.write(email + "\n")

    print(f"  Found {len(unique_emails)} email(s):")
    for email in unique_emails:
        print(f"    ✉️  {email}")
    print(f"\n  ✅ Saved to '{output_file}'")


# ─────────────────────────────────────────
#  TASK C: Scrape the title of a webpage and save it
# ─────────────────────────────────────────
def scrape_webpage_title(url="https://www.codealpha.tech", output_file="webpage_title.txt"):
    """Scrape the title of a webpage and save it to a file."""
    print("\n" + "=" * 50)
    print("  🌐 WEBPAGE TITLE SCRAPER")
    print("=" * 50)

    try:
        import urllib.request
        print(f"  🔍 Fetching: {url}")

        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode("utf-8", errors="ignore")

        # Extract title using regex
        title_match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
        title = title_match.group(1).strip() if title_match else "No title found"

        print(f"  📌 Title found: {title}")

        # Save to file
        with open(output_file, "w") as f:
            f.write(f"URL   : {url}\n")
            f.write(f"Title : {title}\n")

        print(f"  ✅ Title saved to '{output_file}'")

    except Exception as e:
        print(f"  ❌ Error fetching page: {e}")
        print("  💡 Tip: Make sure you have internet access.")


# ─────────────────────────────────────────
#  MAIN MENU
# ─────────────────────────────────────────
def main():
    print("=" * 50)
    print("  🤖 TASK AUTOMATION — CodeAlpha Task 3")
    print("=" * 50)
    print("\n  Choose an automation task:")
    print("  1. Move all .jpg files to a new folder")
    print("  2. Extract emails from a .txt file")
    print("  3. Scrape webpage title and save it")
    print("  4. Run ALL tasks")
    print("  0. Exit")

    while True:
        choice = input("\n  Enter your choice (0-4): ").strip()

        if choice == "1":
            move_jpg_files()
        elif choice == "2":
            extract_emails()
        elif choice == "3":
            scrape_webpage_title()
        elif choice == "4":
            move_jpg_files()
            extract_emails()
            scrape_webpage_title()
        elif choice == "0":
            print("\n  Goodbye! 👋")
            break
        else:
            print("  ⚠️  Invalid choice. Please enter 0-4.")


if __name__ == "__main__":
    main()