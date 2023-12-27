from setuptools import setup, find_namespace_packages
from setup_helper import find_all_resource_files

# -- Apps Definition -- #
namespace = 'tethysapp'
app_package = "snow_inspector"
release_package = "tethysapp-" + app_package

# -- Python Dependencies -- #
dependencies = []

# -- Get Resource File -- #
resource_files = find_all_resource_files(app_package, namespace)


setup(
    name=release_package,
    version="3.0.0",
    description="Snow Inspector",
    long_description="Snow Inspector",
    keywords="replace_keywords",
    author="",
    author_email="_email",
    url="",
    license="",
    packages=find_namespace_packages(),
    package_data={"": resource_files},
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,
)
