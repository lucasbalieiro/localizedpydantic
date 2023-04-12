import os

version = "0.1.2"
os.system(f"sed -i 's/version=\".*\"/version=\"{version}\"/' setup.py")

os.system("rm -rf dist")
os.system("rm -rf build")
os.system("rm -rf localizedpydantic.egg-info")

os.system("python setup.py sdist bdist_wheel")

os.system("twine check dist/*")

os.system("twine upload dist/*")
