import sys
import logging


sys.path.insert(0, '/home/www-data/blog_root/')
logging.basicConfig(stream=sys.stderr)
from blog.blog import app as application
