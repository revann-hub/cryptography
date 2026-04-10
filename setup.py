from setuptools import setup, find_packages

setup(
    name="cryptotoolbox_az",         # Kitabxananın adı
    version="1.0.0",                 # Versiya
    author="Your Name",              # Öz adını yaza bilərsən
    author_email="email@example.com",
    description="A comprehensive Python library for symmetric, asymmetric, and classical cryptography.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/username/repository", # Öz GitHub linkin
    packages=find_packages(),        # Avtomatik olaraq bütün alt paketləri tapır
    install_requires=[               # Xarici asılılıqlar
        "pycryptodome",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security :: Cryptography",
    ],
    python_requires='>=3.6',
)
