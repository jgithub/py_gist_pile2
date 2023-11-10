import datetime
import json

def d4l(input):
  """decorate-for-logging"""
  
  if input is None:
    return "<null> (null)"
  elif input is None:
    return "<undefined> (undefined)"
  elif isinstance(input, str):
    return f"'{input}' (string, {len(input)})"
  elif isinstance(input, int) or isinstance(input, float):
    return f'{input} (number)'
  elif isinstance(input, bool):
    return 'TRUE (boolean)' if input else 'FALSE (boolean)'
  elif isinstance(input, dict) or isinstance(input, list):
    try:
        return json.dumps(input)
    except Exception:
        pass
  elif isinstance(input, list):
    parts = []

    input_as_list = input
    if len(input_as_list) > 0:
        parts.append(d4l(input_as_list[0]))
    if len(input_as_list) > 2:
        parts.append("…")
    if len(input_as_list) > 1:
        parts.append(d4l(input_as_list[-1]))

    return f"Array(len={len(input_as_list)}) [{', '.join(parts)}]"
  elif isinstance(input, Exception):
    stack_str = str(input)
    if hasattr(input, "stack"):
        stack_str = input.stack.replace("\r\n", "\\n,   ").replace("\n\r", "\\n,   ").replace("\n", "\\n,   ").replace("\r", "\\n,   ")
    return f'{input} (Error, stack: {stack_str})'
  elif isinstance(input, datetime.datetime):
    return input.isoformat()
  
  return str(input)