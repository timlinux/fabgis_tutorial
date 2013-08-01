# For vagrant support you need to do this:
from fabtools.vagrant import vagrant
# Now import some fabgis tasks
from fabgis.tilestream import setup_tilestream, start_tilestream, setup_tilestream_daemon
from fabgis.tilemill import setup_tilemill, start_tilemill
