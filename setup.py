from setuptools import setup

setup(
    name = 'snapshot_test',
    version = '0.1',
    author = "Robin Norwood",
    author_email = "danieldoan1512@gmail.com",
    description = "Snapshot is a tool to manage AWS EC2 snapshots",
    license = "GPLv3+",
    packages=['shotty'],
    url='https://github.com/akafinal/snapshot_test',
    install_requires= [
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
