import os 
import json

print(os.name)

if os.name == 'nt':
	# install the be5invis.vscode-custom-css extension
	os.system('code --install-extension be5invis.vscode-custom-css')
	# edit the settings.json file
	with open(os.path.expanduser('~/AppData/Roaming/Code/User/settings.json'), 'r') as f:
		settings = json.load(f)
		settings['vscode_custom_css.imports'] = [
			'file:///' + os.path.abspath('custom.css').replace('//', '/')
		]
		settings['vscode_custom_css.policy'] = True
	with open(os.path.expanduser('~/AppData/Roaming/Code/User/settings.json'), 'w') as f:
		json.dump(settings, f, indent=4)
	