import re 
def use_regex(input_text):
    pattern = re.compile(r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(?:-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|live\/|v\/)?)([\w\-]+)(\S+)?$", re.IGNORECASE)
    return bool(pattern.match(input_text))
