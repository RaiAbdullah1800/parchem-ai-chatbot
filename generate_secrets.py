import os
import toml

secrets = {}

# Read environment variables starting with "STREAMLIT_SECRET_"
for key, value in os.environ.items():
    if key.startswith("STREAMLIT_SECRET_"):
        parts = key[len("STREAMLIT_SECRET_ "):].lower().split('__')
        current = secrets
        for part in parts[:-1]:
            current = current.setdefault(part, {})
        current[parts[-1]] = value

# Get the STREAMLIT_TOML environment variable
streamlit_toml = os.getenv("STREAMLIT_TOML")

# Create the .streamlit folder if it doesn't exist
os.makedirs(".streamlit", exist_ok=True)

# Write the secrets.toml file
with open(".streamlit/secrets.toml", "w") as f:
    toml.dump(secrets, f)

# Write the secrets.toml file if STREAMLIT_TOML is set
if streamlit_toml:
    with open(".streamlit/secrets.toml", "w") as f:
        f.write(streamlit_toml)
else:
    print("STREAMLIT_TOML environment variable is not set.")