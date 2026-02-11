from setuptools import setup, find_packages

setup(
    name="title-cover-generator",
    version="1.0.0",
    description="Generate clean title cover images for social media",
    author="TClawE",
    py_modules=["generate"],
    python_requires=">=3.8",
    install_requires=[
        "Pillow>=9.0.0",
    ],
)
