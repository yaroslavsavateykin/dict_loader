import json
from dict_loader import DictLoader
import yaml

a = (
    DictLoader()
    .load_json_file("../omd2tex/omd2tex/default/settings.json")
    .to_obs_dict()
    .dict
)
b = (
    DictLoader()
    .load_json_file("../omd2tex/omd2tex/default/preamble.json")
    .to_obs_dict()
    .dict
)

print(json.dumps({**a, **b}))

print()

print(yaml.dump({**a, **b}))
