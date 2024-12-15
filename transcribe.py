
SYSTEM_MESSAGE = "prompts/system_message.txt"
EXTRACT_PROMPT = "prompts/extract_text.txt"
FORMAT_PROMPT = "prompts/format_religious_text.txt"

def get_prompt(prompt_path: str) -> str:
    message = None
    with open(prompt_path, "r") as file:
        message = file.read()
        
    return message    

SYSTEM_MESSAGE = get_prompt(SYSTEM_MESSAGE)
EXTRACT_PROMPT = get_prompt(EXTRACT_PROMPT)
FORMAT_PROMPT = get_prompt(FORMAT_PROMPT)

