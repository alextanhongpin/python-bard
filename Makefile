include .env
export

test:
	curl \
	-H 'Content-Type: application/json' \
	-d '{ "prompt": { "text": "Write a story about a magic backpack"} }' \
	"https://generativelanguage.googleapis.com/v1beta3/models/text-bison-001:generateText?key=${BARD_API_KEY}"
