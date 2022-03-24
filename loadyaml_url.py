import urllib.request  # the lib that handles the url stuff
import yaml

# Load a yaml file from url
def loadyaml_url(url):
    """loadyaml_url(url)

    Args:
        url (string):url to the yaml file

    Returns:
        data: yaml object with the opened data
    """
    # Open and read the url -> decode bytestream to utf8
    db_lib = urllib.request.urlopen(url).read().decode('utf8')
    # Load yaml encoded file
    data = yaml.safe_load(db_lib)
    return data
