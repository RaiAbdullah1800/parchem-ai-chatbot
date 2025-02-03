import os
import toml

secrets = {}

# Read environment variables starting with "STREAMLIT_SECRET_"
for key, value in os.environ.items():
    if key.startswith("STREAMLIT_TOML"):
        parts = key[len("STREAMLIT_TOML"):].lower().split('__')
        current = secrets
        for part in parts[:-1]:
            current = current.setdefault(part, {})
        current[parts[-1]] = value

# Create the .streamlit folder if it doesn't exist
os.makedirs(".streamlit", exist_ok=True)

# Write the secrets.toml file
with open(".streamlit/secrets.toml", "w") as f:
    toml.dump(secrets, f)