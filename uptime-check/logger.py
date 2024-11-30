import subprocess
import time


def ping_every(hostname, filename, interval):
    while True:
        print(log(hostname, filename))
        time.sleep(interval)


def log(hostname, filename):
    current_time = time.time()
    current_status = get_current_status(hostname)

    log_string = f'{current_time},{current_status}'

    append_to_file(filename, log_string + '\n')
    return log_string


def get_current_status(hostname):
    command = ['ping', '-c', '1', hostname]
    return subprocess.run(args=command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode


def append_to_file(filename, text):
    with open(filename, 'a') as myfile:
        myfile.write(text)


if __name__ == '__main__':
    hostname = 'facebook.com'
    logfile = 'ping.log'
    interval_in_seconds = 60 # every minute
    ping_every(hostname, logfile, interval_in_seconds)
