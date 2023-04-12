import os

import subprocess

last_tag = subprocess.check_output(['git', 'describe', '--tags', '--abbrev=0']).decode().strip()

commit_message = subprocess.check_output(['git', 'log', '-1', '--pretty=%B']).decode().strip()

if 'feat' in commit_message:
    version_type = 'minor'
elif 'fix' in commit_message:
    version_type = 'patch'
else:
    version_type = 'other'

if version_type == 'other':
    new_version = last_tag
else:
    major, minor, patch = [int(x) for x in last_tag.split('.')]
    if version_type == 'patch':
        patch += 1
    elif version_type == 'minor':
        minor += 1
        patch = 0
    new_version = f'{major}.{minor}.{patch}'

version = new_version
print(f'New version: {version}')
os.system(f"sed -i 's/version=\".*\"/version=\"{version}\"/' setup.py")

os.system("rm -rf dist")
os.system("rm -rf build")
os.system("rm -rf localizedpydantic.egg-info")

os.system("python setup.py sdist bdist_wheel")

os.system("twine check dist/*")

os.system("twine upload dist/*")
