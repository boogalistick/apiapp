import signal, logging, time, sys
from async_server import AsyncHTTPServer
import settings

logging.basicConfig(filename=settings.log_file_path, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler())

class GracefulKiller:
    httpd = None
    def __init__(self):
        logging.info('Started');
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)
        self.httpd = AsyncHTTPServer(settings.http_host, settings.http_port)

        while (self.httpd != None):
            time.sleep(1)

    def exit_gracefully(self, signum, frame):
        if self.httpd != None :
            self.httpd.stop(1)
            self.httpd = None

        logging.info('Finished')

if __name__ == '__main__':
    killer = GracefulKiller()
