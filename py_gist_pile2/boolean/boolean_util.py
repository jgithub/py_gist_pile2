def is_truelike(input):
  if input is None:
    return False
  if str(input).strip().lower() in ['true', 'yes', 't', 'y', '1']:
    return True
  return False
