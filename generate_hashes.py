import hashlib
import subprocess

# File paths
files_to_hash = {
    "input/Reviews.txt": r"C:\Users\jrupa\OneDrive\Desktop\Hasmitha\sentiment analysis\extracted\hashes.txt",  # <-- update if needed
    "output/Reviews.csv": r"C:\Users\jrupa\OneDrive\Desktop\Hasmitha\sentiment analysis\extracted\Reviews.csv",
    "output/database.sqlite": r"C:\Users\jrupa\OneDrive\Desktop\Hasmitha\sentiment analysis\extracted\database.sqlite",
}

def get_md5(file_path):
    try:
        hasher = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return "File not found"

def get_git_commit_hash():
    try:
        # Use your actual git.exe path here if needed
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=r"C:\Users\jrupa\OneDrive\Desktop\Hasmitha\sentiment analysis",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True,
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return "Git commit hash not found"
    except Exception as e:
        return f"Error getting git commit hash: {e}"

def main():
    print("Current git commit:")
    print(get_git_commit_hash())
    print("\nCurrent input/ouput md5 hashes:")
    for label, path in files_to_hash.items():
        print(f"MD5 ({label}) = {get_md5(path)}")

if __name__ == "__main__":
    main()
