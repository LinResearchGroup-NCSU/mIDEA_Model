import re

native_content = "RKKRIPYSKGQLRELEREYAANKFITKDKRRKISAATSLSERQITIWFQNRRVKEKKVLAKllejjt.lteeeejejeettltltttte.lelltjj"
cleaned_native_content = re.sub(r'[^A-Z]', '', native_content)

print(cleaned_native_content)
