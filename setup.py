import setuptools

with open("README.md", "r") as fh:
  
    long_description = fh.read()
      
    setuptools.setup(
        name="gauge",
        version="0.0.1",
        author="Killian Lucas, Roger Hu",
        author_email="killian@drinkwater.ai",
        description="Qualitative LLM evals",
        long_description=long_description, # don't touch this, this is your README.md
        long_description_content_type="text/markdown",
        url="https://github.com/KillianLucas/gauge",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.6',
    )