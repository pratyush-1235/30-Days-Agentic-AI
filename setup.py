from setuptools import setup, find_packages

setup(
    name="agentic-ai-30-days",
    version="1.0.0",
    description="30 Days of Agentic AI - a hands-on curriculum for building AI agents",
    author="30 Days of Agentic AI Contributors",
    license="MIT",
    packages=find_packages(exclude=["tests", "*.tests"]),
    python_requires=">=3.11",
    install_requires=[
        line.strip()
        for line in open("requirements.txt")
        if line.strip() and not line.startswith("#")
    ],
)
