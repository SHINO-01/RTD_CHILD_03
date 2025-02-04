import os

DOCS_DIR = "docs"
INDEX_FILE = os.path.join(DOCS_DIR, "index.md")

def generate_toc():
    toc = ["# Welcome to the Documentation\n", "## Table of Contents\n"]
    for root, _, files in os.walk(DOCS_DIR):
        for file in files:
            if file.endswith(".md") and file != "index.md":
                rel_path = os.path.relpath(os.path.join(root, file), DOCS_DIR)
                title = file.replace(".md", "").replace("-", " ").title()
                toc.append(f"- [{title}]({rel_path})\n")

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.writelines(toc)

if __name__ == "__main__":
    generate_toc()
