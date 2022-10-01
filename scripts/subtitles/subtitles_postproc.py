import logging
import sys

from subliminal import region

logging.basicConfig(filename='/app/scripts.log', level=logging.DEBUG)
region.configure('dogpile.cache.memory')

try:
    logging.info("starting subtitles fetcher")
    main()
    sys.exit(0)
except Exception as e:
    logging.error(("No commandline parameters found", e))
    sys.exit(1)
