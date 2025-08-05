from pathlib import Path
from setuptools import find_packages, setup

this_dir = Path(__file__).parent

setup(
    name="ml_ai_interview_mastery",
    version="0.0.1",
    description="End-to-end interview prep notebooks & libs",
    author="Your Name",
    python_requires=">=3.9",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        # core runtime deps (same as requirements.txt *minus* tooling)
        "numpy",
        "pandas",
        "scikit-learn",
        "torch",
        "torchaudio",
        "torchvision",
        "matplotlib",
        "seaborn",
        "transformers",
        "sentencepiece",
        "datasets",
        "langchain>=0.2.0",
        "faiss-cpu",            # vector search
        "fastapi",
        "uvicorn[standard]",
        "pydantic",
    ],
)
