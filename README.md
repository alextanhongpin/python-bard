# Bard


## Setup


Use `pipenv install` to initialize local python.

```bash
$ pipenv shell
```

## Useful commands

```bash
# Install package
$ pip install -q google-generativeai

# Generate requirements txt
$ pip freeze > requirements.txt

# Install from requirements.txt
$ pip install -r requirements.txt
```

## Example

```bash
curl \
-H 'Content-Type: application/json' \
-d '{ "prompt": { "text": "Write a story about a magic backpack"} }' \
"https://generativelanguage.googleapis.com/v1beta3/models/text-bison-001:generateText?key=YOUR_API_KEY"
```
