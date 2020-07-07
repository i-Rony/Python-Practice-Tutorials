# Example 01
from importlib import metadata
metadata.version("pip")

pip_metadata = metadata.metadata("pip")
list(pip_metadata)

pip_metadata["Home-page"]

pip_metadata["Requires-Python"]

len(metadata.files("pip"))

# Example 02
[p for p in metadata.files("realpython-reader") if p.suffix == ".py"]

init_path = _[0]  # Underscore access last returned value in the REPL
print(init_path.read_text())

# Example 03
metadata.requires("realpython-reader")
