from datetime import datetime

AUTHOR = "Anders Lauridsen"
SITENAME = "Anders Lauridsen"
SITESUBTITLE = "Blogging and Image Gallery"
SITEURL = "https://anders-lauridsen.dk"

PATH = "content"
THEME = "themes/flex"

TIMEZONE = "Europe/Copenhagen"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Instagram", "https://www.instagram.com/anderslauridsen98/"),
    ("LinkedIn", "https://www.linkedin.com/in/anders-hl-lauridsen/"),
)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# pelican-hyde settings
# BIO = (
#     "I use my personal website for blogging and for hosting an image gallery of "
#     "images that I want to display."
# )
# PROFILE_IMAGE = "profile.JPG"
# COLOR_THEME = "0c"

# flex settings
SITETITLE = "Anders Lauridsen"
SITELOGO = "images/profile.JPG"
SITEDESCRIPTION = "Blogging and Image Gallery"
COPYRIGHT_NAME = "Anders Lauridsen"
COPYRIGHT_YEAR = f"{datetime.now().year}"
MAIN_MENU = True
MENUITEMS = [
    ("Blog", "https://anders-lauridsen.dk"),
]
PAGES_SORT_ATTRIBUTE = True
ARTICLE_ORDER_BY = "reversed-date"
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True

# Plugin
PLUGINS = []
