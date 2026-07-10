from setuptools import find_packages,setup

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> list:
    """
    Reads a requirements.txt file and returns a clean list of dependencies.
    Removes '-e .' if present (used for editable installs).
    """
    requirements = []
    
    # Open the requirements file in read mode
    with open(file_path) as file_obj:
        # Read all lines into a list
        requirements = file_obj.readlines()
        
        # Strip whitespace/newline characters from each requirement
        requirements = [req.strip() for req in requirements]

        # Remove the special editable install flag if present
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

        # Return the final cleaned list of requirements
        return requirements


setup(
    name="email_spam_detection",
    version="0.0.1",
    author="Aneesh Jose",
    author_email="aneeshjose012@gmail.com",
    description="End-to-End Email Spam Detection using NLP and Machine Learning",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=get_requirements("requirements.txt"),
)
