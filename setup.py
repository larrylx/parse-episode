import setuptools

with open("README.md", "r") as md:
  long_description = md.read()

setuptools.setup(
  name="parse-episode",
  version="0.1.0",
  author="Larry Liang",
  author_email="0lambdas_amici@icloud.com",
  description="Parse episode from a TV show file name or title.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/larrylx/parse-episode",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)