import re


def remove_unclean_data(chat_export_file):

    pattern = r"(\d{1,2}/\d{1,2}/\d{2}, \d{1,2}:\d{2}\s*(AM|PM)? - [\w\s]+:)|(\d{1,2}/\d{1,2}/\d{2}, \d{1,2}:\d{2}\s*(AM|PM)? -)|(\s*Bytgate:\s*<Media omitted>)|(\s*Toyosi:\s*<Media omitted>)"

    with open(chat_export_file, 'r') as clean:
        content = clean.read()
        cleaned_text = re.sub(pattern, " ", content)
        return tuple(cleaned_text.split("\n"))


def remove_non_message_text(export_text_lines):
    messages = export_text_lines[1:-1]

    filter_out_msgs = ("  <Media omitted>",)
    return tuple((msg for msg in messages if msg not in filter_out_msgs))


def clean_corpus(chat_export_file):
    message_corpus = remove_unclean_data(chat_export_file)
    cleaned_corpus = remove_non_message_text(message_corpus)
    return cleaned_corpus
