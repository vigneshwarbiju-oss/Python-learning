import subprocess
import sys

# Image name and dockerfile path
image_name = "my-python-image"
dockerfile_path = "asdf.dockerfile"

try:
    # Build the Docker image
    print("Building Docker image...")
    build_cmd = ["docker", "build", "-f", dockerfile_path, "-t", image_name, "."]
    result = subprocess.run(build_cmd, check=True, capture_output=True, text=True)
    print("Build output:")
    print(result.stdout)
    
    # Run the Docker container
    print("\nRunning Docker container...")
    run_cmd = ["docker", "run", image_name, "python", "--version"]
    result = subprocess.run(run_cmd, check=True, capture_output=True, text=True)
    print("Container output:")
    print(result.stdout)
    
    print("\nDocker container ran successfully!")
    
except FileNotFoundError:
    print("Error: Docker is not installed. Please install Docker Desktop first.")
    sys.exit(1)
except subprocess.CalledProcessError as e:
    print(f"Error running Docker command: {e}")
    print(f"Error output: {e.stderr}")
    sys.exit(1)
